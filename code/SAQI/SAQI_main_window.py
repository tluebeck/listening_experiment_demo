import sys
from PyQt5 import QtCore, QtWidgets
import numpy as np


from .GUI import SAQI_goodbye_gui, SAQI_welcome_gui, SAQI_main_gui, breeze_resources

class SAQI_main_window(QtWidgets.QMainWindow):

    def __init__(self, ssr_handler, jack_handler, experiment_handler, language='english', verbose=1, monitor_id=1, skip_on_no_difference=0):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        ssr_handler
        jack_handler
        experiment_handler
        language
        verbose
        """
        super().__init__()
        self.setWindowTitle('SAQI EXPERIMENT')
        self._ssr_handler = ssr_handler
        self._jack_handler = jack_handler
        self._experiment_handler = experiment_handler
        self._ui = None
        self._language = language
        self._verbose = verbose
        self.sliders_per_page = self._experiment_handler.attributes_per_page
        self.show_categories = False
        self._is_playing = False
        self._touched_raters = None
        self._active_stimuli = None
        self._skip_on_no_difference = skip_on_no_difference # 0: always ask for all attributes
                                                            # 1: original saqi paradigm skip all attributes if no difference was detected
        self.start_welcome_screen()
        self._monitor = QtWidgets.QDesktopWidget().screenGeometry(monitor_id)

    def start_welcome_screen(self):
        self._ui = SAQI_welcome_gui.Ui_SAQI_welcome_gui()
        self._ui.setupUi(self, self._language)

        # callbacks
        self._ui.age_combobox.activated.connect(lambda: self.set_participant_infos(0))
        self._ui.gender_combobox.activated.connect(lambda: self.set_participant_infos(1))
        self._ui.LE_exp_combobox.activated.connect(lambda: self.set_participant_infos(2))
        self._ui.BinTech_exp_combobox.activated.connect(lambda: self.set_participant_infos(3))

        self._ui.start_btn.clicked.connect(self.finish_login)
        self._ui.calibrate_btn.clicked.connect(self._ssr_handler.calibrate_tracker)

        self.checked_participant_infos = list([0, 0, 0, 0])

    def set_participant_infos(self, id):
        self.checked_participant_infos[id] = 1

    def finish_login(self):
        if self._ssr_handler._is_calibrated:
            if np.sum(self.checked_participant_infos) == len(self.checked_participant_infos):
                self.checked_participant_infos[0] = self._ui.age_combobox.currentText()
                self.checked_participant_infos[1] = self._ui.gender_combobox.currentText()
                self.checked_participant_infos[2] = self._ui.LE_exp_combobox.currentText()
                self.checked_participant_infos[3] = self._ui.BinTech_exp_combobox.currentText()
                self._experiment_handler.set_participant_infos(self.checked_participant_infos)
                if self._verbose:
                    print('start experiment')

                message_box = QtWidgets.QMessageBox()
                message_box.setGeometry(QtCore.QRect(700, 500, 151, 32))
                message_box.move(self._monitor.left()/1.7, self._monitor.top()*1.5)

                if self._language == 'english':
                    message = 'Thanks for participating in our listenining experiment\n The experiment starts now. Please click on the "A", or "B" button to listen to the stimuli.'

                elif self._language == 'german':
                    message = 'Danke für die Teilnahme an unserm Hörversuch\n Der Versuch startet nun. Bitte klicke auf "A", oder "B" um den jeweiligen Stimulus abzuspielen.'
                else:
                    message = ''
                message_box = QtWidgets.QMessageBox.information(message_box, 'Error', message, QtWidgets.QMessageBox.Ok)

                self.start_SAQI_test()
            else:
                message_box = QtWidgets.QMessageBox()
                message_box.setGeometry(QtCore.QRect(700, 500, 151, 32))
                message_box.move(self._monitor.left() / 1.7, self._monitor.top()*1.5)

                if self._language == 'english':
                    message = 'Please fill all fields.'
                elif self._language == 'german':
                    message = 'Bitte fülle alle Felder aus.'
                else:
                    message = ''
                message_box = QtWidgets.QMessageBox.warning(message_box, 'Error', message,
                                                            QtWidgets.QMessageBox.Ok)
        else:
            message_box = QtWidgets.QMessageBox()
            message_box.setGeometry(QtCore.QRect(700, 500, 151, 32))
            message_box.move(self._monitor.left() / 1.7, self._monitor.top()*1.5)

            if self._language == 'english':
                message = 'Please calibrate tracker before starting the experiment.'
            elif self._language == 'german':
                message = 'Bitte calibriere den Head tracker bevor du das Experiment startest.'
            else:
                message = ''
            message_box = QtWidgets.QMessageBox.warning(message_box, 'Error', message,
                                                            QtWidgets.QMessageBox.Ok)

    def start_SAQI_test(self):
        self._ui = SAQI_main_gui.Ui_SAQI_main_gui()
        self._ui.setupUi(self, categories=self._experiment_handler._categories, language=self._language)

        self._ui.stimuli_A_btn.clicked.connect(lambda: self.select_stimuli('A'))
        self._ui.stimuli_B_btn.clicked.connect(lambda: self.select_stimuli('B'))

        self._ui.diff_btn.clicked.connect(lambda: self.on_overal_diff_btn(True))
        self._ui.no_diff_btn.clicked.connect(lambda: self.on_overal_diff_btn(False))

        self._ui.play_pause_btn.clicked.connect(self.play_pause_sound)
        self._ui.next_trial_btn.clicked.connect(self.on_trial_finished)

        #  for idx in range(0, self.sliders_per_page): # somehow assigning in a loop does not work
        self._ui.rating_sliders[0].valueChanged.connect(lambda: self.on_slider_touched(0))
        self._ui.rating_sliders[1].valueChanged.connect(lambda: self.on_slider_touched(1))
        self._ui.rating_sliders[2].valueChanged.connect(lambda: self.on_slider_touched(2))
        self._ui.rating_sliders[3].valueChanged.connect(lambda: self.on_slider_touched(3))
        self._ui.rating_sliders[4].valueChanged.connect(lambda: self.on_slider_touched(4))
        self._ui.rating_sliders[5].valueChanged.connect(lambda: self.on_slider_touched(5))
        self._ui.rating_sliders[6].valueChanged.connect(lambda: self.on_slider_touched(6))
        self._ui.rating_sliders[7].valueChanged.connect(lambda: self.on_slider_touched(7))
        self._ui.rating_sliders[8].valueChanged.connect(lambda: self.on_slider_touched(8))

        self._ui.set_zero_btns[0].clicked.connect(lambda: self.on_set_zero_btn(0))
        self._ui.set_zero_btns[1].clicked.connect(lambda: self.on_set_zero_btn(1))
        self._ui.set_zero_btns[2].clicked.connect(lambda: self.on_set_zero_btn(2))
        self._ui.set_zero_btns[3].clicked.connect(lambda: self.on_set_zero_btn(3))
        self._ui.set_zero_btns[4].clicked.connect(lambda: self.on_set_zero_btn(4))
        self._ui.set_zero_btns[5].clicked.connect(lambda: self.on_set_zero_btn(5))
        self._ui.set_zero_btns[6].clicked.connect(lambda: self.on_set_zero_btn(6))
        self._ui.set_zero_btns[7].clicked.connect(lambda: self.on_set_zero_btn(7))
        self._ui.set_zero_btns[8].clicked.connect(lambda: self.on_set_zero_btn(8))

        self._ui.quality_labels[0].is_under_mouse.connect(lambda: self.display_circumscription(0))
        self._ui.quality_labels[1].is_under_mouse.connect(lambda: self.display_circumscription(1))
        self._ui.quality_labels[2].is_under_mouse.connect(lambda: self.display_circumscription(2))
        self._ui.quality_labels[3].is_under_mouse.connect(lambda: self.display_circumscription(3))
        self._ui.quality_labels[4].is_under_mouse.connect(lambda: self.display_circumscription(4))
        self._ui.quality_labels[5].is_under_mouse.connect(lambda: self.display_circumscription(5))
        self._ui.quality_labels[6].is_under_mouse.connect(lambda: self.display_circumscription(6))
        self._ui.quality_labels[7].is_under_mouse.connect(lambda: self.display_circumscription(7))
        self._ui.quality_labels[8].is_under_mouse.connect(lambda: self.display_circumscription(8))

        if not self._experiment_handler._restore:
            # set first attribute
            self.set_attributes(self._experiment_handler.get_current_attributes())

            # set first test signal
            self._jack_handler.change_test_signal(self._experiment_handler.get_current_test_signal())

            if self.show_categories:
                self._ui.category_title_label.show()
                self.update_category_labels()
        else:
            message_box = QtWidgets.QMessageBox()
            message_box.setGeometry(QtCore.QRect(700, 500, 151, 32))
            message_box.move(self._monitor.left() / 1.7, self._monitor.top() * 1.5)

            if self._language == 'english':
                message = f'Results of participant {self._experiment_handler._restore} are restored and experiment will continue now.'
            elif self._language == 'german':
                message = f'Ergebnisse von Teilnehmer {self._experiment_handler._restore} werden geeladen und das Experiment nun forgeführt.'
            else:
                message = ''
            message_box = QtWidgets.QMessageBox.warning(message_box, 'Error', message,
                                                        QtWidgets.QMessageBox.Ok)
            # prepare restored experiment
            self._experiment_handler.restore_experiment()

            # set first attribute
            self.set_attributes(self._experiment_handler.get_current_attributes())

            # set first test signal
            self._jack_handler.change_test_signal(self._experiment_handler.get_current_test_signal())

    def display_circumscription(self, id):
        attributes = self._experiment_handler.get_current_attributes()
        self._ui.circumscription_label.show()
        self._ui.circumscription_label.setText(
            f"{attributes[id].get_quality_name()}:{attributes[id].get_circumscription()}")
        self._ui.circumscription_label.adjustSize()

    def set_attributes(self, SAQI_attributes):
        # hide every slider and label
        for idx in range(0, self.sliders_per_page):
            self._ui.rating_sliders[idx].hide()
            self._ui.scale_end_labels_low[idx].hide()
            self._ui.scale_end_labels_high[idx].hide()
            self._ui.quality_labels[idx].hide()
            self._ui.attribute_separator_lines[idx].hide()
            self._ui.circumscription_label.hide()


            self._ui.rating_sliders[idx].setTickPosition(QtWidgets.QSlider.TicksLeft)
            self._ui.rate_b_labels[idx].hide()
            self._ui.set_zero_btns[idx].hide()

            self._ui.rating_sliders[idx].setInvertedAppearance(False)
            self._ui.rating_sliders[idx].setInvertedControls(False)

            self._ui.slider_ticks[idx].hide()

        cnt = 0
        for attribute in SAQI_attributes:
            slider_x_position = self._ui.rating_sliders[cnt].geometry().getCoords()[0]
            slider_zero_geometry = self._ui._rating_slider_zero_geometry

            if attribute.rating_scale_mode == 'unipolar':
                self._ui.rating_sliders[cnt].setGeometry(
                    QtCore.QRect(slider_x_position, slider_zero_geometry[1] + int(slider_zero_geometry[3] / 4),
                                 slider_zero_geometry[2], int(slider_zero_geometry[3] / 2)))

                self._ui.rating_sliders[cnt].setMinimum(0)
                self._ui.rating_sliders[cnt].setMaximum(30)
                self._ui.rating_sliders[cnt].setValue(0)

                slider_geometry = self._ui.rating_sliders[cnt].geometry().getCoords()
                self._ui.scale_end_labels_high[cnt].setGeometry(QtCore.QRect(slider_geometry[0] - 18,
                                                                             slider_geometry[1] + 148,
                                                                             55, 16))
                self._ui.scale_end_labels_low[cnt].setGeometry(QtCore.QRect(slider_geometry[0] - 18,
                                                                            slider_geometry[1] - 31,
                                                                            55, 16))
                self._ui.scale_end_labels_high[cnt].setText(attribute.get_scale_end_label_low())
                self._ui.scale_end_labels_low[cnt].setText(attribute.get_scale_end_label_high())

                self._ui.slider_ticks[cnt].draw(mode='unipolar',
                                                y=int(slider_zero_geometry[1] + int(slider_zero_geometry[3] / 4)),
                                                intervals=3,
                                                slider_height=int(slider_zero_geometry[3] / 2))
                self._ui.slider_ticks[cnt].show()
            else:
                self._ui.rating_sliders[cnt].setGeometry(
                    QtCore.QRect(slider_x_position, slider_zero_geometry[1], slider_zero_geometry[2],
                                 slider_zero_geometry[3]))

                self._ui.rating_sliders[cnt].setMinimum(-30)
                self._ui.rating_sliders[cnt].setMaximum(30)
                self._ui.rating_sliders[cnt].setValue(0)
                self._ui.rate_b_labels[cnt].show()
                self._ui.set_zero_btns[cnt].show()

                self._ui.rating_sliders[cnt].setTickPosition(QtWidgets.QSlider.TicksLeft)

                slider_geometry = self._ui.rating_sliders[cnt].geometry().getCoords()
                self._ui.scale_end_labels_high[cnt].setGeometry(QtCore.QRect(slider_geometry[0] - 18,
                                                                             self._ui._scale_end_label_high_y_pos,
                                                                             55, 16))
                self._ui.scale_end_labels_low[cnt].setGeometry(QtCore.QRect(slider_geometry[0] - 18,
                                                                            self._ui._scale_end_label_low_y_pos+10,
                                                                            55, 16))
                self._ui.scale_end_labels_high[cnt].setText(attribute.get_scale_end_label_high())
                self._ui.scale_end_labels_low[cnt].setText(attribute.get_scale_end_label_low())

                self._ui.slider_ticks[cnt].draw(mode='bipolar',
                                                y=int(slider_zero_geometry[1]),
                                                intervals=7,
                                                slider_height=int(slider_zero_geometry[3]))
                self._ui.slider_ticks[cnt].show()
                self._touched_raters = np.zeros(self.sliders_per_page)

            self._ui.scale_end_labels_high[cnt].adjustSize()
            self._ui.scale_end_labels_low[cnt].adjustSize()

            if attribute.id == 0:  # first mandatory overall difference rating with 2 additional yes/no buttons
                self._ui.diff_btn.setDisabled(False)
                self._ui.diff_btn.setStyleSheet("border: 0.5px solid white;")
                self._ui.no_diff_btn.setDisabled(False)
                self._ui.no_diff_btn.setStyleSheet("border: 0.5px solid white;")
                self._ui.diff_btn.show()
                self._ui.no_diff_btn.show()

                self._ui.slider_ticks[0].hide()
                self._ui.scale_end_labels_high[0].hide()
                self._ui.scale_end_labels_low[0].hide()
                self._ui.rating_sliders[0].hide()
                self._touched_raters = np.array([0])  # one button, one slider have to be touche for the next trial
            else:
                self._ui.diff_btn.hide()
                self._ui.no_diff_btn.hide()
                self._ui.attribute_separator_lines[cnt].show()
                self._ui.scale_end_labels_high[cnt].show()
                self._ui.rating_sliders[cnt].show()
                self._ui.scale_end_labels_low[cnt].show()

            self._ui.quality_labels[cnt].setText(f"{attribute.get_quality_name()}")
            self._ui.quality_labels[cnt].adjustSize()
            self._ui.quality_labels[cnt].show()

            self._ui.task_label.setText(attribute.get_phrase())
            cnt = cnt + 1

        if self._verbose:
            if self._language == 'german':
                self._ui._trial_cnt.setText(f"Nr: {self._experiment_handler._trial_page_cnt + 1}")
            else:
                self._ui._trial_cnt.setText(f"No: {self._experiment_handler._trial_page_cnt + 1}")


        self._ui.next_trial_btn.setDisabled(True)

    def on_overal_diff_btn(self, value):
        if value:  # if the participant detected a difference:
            self._ui.rating_sliders[0].show()
            self._ui.scale_end_labels_low[0].show()
            self._ui.scale_end_labels_high[0].show()
            self._ui.slider_ticks[0].show()
            self._ui.diff_btn.setStyleSheet("border: 3px solid white;")
            self._ui.no_diff_btn.setStyleSheet("border: 0.5px solid white;")

        else:  # if not, skip this condition
            if self._verbose:
                print('Could not detect any difference, skip this trial')

            self._ui.diff_btn.setStyleSheet("border: 0.5px solid white;")
            self._ui.no_diff_btn.setStyleSheet("border: 3px solid white;")

            # if no difference were detected, enable next trial button
            self._ui.next_trial_btn.setDisabled(False)

            self._ui.rating_sliders[0].hide()
            self._ui.scale_end_labels_low[0].hide()
            self._ui.scale_end_labels_high[0].hide()
            self._ui.slider_ticks[0].hide()

    def on_slider_touched(self, slider_id):
        try:
            self._touched_raters[slider_id] = 1
        except:
            print('')

        # if all sliders and btns were touched, enable next trial btn
        if np.sum(self._touched_raters) == len(self._touched_raters):
            self._ui.next_trial_btn.setDisabled(False)

    def on_set_zero_btn(self, id):
        self._ui.rating_sliders[id].setValue(0)
        self.on_slider_touched(id)

    def on_trial_finished(self):
        print('Trial finished\n\n')

        result_list = list()
        skip = False
        new_condition = False
        if self._experiment_handler.get_current_attributes()[0].id == 0: # attribute was difference
            if self._ui.rating_sliders[0].isVisible():  # if sliders are visible a difference was detected
                result_list.append('yes')
                result_list.append(self._ui.rating_sliders[0].value())
            else: # no difference was detected 
                result_list.append('no')
                if self._skip_on_no_difference:
                    skip = True
                    new_condition = True
                self._ssr_handler.mute_all()  # just mute if signal changes
        else:
            self._ssr_handler.mute_all()  # just mute if signal changes
            for idx in range(0, self.sliders_per_page):
                result_list.append(self._ui.rating_sliders[idx].value())
            new_condition = True

        if (self._experiment_handler.finished_trials > self._experiment_handler._total_num_ratings / 2) \
                and not self._experiment_handler._paused and not self._experiment_handler.get_current_attributes()[
                                                                     0].id == 0:
            # pausing after a COMPLETE trial if half of the conditions are done.
            print(" ------- PAUSE -------")
            message_box = QtWidgets.QMessageBox()
            message_box.setGeometry(QtCore.QRect(700, 500, 151, 32))
            message_box.move(self._monitor.left() / 1.7, self._monitor.top() * 1.5)

            if self._language == 'english':
                message = f'Halfway done. Please make a breakn and click on Ok to continue.'
            elif self._language == 'german':
                message = f'Die Hälfte ist geschafft. Bitte machen Sie eine Pause und klicken Sie auf Ok, um fortzufahren'
            else:
                message = ''
            message_box = QtWidgets.QMessageBox.warning(message_box, 'Error', message,
                                                        QtWidgets.QMessageBox.Ok)
            self._experiment_handler._paused = 1

        self._experiment_handler.trial_finished(values=result_list, skip=skip)
        self.continue_experiment(new_condition=new_condition)

    def continue_experiment(self, new_condition=False):
        if self._experiment_handler.get_current_attributes()[0].id == 0:
            if self._language == "english":
                self._ui.next_trial_btn.setText("next")
            elif self._language == "german":
                self._ui.next_trial_btn.setText("Weiter")
        else:
            if self._language == "english":
                self._ui.next_trial_btn.setText("next trial")
            elif self._language == "german":
                self._ui.next_trial_btn.setText("Nächster Trial")

        if not self._experiment_handler._is_complete:

            attribute = self._experiment_handler.get_current_attributes()
            self.set_attributes(attribute)
            if new_condition:
                if self._jack_handler._is_playing:
                    self._jack_handler.pause_sound()
                    self._jack_handler.change_test_signal(self._experiment_handler.get_current_test_signal())
                    self._jack_handler.play_sound()
                else:
                    self._jack_handler.change_test_signal(self._experiment_handler.get_current_test_signal())

            if self.show_categories:
                self.update_category_labels()
        else:
            print('End of the experiment')
            if self._jack_handler._is_playing:
                self._jack_handler.pause_sound()
            if not self._verbose:
                self._experiment_handler.back_up_results()
            self.start_goodbye_screen()

    def update_category_labels(self):
        attributes = self._experiment_handler.get_current_attributes()
        for attribute in attributes:
            if not attribute.get_category_name == '':
                for label in self._ui.category_labels:
                    label.setStyleSheet("border: 1px solid white;")

    def select_stimuli(self, ID):
        self._active_stimuli = ID
        if ID == 'A':
            if self._verbose:
                print(f'A: {self._experiment_handler.get_current_stimuli_ids()[1]}')
            self._ssr_handler.select_source(self._experiment_handler.get_current_stimuli_ids()[1])
            self._ui.stimuli_A_btn.setStyleSheet("border: 3px solid white;")
            self._ui.stimuli_B_btn.setStyleSheet("border: 1px solid white;")

        elif ID == 'B':
            if self._verbose:
                print(f'B: {self._experiment_handler.get_current_stimuli_ids()[0]}')
            self._ssr_handler.select_source(self._experiment_handler.get_current_stimuli_ids()[0])
            self._ui.stimuli_A_btn.setStyleSheet("border: 1px solid white;")
            self._ui.stimuli_B_btn.setStyleSheet("border: 3px solid white;")


    def play_pause_sound(self):
        if self._jack_handler._is_playing:
            self._jack_handler.pause_sound()
            if self._language == 'english':
                self._ui.play_pause_btn.setText("play")
            elif self._language == 'german':
                self._ui.play_pause_btn.setText("Play")
            self._is_playing = False

        else:
            self._jack_handler.play_sound()
            if self._language == 'english':
                self._ui.play_pause_btn.setText("pause")
            elif self._language == 'german':
                self._ui.play_pause_btn.setText("Pause")
            self._is_playing = True

            if self._active_stimuli is None:
                self.select_stimuli('A')  # if no stimuli is selected, play 'A'

    def start_goodbye_screen(self):
        self._ui = SAQI_goodbye_gui.Ui_SAQI_goodbye_gui()
        self._ui.setupUi(self, self._language)
        self._ui.finish_btn.clicked.connect(self.close_app)

    def close_app(self):
        self._ssr_handler.destroy_handler()
        self._jack_handler.destroy_handler()
        self.close()
