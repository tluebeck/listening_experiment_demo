import sys
import numpy as np
from PyQt5 import QtCore, QtWidgets
from utils import SSR_handler, jack_client_handler

from SAQI.SAQI_test import SAQI_test
from SAQI.SAQI_main_window import SAQI_main_window
from SAQI import SAQI_vocabulary

def main():

    debug = 1
    language = 'english'
    if len(sys.argv) > 1:
        for idx, arg in enumerate(sys.argv[1:]):
            if arg == '--debug':
                debug = 1

            if arg == '--language':
                print(sys.argv[idx+2])
                if sys.argv[idx+2] == 'en':
                    language = 'english'
                elif sys.argv[idx+2] == 'ger':
                    language = 'german'
                else:
                    print('Unknown language, chose english version')
    if debug:
        print("DEBUG MODE - No results will be printed!")
    else:
        print("Start listening experiment!")

    print(f'Language: {language}')

    # define conditions: with SSR ids
    # num_trials x [condition id, reference id]
    stimuli_ssr_ids = [[3, 1],
                       [4, 1],
                       [5, 1],
                       [6, 1]]

    # define categories to test
    general = SAQI_vocabulary.General()
    timbre = SAQI_vocabulary.Timbre()
    geometry = SAQI_vocabulary.Geometry()
    room = SAQI_vocabulary.Room()
    categories = [general, timbre, geometry, room]

    # define all attributes to test
    attributes = [timbre.coloration,
                  geometry.sourcePosition,
                  geometry.externalization,
                  geometry.sourceWidth,
                  room.envelopment]

    # define test signals
    test_signals = ['../src/test_signals/MARA_LE_DRUMS.wav',
                    '../src/test_signals/MARA_LE_SPEECH.wav']

    # init app
    app = QtWidgets.QApplication(sys.argv)

    # init handlers
    num_available_src = np.max(np.max(stimuli_ssr_ids))
    ssr_handler = SSR_handler.SSRhandler(num_available_src)
    jack_handler = jack_client_handler.JackClientHandler(48000, num_available_src)

    # init experiment
    saqi_experiment = SAQI_test(stimuli_ssr_ids,
                                categories=categories,
                                attributes=attributes,
                                test_signals=test_signals,
                                attributes_per_page=5,
                                language=language,
                                debug=debug)
    # init GUI and set handlers
    Gui_main_comp = SAQI_main_window(ssr_handler,
                                     jack_handler,
                                     saqi_experiment,
                                     language=language,
                                     verbose=debug)

    # set style sheet
    file = QtCore.QFile(":/dark.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    app.aboutToQuit.connect(Gui_main_comp.close_app)

    # define monitor
    display_monitor = 2
    monitor = QtWidgets.QDesktopWidget().screenGeometry(display_monitor)
    Gui_main_comp.move(monitor.left(), monitor.top())
    # Gui_main_comp.showFullScreen()

    # show GUI
    Gui_main_comp.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
