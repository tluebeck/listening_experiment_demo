    # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mushra_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mushra(object):
    def setupUi(self, Mushra, num_stimuli_per_page, num_trails):
        Mushra.setObjectName("Mushra")
        slider_horizontal_spacing = 110
        width = num_stimuli_per_page*slider_horizontal_spacing+210
        Mushra.resize(width, 476)


        self.centralwidget = QtWidgets.QWidget(Mushra)
        self.centralwidget.setObjectName("centralwidget")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(width-250, 430, 68, 32))
        self.play_button.setObjectName("play_button")
        self.major_line = QtWidgets.QFrame(self.centralwidget)
        self.major_line.setGeometry(QtCore.QRect(20, 50, 1011, 10))
        self.major_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.major_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.major_line.setObjectName("major_line")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(60, 20, 701, 20))
        self.title.setObjectName("title")
        self.next_trial_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_trial_btn.setGeometry(QtCore.QRect(width-150, 430, 111, 32))
        self.next_trial_btn.setObjectName("next_trial_btn")

        self.Ref_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Ref_btn.setGeometry(QtCore.QRect(20, 100, 107, 32))
        self.Ref_btn.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Ref_btn.setObjectName("Ref_btn")

        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 95, 881, 32))
        self.layoutWidget1.setObjectName("layoutWidget1")

        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 140, 133, 281))
        self.layoutWidget.setObjectName("layoutWidget")

        self.sliders = []
        self.btns = []


        for idx in range(num_stimuli_per_page):
            # create slider
            horizontal_pos = 210 + (idx * slider_horizontal_spacing)
            slider = QtWidgets.QSlider(self.centralwidget)
            slider.setGeometry(QtCore.QRect(horizontal_pos, 150, 20, 250))
            slider.setOrientation(QtCore.Qt.Vertical)
            slider.setInvertedAppearance(True)
            slider.setInvertedControls(True)
            slider.setTickPosition(QtWidgets.QSlider.NoTicks)
            slider.setTickInterval(21)
            slider.setObjectName("A_slider")
            slider.raise_()
            self.sliders.append(slider)

            # create ticks
            no_tick = QtWidgets.QFrame(self.centralwidget)
            no_tick.setGeometry(QtCore.QRect(horizontal_pos-10, 160, 10, 5))
            no_tick.setFrameShape(QtWidgets.QFrame.HLine)
            no_tick.setFrameShadow(QtWidgets.QFrame.Sunken)
            no_tick.setObjectName("excelent_line")
            no_tick.raise_()

            small_tick = QtWidgets.QFrame(self.centralwidget)
            small_tick.setGeometry(QtCore.QRect(horizontal_pos-10, 218, 10, 5))
            small_tick.setFrameShape(QtWidgets.QFrame.HLine)
            small_tick.setFrameShadow(QtWidgets.QFrame.Sunken)
            small_tick.setObjectName("good_line")
            small_tick.raise_()

            moderate_tick = QtWidgets.QFrame(self.centralwidget)
            moderate_tick.setGeometry(QtCore.QRect(horizontal_pos-10, 276, 10, 5))
            moderate_tick.setFrameShape(QtWidgets.QFrame.HLine)
            moderate_tick.setFrameShadow(QtWidgets.QFrame.Sunken)
            moderate_tick.setObjectName("fair_line")
            moderate_tick.raise_()

            significant_tick = QtWidgets.QFrame(self.centralwidget)
            significant_tick.setGeometry(QtCore.QRect(horizontal_pos-10, 334, 10, 5))
            significant_tick.setFrameShape(QtWidgets.QFrame.HLine)
            significant_tick.setFrameShadow(QtWidgets.QFrame.Sunken)
            significant_tick.setObjectName("poor_line")
            significant_tick.raise_()

            huge_tick = QtWidgets.QFrame(self.centralwidget)
            huge_tick.setGeometry(QtCore.QRect(horizontal_pos-10, 395, 10, 5))
            huge_tick.setFrameShape(QtWidgets.QFrame.HLine)
            huge_tick.setFrameShadow(QtWidgets.QFrame.Sunken)
            huge_tick.setObjectName("bad_line")
            huge_tick.raise_()

            # create button
            btn = QtWidgets.QPushButton(self.centralwidget)
            btn.setFocusPolicy(QtCore.Qt.ClickFocus)
            btn.setObjectName("A_btn")
            btn.setText(chr(ord('@')+idx+1))
            btn.setGeometry(QtCore.QRect(175 + (idx * slider_horizontal_spacing), 100, 90, 32))
            self.btns.append(btn)
            #self.gridLayout.addWidget(btn, 0, idx, 1, 1)

        # create slider labels
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.excelent_label = QtWidgets.QLabel(self.layoutWidget)
        self.excelent_label.setObjectName("excelent_label")
        self.verticalLayout.addWidget(self.excelent_label)
        self.small_label = QtWidgets.QLabel(self.layoutWidget)
        self.small_label.setObjectName("slieder_label_3")
        self.verticalLayout.addWidget(self.small_label)
        self.fair_label = QtWidgets.QLabel(self.layoutWidget)
        self.fair_label.setObjectName("fair_label")
        self.verticalLayout.addWidget(self.fair_label)
        self.poor_label = QtWidgets.QLabel(self.layoutWidget)
        self.poor_label.setObjectName("poor_label")
        self.verticalLayout.addWidget(self.poor_label)
        self.bad_label = QtWidgets.QLabel(self.layoutWidget)
        self.bad_label.setObjectName("bad_label")
        self.verticalLayout.addWidget(self.bad_label)

        self.reconnect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.reconnect_btn.setGeometry(QtCore.QRect(20, 430, 91, 32))
        self.reconnect_btn.setObjectName("reconnect_btn")

        self.trail_count_label = QtWidgets.QLabel(self.centralwidget)
        self.trail_count_label.setGeometry(QtCore.QRect(width - 100, 20, 101, 20))
        self.trail_count_label.setObjectName("label")
        self.trail_count_label.setText("Trial out of {}".format(num_trails))

        self.play_button.raise_()
        self.major_line.raise_()
        self.title.raise_()
        self.next_trial_btn.raise_()

        self.layoutWidget.raise_()

        self.layoutWidget.raise_()


        self.reconnect_btn.raise_()
        self.trail_count_label.raise_()
        Mushra.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mushra)
        QtCore.QMetaObject.connectSlotsByName(Mushra)

    def retranslateUi(self, Mushra):
        _translate = QtCore.QCoreApplication.translate
        Mushra.setWindowTitle(_translate("Mushra", "Listen Experiment"))
        self.play_button.setText(_translate("Mushra", "Play"))
        self.title.setText(_translate("Mushra", "Please rate the similarity of each sample related to the reference"))
        self.next_trial_btn.setText(_translate("Mushra", "Next Trial"))
        self.Ref_btn.setText(_translate("Mushra", "Reference"))
        self.excelent_label.setText(_translate("Mushra", "No difference"))
        self.small_label.setText(_translate("Mushra", "Small difference"))
        self.fair_label.setText(_translate("Mushra", "Moderate difference"))
        self.poor_label.setText(_translate("Mushra", "Significant difference"))
        self.bad_label.setText(_translate("Mushra", "Huge difference"))

        self.reconnect_btn.setText(_translate("Mushra", "reconnect"))


