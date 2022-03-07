import jack
import threading

import numpy as np
import soundfile as sf

import queue
import time

class JackClientHandler(object):
    def __init__(self, sampling_rate, num_ssr_srcs):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2019 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        sampling_rate
        num_ssr_srcs
        """
        self._sampling_rate = sampling_rate
        self._is_playing = False
        self._num_ssr_srcs = num_ssr_srcs

        # open new jack audio thread
        self._audio_thread = JackAudioThread(sampling_rate, num_ssr_srcs)

        # set playback source
        self._audio_thread.set_source('file_playback', '../src/test_signals/MARA_LE_DRUMS.wav')

        #self._audio_thread.set_source('file_playback', 'Drums_48kHz_AKG_K702.wav')

        # starting jack audio threat
        self._audio_thread.start()

        # and ensure initial pause
        self._audio_thread.pause()

    def play_sound(self):
        print('play')
        if self._is_playing is False:
            self._audio_thread.play()
            self._is_playing = True
        else:
            print('Source already playing')

    def pause_sound(self):
        print('pause')
        if self._is_playing is True:
            self._audio_thread.pause()
            self._is_playing = False
        else:
            print('Source already paused')

    def change_test_signal(self, filename):
        self._audio_thread.set_source('file_playback', file_name=filename)

    def get_state(self):
        return self._is_playing

    def destroy_handler(self):
        self._audio_thread.kill()

class JackAudioThread(threading.Thread):
    def __init__(self, fs, num_ssr_srcs, num_buffers=5):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2019 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        fs
        num_ssr_srcs
        num_buffers
        """
        threading.Thread.__init__(self)
        self._id = 'Testsignal_playback_py'
        self._mode = 'noise'  # 'file_playback' for plaback from file
        self._fs = fs
        self._num_ssr_srcs = num_ssr_srcs
        self._num_buffer = num_buffers
        # initialize jack client
        self._jack_client = jack.Client(self._id)
        # register output port
        self._jack_client.outports.register('output_1')
        # get buffer size from JackServer
        self._blocksize = self._jack_client.blocksize
        # define timeout for filling the queue, if timeout time will exceed, queue.Full waring fill be called
        self._timeout = self._num_buffer * self._blocksize / self._fs
        # declare blockgenerator for file playback
        self._block_generator = None
        self._sound_file_name = None
        self._sound_file = None
        # register queue & events
        self._queue = queue.Queue(maxsize=self._num_buffer)
        self._queue.put_nowait(np.zeros((1, self._blocksize)))  # Pre-fill queue with zeros
        self._play_event = threading.Event()  # event for play and pause
        self._terminate_event = threading.Event()  # event for terminating the audio thread and processing
        self._change_params = threading.Event()  # event to interrupt processing for change of parameters

        # register process callback
        @self._jack_client.set_process_callback
        def process(frames):
            if self._play_event.is_set() and not self._terminate_event.is_set():
                try:
                    data = self._queue.get_nowait()
                    for channel, port in zip(data.T, self._jack_client.outports):
                        port.get_array()[:] = channel
                except queue.Empty:
                    pass
                    #print('Qeuue empty!')
            else:  # fill jack port with zeros
                for port in self._jack_client.outports:
                    port.get_array().fill(0)

    def run(self):
        print('Start Jack Audio Thread')
        # activate jack client
        self._jack_client.activate()
        # do jack routing
        self.jack_routing(self._num_ssr_srcs)

        # waiting for play
        self._play_event.wait()
        if self._mode == 'file_playback':
            # start to fill queue blockwise from audio file
            while (not self._terminate_event.is_set()):
                for data in self._block_generator:  # samples x channels
                    self._play_event.wait()
                    #self._terminate_event.wait()
                    if self._terminate_event.is_set():
                        return
                    try:
                        self._queue.put(data, timeout=self._timeout)
                    except queue.Full:
                        if not self._terminate_event.is_set() and self._play_event.is_set():
                            pass
                print('End of file, fill block generator')
                self.fill_block_generator()
        else:
            # start to fill queue with noise
            while (not self._terminate_event.is_set()):
                self._play_event.wait()
                try:
                    noise = np.random.normal(0, 1, size=self._blocksize) * 0.2  # * np.hanning(self._blocksize) * 0.2
                    self._queue.put(noise[:, np.newaxis], timeout=self._timeout)  # samples x channels
                except queue.Full:
                    if not self._terminate_event.is_set() and self._play_event.is_set():
                        pass
            print('Noise generator stopped!')

    def jack_routing(self, num_ssr_srcs):
        # connect python to SSR
        for idx in range(0, num_ssr_srcs):
            try:
                self._jack_client.connect(f'{self._id}:output_1', 'BrsRenderer:in_{:01d}'.format(idx + 1))
            except:
                print('No SSR running, routing failed')

    def play(self):
        self._play_event.set()

    def pause(self):
        self._play_event.clear()

    def set_source(self, mode, file_name=None):

        self._change_params.set()
        self._play_event.clear()
        time.sleep(0.2)

        if mode == 'file_playback' and file_name is None:
            self._mode = 'noise'
        else:
            self._mode = mode

        if self._mode == 'file_playback':
            self._sound_file_name = file_name
            self.fill_block_generator()

        time.sleep(0.2)
        self._play_event.set()
        self._change_params.clear()

    def fill_block_generator(self):
        if self._block_generator is not None:
            self._block_generator.close()
            
        self._sound_file = sf.SoundFile(self._sound_file_name)

        self._block_generator = self._sound_file.blocks(blocksize=self._blocksize, dtype='float32', always_2d=True,
                                                        fill_value=0)
    def kill(self):
        print('Stopping Jack Audio Thread')
        self._terminate_event.set()
        self._play_event.set()  # ugly but necessarry to escape from noise generator loop!
