# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
import numpy as np


class Ui_SAQI_main_gui(object):
    def setupUi(self, SAQI_main_gui, categories, language='english'):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        SAQI_main_gui
        categories
        language
        """
        SAQI_main_gui.setObjectName("SAQUI_main_gui")
        SAQI_main_gui.resize(1024, 768)

        self.centralwidget = QtWidgets.QWidget(SAQI_main_gui)
        self.centralwidget.setObjectName("centralwidget")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 10, 1004, 5))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        # Trial count
        self._trial_cnt = QtWidgets.QLabel(self.centralwidget)
        self._trial_cnt.setGeometry(QtCore.QRect(900, 18, 80, 25))
        self._trial_cnt.setObjectName("trial count")
        self._trial_cnt.setWordWrap(True)
        # self._trial_cnt.hide()

        self.stimuli_A_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stimuli_A_btn.setGeometry(QtCore.QRect(50, 610, 130, 50))   # x right / y down
        self.stimuli_A_btn.setObjectName("stimuli_A_btn")
        self.stimuli_A_btn.setStyleSheet("border: 1px solid white;")

        self.stimuli_B_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stimuli_B_btn.setGeometry(QtCore.QRect(210, 610, 130, 50))
        self.stimuli_B_btn.setObjectName("stimuli_B_btn")
        self.stimuli_B_btn.setStyleSheet("border: 1px solid white;")

        self.play_pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_pause_btn.setGeometry(QtCore.QRect(400, 620, 61, 32))
        self.play_pause_btn.setObjectName("play_pause_btn")

        self.next_trial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_trial_btn.setGeometry(QtCore.QRect(885, 632, 113, 32))
        self.next_trial_btn.setObjectName("next_trial_btn")

        # category display not implemented so far
        self.category_title_label = QtWidgets.QLabel(self.centralwidget)
        self.category_title_label.setGeometry(QtCore.QRect(630, 80, 171, 20))
        self.category_title_label.setObjectName("category_title_label")
        self.category_title_label.hide()

        self.category_labels = list()
        self.category_frames = list()
        position = np.array([520, 130])
        for category in categories:
            category_label = QtWidgets.QLabel(self.centralwidget)
            category_label.setGeometry(QtCore.QRect(position[0], position[1], 100, 20))
            category_label.setObjectName("category_label")
            category_label.setText(category.get_name())
            category_label.setStyleSheet("border: 1px solid white;")
            category_label.hide()
            self.category_labels.append(category_label)
            position[0] += 120

        # attribute window
        task_position = np.array([45, 30])
        self.task_label = QtWidgets.QLabel(self.centralwidget)
        self.task_label.setGeometry(QtCore.QRect(task_position[0], task_position[1], 295, 92))
        self.task_label.setObjectName("task_label")
        self.task_label.setWordWrap(True)

        self.diff_btn = QtWidgets.QPushButton(self.centralwidget)
        self.diff_btn.setGeometry(QtCore.QRect(task_position[0], task_position[1] + 215, 113, 32))
        self.diff_btn.setObjectName("diff_btn")
        self.diff_btn.setStyleSheet("border: 0.5px solid white;")

        self.no_diff_btn = QtWidgets.QPushButton(self.centralwidget)
        self.no_diff_btn.setGeometry(QtCore.QRect(task_position[0] + 130, task_position[1] + 215, 113, 32))
        self.no_diff_btn.setObjectName("no_diff_btn")
        self.no_diff_btn.setStyleSheet("border: 0.5px solid white;")

        # quality # not visible now
        self.quality_title = QtWidgets.QLabel(self.centralwidget)
        self.quality_title.setGeometry(QtCore.QRect(60, 140, 250, 16))
        self.quality_title.setObjectName("quality_label")
        self.quality_title.setText('Attribute:')
        self.quality_title.hide()

        self.quality_labels = list()
        quality_label_geometry = [110, 205, 80, 22]

        # circumscription:
        self.circumscription_title = QtWidgets.QLabel(self.centralwidget)
        self.circumscription_title.setGeometry(QtCore.QRect(475, 40, 460, 20)) ##-20
        self.circumscription_title.setObjectName("circumscription_title_label")

        if language == 'english':
            self.circumscription_title.setText('Circumscription: ')
        elif language == 'german':
            self.circumscription_title.setText('Beschreibung: ')

        self.circumscription_title.show()

        # show one circumscription by touching the corresponding quality label
        circumscription_label_geometry = [475, 65, 420, 130]

        self.circumscription_label = QtWidgets.QLabel(self.centralwidget)
        self.circumscription_label.setGeometry(
            QtCore.QRect(circumscription_label_geometry[0], circumscription_label_geometry[1],
                         circumscription_label_geometry[2], circumscription_label_geometry[3]))
        self.circumscription_label.setObjectName("circumscription_label")
        self.circumscription_label.setWordWrap(True)
        self.circumscription_label.setStyleSheet("border: 0.7px solid white;")
        self.circumscription_label.hide()

        # sliders
        self.rating_sliders = list()
        self._rating_slider_zero_geometry = [140, 290, 22, 290]  # 231
        self.scale_end_labels_low = list()
        self.scale_end_labels_high = list()
        slider_position = [self._rating_slider_zero_geometry[0], self._rating_slider_zero_geometry[1]]

        # separator lines
        self.attribute_separator_lines = list()
        attribute_separator_gemoetry = [80, 277, 2, 300]

        attribute_spacing = 170
        self._scale_end_label_low_y_pos = slider_position[1] + self._rating_slider_zero_geometry[3]
        self._scale_end_label_high_y_pos = slider_position[1] - 27

        self.rate_b_labels = list()
        self.slider_ticks = list()
        self.set_zero_btns = list()

        for idx in range(0, 9):
            rate_b_label = QtWidgets.QLabel(self.centralwidget)
            rate_b_label.setGeometry(QtCore.QRect(quality_label_geometry[0], quality_label_geometry[1]+35,
                                                   quality_label_geometry[2], quality_label_geometry[3]))
            rate_b_label.setObjectName("rate_b_label")
            rate_b_label.setWordWrap(True)
            rate_b_label.setFont(QtGui.QFont("Helvetica", 12))
            rate_b_label.hide()

            self.rate_b_labels.append(rate_b_label)

            quality_label = TrackedLabel(self.centralwidget)
            quality_label.setGeometry(QtCore.QRect(quality_label_geometry[0], quality_label_geometry[1],
                                                   quality_label_geometry[2], quality_label_geometry[3]))
            quality_label.setObjectName("quality_label")
            quality_label.setWordWrap(True)
            quality_label.setFont(QtGui.QFont("Helvetica", 14))
            quality_label.hide()
            self.quality_labels.append(quality_label)
            quality_label_geometry[0] += attribute_spacing

            self.rating_sliders.append(QtWidgets.QSlider(self.centralwidget))
            self.rating_sliders[idx].setGeometry(
                QtCore.QRect(slider_position[0], slider_position[1], self._rating_slider_zero_geometry[2],
                             self._rating_slider_zero_geometry[3]))
            self.rating_sliders[idx].setOrientation(QtCore.Qt.Vertical)
            self.rating_sliders[idx].setObjectName("verticalSlider")

            self.rating_sliders[idx].setTickPosition(QtWidgets.QSlider.TicksLeft)
            self.rating_sliders[idx].hide()

            # init set zero buttons
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setGeometry(QtCore.QRect(slider_position[0]+23, int(slider_position[1]+self._rating_slider_zero_geometry[3]/2) -10, 20, 20))
            btn.setObjectName("set_zero_btn")
            btn.setText("0")
            btn.hide()
            self.set_zero_btns.append(btn)

            slider_ticks = SliderTicks(slider_position[0]-5, slider_position[1], self.centralwidget)
            self.slider_ticks.append(slider_ticks)

            self.scale_end_labels_low.append(QtWidgets.QLabel(self.centralwidget))
            self.scale_end_labels_low[idx] = QtWidgets.QLabel(self.centralwidget)
            self.scale_end_labels_low[idx].setGeometry(
                QtCore.QRect(slider_position[0] - 26, self._scale_end_label_low_y_pos, 55, 20))
            self.scale_end_labels_low[idx].setObjectName("scale_end_label_low")
            self.scale_end_labels_low[idx].setWordWrap(True)
            self.scale_end_labels_low[idx].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.scale_end_labels_low[idx].hide()

            self.scale_end_labels_high.append(QtWidgets.QLabel(self.centralwidget))
            self.scale_end_labels_high[idx] = QtWidgets.QLabel(self.centralwidget)
            self.scale_end_labels_high[idx].setGeometry(
                QtCore.QRect(slider_position[0] - 26, self._scale_end_label_high_y_pos, 55, 20))
            self.scale_end_labels_high[idx].setObjectName("scale_end_label_high")
            self.scale_end_labels_high[idx].setWordWrap(True)
            self.scale_end_labels_high[idx].setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.scale_end_labels_high[idx].hide()

            line = QtWidgets.QFrame(self.centralwidget)
            line.setGeometry(QtCore.QRect(attribute_separator_gemoetry[0], attribute_separator_gemoetry[1],
                                          attribute_separator_gemoetry[2], attribute_separator_gemoetry[3]))
            line.setFrameShape(QtWidgets.QFrame.HLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            line.setObjectName("line")
            line.hide()
            line.setStyleSheet("background-color: none; border: 0.5px solid grey;")
            self.attribute_separator_lines.append(line)

            slider_position[0] += attribute_spacing
            attribute_separator_gemoetry[0] += attribute_spacing

        # draw footer
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(80, 768 - 90, 400, 51))
        self.title_label.setObjectName("title_label")
        self.title_label.raise_()

        line = QtWidgets.QFrame(self.centralwidget)
        line.setGeometry(QtCore.QRect(0, 768 - 90, 1024, 5))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        line.setStyleSheet("QLineEdit {background : lightblue;}")

        self.openGLWidget = QtSvg.QSvgWidget('SAQI/GUI/thk_logo_bw_transparent.svg', parent=self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(1024 - 130, 768 - 85, 120, 90))
        self.openGLWidget.setObjectName("openGLWidget")

        SAQI_main_gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(SAQI_main_gui, language)
        QtCore.QMetaObject.connectSlotsByName(SAQI_main_gui)

    def retranslateUi(self, SAQI_main_gui, language):
        _translate = QtCore.QCoreApplication.translate
        SAQI_main_gui.setWindowTitle(_translate("SAQI_main_gui", "SAQI Listening Experiment"))
        self.title_label.setText(_translate("SAQI_welcome_gui",
                                            "<html><head/><body><p><span style=\" font-family: Helvetica; font-size:22pt; font-weight:normal; color:#999999;\">SAQI - A Spatial Audio Quality Inventory </span></p></body></html>"))
        self.stimuli_A_btn.setText(_translate("SAQI_main_gui", "A"))
        self.stimuli_B_btn.setText(_translate("SAQI_main_gui", "B"))
        self._trial_cnt.setText(_translate("SAQI_main_gui", ""))

        if language == 'english':
            self.next_trial_btn.setText(_translate("SAQI_main_gui", "next"))
            self.category_title_label.setText(_translate("SAQI_main_gui", "Categories"))
            self.play_pause_btn.setText(_translate("SAQI_main_gui", "play"))

            self.diff_btn.setText(_translate("SAQI_main_gui", "Yes"))
            self.no_diff_btn.setText(_translate("SAQI_main_gui", "No"))
            for label in self.rate_b_labels:
                label.setText(_translate("SAQI_main_gui", "B is ..."))

        elif language == 'german':
            self.next_trial_btn.setText(_translate("SAQI_main_gui", "Weiter"))
            self.category_title_label.setText(_translate("SAQI_main_gui", "Kategorien"))
            self.play_pause_btn.setText(_translate("SAQI_main_gui", "Play"))

            self.diff_btn.setText(_translate("SAQI_main_gui", "Ja"))
            self.no_diff_btn.setText(_translate("SAQI_main_gui", "Nein"))
            for label in self.rate_b_labels:
                label.setText(_translate("SAQI_main_gui", "B ist ..."))

class TrackedLabel(QtWidgets.QLabel):
    is_under_mouse = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent)
        self.setMouseTracking(True)

    def enterEvent(self, event):
        self.is_under_mouse.emit(True)

    def leaveEvent(self, event):
        self.is_under_mouse.emit(False)


class SliderTicks():

    def __init__(self, x, y, centralwidget):
        self._x = x
        self._y = y
        self._width = 10
        self._height = 4 # tick height
        self._centralwidget = centralwidget
        self._ticks = list()
        self._labels = list()

    def draw(self, mode='bipolar', y=None, intervals=7, slider_height=245):
        if y is None:
            y = self._y
        y = y
        if mode == 'unipolar':
            spacing = slider_height / (intervals)
            label_cnt = intervals
            for i in range(0, intervals+1):
                tick = QtWidgets.QFrame(self._centralwidget)
                tick.setGeometry(QtCore.QRect(self._x, y,
                                      self._width, self._height))
                tick.setFrameShape(QtWidgets.QFrame.HLine)
                tick.setFrameShadow(QtWidgets.QFrame.Sunken)
                tick.show()

                label = QtWidgets.QLabel(self._centralwidget)
                label.setGeometry(QtCore.QRect(self._x - self._width - 4, y - 4,
                                               self._width, self._height))
                label.setText(f"{int(label_cnt)}")
                label.setStyleSheet("color: gray; font-size: 10pt")
                label.adjustSize()
                label.show()

                label_cnt = label_cnt - 1
                self._labels.append(label)
                y = y + spacing
                self._ticks.append(tick)

        elif mode == 'bipolar':
            spacing = slider_height / (intervals-1)
            label_cnt = np.floor(intervals/2)
            for i in range(0, intervals):
                tick = QtWidgets.QFrame(self._centralwidget)
                tick.setGeometry(QtCore.QRect(self._x, y,
                                      self._width, self._height))
                tick.setFrameShape(QtWidgets.QFrame.HLine)
                tick.setFrameShadow(QtWidgets.QFrame.Sunken)

                label = QtWidgets.QLabel(self._centralwidget)
                label.setGeometry(QtCore.QRect(self._x-self._width-4, y-4,
                                              self._width, self._height))

                label.setText(f"{int(label_cnt)}")
                label.setStyleSheet("color: gray; font-size: 10pt")
                label.adjustSize()

                label_cnt = label_cnt -1
                y = y + spacing
                self._ticks.append(tick)
                self._labels.append(label)

    def hide(self):
        for tick in self._ticks:
            tick.hide()

        for label in self._labels:
            label.hide()

    def show(self):
        for tick in self._ticks:
            tick.show()

        for label in self._labels:
            label.show()

        
