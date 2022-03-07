import socket

class SSRhandler():

    def __init__(self, num_sources=1, tcp_ip='127.0.0.1', tcp_port=4711, verbose=False):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2019 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        num_sources
        tcp_ip
        tcp_port
        """

        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._num_sources = num_sources
        self._tcp_ip = '127.0.0.1'
        self._tcp_port = 4711
        self._connection_state = False
        self._is_calibrated = 0
        self._verbose = verbose
        try:
            self._s.connect((tcp_ip, tcp_port))
            print('TCP connection to SSR runs')
            self._connection_state = True
            self.mute_all()
        except:
            if self._verbose:
                print('Could not establish TCP connection to SSR, run GUI without SSR')
            else:
                pass

    def destroy_handler(self):
        try:
            self._s.close()
        except:
            if self._verbose:
                print('No SSR TCP connection running, nothing to stop')
        else:
            pass

    def select_source(self, src_id):
        print('Activate Source ', src_id)

        if src_id > self._num_sources + 1:
            raise ValueError('Source does not exist')
        else:
            cmd = '<request><source id="{:01d}" mute="true"/></request>\0'
            for idx in range(1, self._num_sources + 1):
                msg = cmd.format(idx)
                try:
                    self._s.send(msg.encode('utf-8'))
                except:
                    if self._verbose:
                        print('No SSR TCP connection running!')
                    else:
                        pass
            cmd = '<request><source id="{:01d}" mute="false"/></request>\0'
            msg = cmd.format(src_id)
            try:
                self._s.send(msg.encode('utf-8'))
            except:
                if self._verbose:
                    print('No SSR TCP connection running!')
                else:
                    pass

    def calibrate_tracker(self):
        msg = '<request><state tracker="reset"/></request>\0'
        self._is_calibrated = 1
        try:
            self._s.send(msg.encode('utf-8'))
            print('tracker calibrated')
        except:
            if self._verbose:
                print('No SSR TCP connection running!')
            else:
                pass

    def mute_all(self):
        if self._verbose:
            print('Mute all sources')
        else:
            pass

        cmd = '<request><source id="{:01d}" mute="true"/></request>\0'
        for idx in range(1, self._num_sources + 1):
            msg = cmd.format(idx)
            try:
                self._s.send(msg.encode('utf-8'))
            except:
                if self._verbose:
                    print('No SSR TCP connection running!')
                else:
                    pass

    def get_connection_state(self):
        cmd = '<request><source id="{:01d}" mute="true"/></request>\0'
        msg = cmd.format(1)
        connection_state = True
        try:
            self._s.send(msg.encode('utf-8'))
        except:
            connection_state = False

        return connection_state

    def reconnect(self):
        self._is_calibrated = 0
        self._s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._s.connect((self._tcp_ip, self._tcp_port))
            print('TCP connection to SSR initialized')
        except:
            if self._verbose:
                print('Could not establish TCP connection to SSR, run GUI without SSR')
            else:
                pass
