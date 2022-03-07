  
from PyQt5 import QtCore, QtWidgets
import MUSHRA.GUI.breeze_resources
import sys
from MUSHRA.MUSHRA_test import MUSHRA_test
from MUSHRA.MUSHRA_main_window import mushra_main_window
from utils.SSR_handler import SSRhandler
from utils.jack_client_handler import JackClientHandler
import numpy as np

def main():
    print('____________________________________________________________________________________________________________')
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == '--debug':
            print("DEBUG MODE - No results will be printed!")
            debug = True
    print('____________________________________________________________________________________________________________')

    fs = 48000

    # hard coded initialization vector
    # filter X Mushra pages
    # up to 8 sliders per page are available
    random_vector = np.array([
        [1,  1,  1,  1],  # references
        [2,  2,  2,  2],  # anchors
        [3,  5,  7,  9],  # conditions to evaluate
        [4,  6,  8, 10]   # conditions to evaluate
    ])

    # _________________________________________________________________________________________________________________#
    # set up experiement
    mushra_test = MUSHRA_test(debug_mode=debug)
    mushra_test.set_test_design(random_vector)

    # create jack client, connect to server, and establish SSR connection:
    num_ssr_srcs = np.max(np.max(random_vector, axis=1), axis=0)
    jack_handler = JackClientHandler(fs, num_ssr_srcs)
    ssr_handler = SSRhandler(num_sources=num_ssr_srcs)

    # _________________________________________________________________________________________________________________#
    # start app
    app = QtWidgets.QApplication(sys.argv)

    # set stylesheet
    file = QtCore.QFile(":/dark.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())

    main_window = mushra_main_window()
    main_window.set_gui_handler(ssr_handler, jack_handler, mushra_test)
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

