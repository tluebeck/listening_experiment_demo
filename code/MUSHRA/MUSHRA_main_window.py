from PyQt5 import QtCore, QtWidgets
import numpy as np

from MUSHRA.GUI.log_in_gui import Ui_Log_in
from MUSHRA.GUI.mushra_gui import Ui_Mushra
from MUSHRA.GUI.black_scren import Ui_Black_Screen


class mushra_main_window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle('Main Window')
        self._ui = None

        self.start_log_in()

        self._ssr_handler_ = None
        self._sd_handler = None
        self._exp_handler = None

        self._calibrated = False

        self._current_trial = 0
        self._touched_sliders = None
        self._all_sliders_touched = 0

        self.num_stimuli_per_page = None
    # _________________________________________________________________________________________________________________#
    # Main window methods:
    def set_gui_handler(self, ssr_handler, sd_handler, exp_handler ):

        self._sd_handler = sd_handler
        self._ssr_handler = ssr_handler
        self._exp_handler = exp_handler

        # some checks
        assert self._exp_handler.get_num_stimuli_per_page() < 8
        self.num_stimuli_per_page = self._exp_handler.get_num_stimuli_per_page()

    def closeEvent(self, event: object):
        self._ssr_handler.destroy_handler()
        self._sd_handler.destroy_handler()

        self.close()

    #__________________________________________________________________________________________________________________#
    def start_log_in(self):
        self._ui = Ui_Log_in()
        self._ui.setupUi(self)

        # register log-in-GUI callbacks
        self._ui.start_btn.clicked.connect(self.start_experiment)
        self._ui.calibrate_btn.clicked.connect(self.calibrate)

    def calibrate(self):
        self._calibrated = True
        self._ssr_handler.calibrate_tracker()

    def start_experiment(self):
        if self.get_user_data():
            if self._calibrated:
                print('Experiment Starts')
                self._exp_handler.initialize()
                if self._exp_handler.is_training_desired():
                    self.start_training_gui()
                else:
                    self.start_mushra_gui()
            else:
                Q = QtWidgets.QMessageBox()
                Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
                Q = QtWidgets.QMessageBox.information(Q, 'Error', "Please orient to the front and press the 'Calibrate' button.",
                                                      QtWidgets.QMessageBox.Ok)
        else:
            Q = QtWidgets.QMessageBox()
            Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
            Q = QtWidgets.QMessageBox.information(Q, 'Error', 'Please fill in all fields. Try again.',
                                        QtWidgets.QMessageBox.Ok)

    #__________________________________________________________________________________________________________________#
    def start_training_gui(self):
        #self._ui = Ui_Mushra_4()
        #self._ui.setupUi(self)

        self._ui = Ui_Mushra()
        num_training_stimuli = 3
        if self._exp_handler.get_num_stimuli_per_page() < num_training_stimuli:
            num_training_stimuli=self._exp_handler.get_num_stimuli_per_page()

        self._ui.setupUi(self, num_training_stimuli, 1)

        if self._sd_handler.get_state():
            _translate = QtCore.QCoreApplication.translate
            self._sd_handler.stop_sound()
            self._ui.play_button.setText(_translate("Experiment", "Play"))

        # register training-GUI callbacks
        #self._ui.next_trial_btn.clicked.connect(self.next_stimuli)
        self._ui.play_button.clicked.connect(self.play_stop_sound)
        self._ui.reconnect_btn.clicked.connect(self.reconnect_ssr)
        self._ui.Ref_btn.clicked.connect(lambda: self.play_reference(training=True))

        for idx in range(num_training_stimuli):
            if idx == 0:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(0))
                #self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(0))
            elif idx == 1:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(1))
                #self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(1))
            elif idx == 2:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(2))
                #self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(2))
            elif idx == 3:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(3))
                #self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(3))

        self._ui.next_trial_btn.clicked.connect(self.start_mushra_gui)

    #__________________________________________________________________________________________________________________#
    def start_mushra_gui(self):

        self._touched_sliders = np.zeros((1, self.num_stimuli_per_page))
        self._ui = Ui_Mushra()
        self._ui.setupUi(self, self. num_stimuli_per_page, self._exp_handler._num_trials)

        if self._sd_handler.get_state():
            _translate = QtCore.QCoreApplication.translate
            self._sd_handler.pause_sound()
            self._ui.play_button.setText(_translate("Experiment", "Play"))

        # register Mushra-GUI callbacks
        self._ui.next_trial_btn.clicked.connect(self.next_stimuli)
        self._ui.play_button.clicked.connect(self.play_stop_sound)
        self._ui.reconnect_btn.clicked.connect(self.reconnect_ssr)
        self._ui.Ref_btn.clicked.connect(self.play_reference)

        # somehow connecting callback to btn and sliders is not working in a loop
        # indices = np.array([0, 1, 2, 3, 4, 5, 6, 7])
        # indices = np.array(range(0, self.num_stimuli_per_page))
        # for i, arg in enumerate(indices):
        #     print(i)
        #     print(arg)
        #     self._ui.btns[i].clicked.connect(lambda: self.unmute_btn_callback(arg))
        #     self._ui.sliders[i].valueChanged.connect(lambda: self.slider_callback(arg))
        #     self._ui.sliders[i].setValue(0)
        for idx in range(self.num_stimuli_per_page):
            if idx == 0:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(0))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(0))
            elif idx == 1:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(1))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(1))
            elif idx == 2:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(2))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(2))
            elif idx == 3:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(3))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(3))
            elif idx == 4:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(4))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(4))
            elif idx == 5:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(5))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(5))
            elif idx == 6:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(6))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(6))
            elif idx == 7:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(7))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(7))
            elif idx == 8:
                self._ui.btns[idx].clicked.connect(lambda: self.unmute_btn_callback(8))
                self._ui.sliders[idx].valueChanged.connect(lambda: self.slider_callback(8))

            self._ui.sliders[idx].setValue(0)

        self._touched_sliders *= 0  # reset touched slider array
        self._all_sliders_touched = 0

        self._current_trial = 0
        self.display_current_trial()
        self.disable_next_trial_btn()

    def get_user_data(self):
        try:
            VA_exp = self._ui.VA_box.currentText()
        except:
            print('no VA_expertise!')
        try:
            LE_exp = self._ui.no_experiments.currentText()
        except:
            print('no LE_expertise!')
        try:
            age = self._ui.age_box.currentText()
        except:
            print('no age')
        if VA_exp and LE_exp and age:
            self._exp_handler.set_participant_infos(age, VA_exp, LE_exp)
            check = True
        else:
            check = False
        return check

    #__________________________________________________________________________________________________________________#
    def next_stimuli(self):
        if (self._touched_sliders == 0).any():
            Q = QtWidgets.QMessageBox()
            Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
            Q = QtWidgets.QMessageBox.information(Q, 'Error', 'Please move all sliders!',
                                                  QtWidgets.QMessageBox.Ok)
        else:
            _translate = QtCore.QCoreApplication.translate
            self._sd_handler.pause_sound()
            self._ui.play_button.setText(_translate("Experiment", "Stop"))

            result_values = []
            for idx in range(self.num_stimuli_per_page):
                # get results and reset
                result_values.append(100 - self._ui.sliders[idx].value())
                self._ui.sliders[idx].setValue(0)

            self._exp_handler.store_result(self._current_trial, result_values)

            self._touched_sliders *= 0
            self._all_sliders_touched = 0

            self._current_trial += 1
            print('Trial: ', self._current_trial + 1)
            self.display_current_trial()
            self.disable_next_trial_btn()

            if self._current_trial == self._exp_handler._num_trials:
                self.end_experiment()

    def play_stop_sound(self):
        _translate = QtCore.QCoreApplication.translate
        if self._sd_handler.get_state():
            self._sd_handler.pause_sound()
            self._ui.play_button.setText(_translate("Experiment", "Play"))
        else:
            self._sd_handler.play_sound()
            self._ui.play_button.setText(_translate("Experiment", "Stop"))

    def unmute_btn_callback(self, id, training=False):
        print('Source ', id, 'unmute!')
        if not self._sd_handler.get_state():
            self._ssr_handler.mute_all()
            self.play_stop_sound()

        trial_id = int(self._exp_handler._random_vector[id, self._current_trial])
        if training:
            print('Training!')
            if id == 0:
                trial_id = 45  # SBS BEMA N3 90deg
            if id == 1:
                trial_id = 46  # SBS MagLS N3 90deg
            if id == 2:
                trial_id = 6  # Anchor 90deg
            if id == 3:
                trial_id = 2  # Reference 90deg
        self._ssr_handler.select_source(trial_id)

    def play_reference(self, training=False):
        print('Reference unmute')
        ref_id = int(self._exp_handler._reference_ids[self._current_trial])
        if not self._sd_handler.get_state():
            self.play_stop_sound()
        if training:
            print('Training!')
            ref_id = 2

        self._ssr_handler.select_source(ref_id)

    def slider_callback(self, id):
        print(id)
        self._touched_sliders[0, id] = 1
        if (self._touched_sliders[0, :] == 1).all():
            print('all sliders touched!')
            self._all_sliders_touched = 1
            self.enable_next_trial_btn()

    def display_current_trial(self):
        _translate = QtCore.QCoreApplication.translate
        self._ui.trail_count_label.setText(_translate("Mushra", f"Trial {self._current_trial + 1} out of {self._exp_handler.get_num_trails()}"))

    def disable_next_trial_btn(self):
        print('disable next trial button')
        self._ui.next_trial_btn.setDisabled(True)

    def enable_next_trial_btn(self):
        print('enable next trial button')
        self._ui.next_trial_btn.setDisabled(False)

    def reconnect_ssr(self):
        if self._ssr_handler.get_connection_state():
            print('Connection already established!')
            #self._sd_handler._audio_thread.jack_routing(self._sd_handler._audio_thread._num_ssr_srcs)
            Q = QtWidgets.QMessageBox()
            Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
            Q = QtWidgets.QMessageBox.information(Q, 'Warning',
                                                  'SSR connection already established!',
                                                  QtWidgets.QMessageBox.Ok)
        else:
            print('Try reconnect to SSR!')
            self._ssr_handler.reconnect()
            Q = QtWidgets.QMessageBox()
            Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
            Q = QtWidgets.QMessageBox.information(Q, 'SSR Error', 'Please calibrate anew by looking to the front and press the Calibrate button!',
                                                  QtWidgets.QMessageBox.Ok)
            print('Jack Routing....')
            self._sd_handler._audio_thread.jack_routing(self._sd_handler._audio_thread._num_ssr_srcs)
            print('Here we go again. Just repeat the last trial :)')
            self._current_trial -= 1

    def end_experiment(self):
        print('end of experiment:')
        self._ui = Ui_Black_Screen()
        self._ui.setupUi(self)
        self._exp_handler.back_up_results('/Users/tluebeck/sciebo/User_study/new_results/')
        Q = QtWidgets.QMessageBox()
        Q.setGeometry(QtCore.QRect(700, 500, 151, 32))
        Q = QtWidgets.QMessageBox.information(Q, 'Finished', 'End of the experiment, Thank you for participating.',
                                              QtWidgets.QMessageBox.Ok)

        self.close()
