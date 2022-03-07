# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Ui_SAQI_welcome_gui(object):
    def setupUi(self, SAQI_welcome_gui, language='english'):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        SAQI_welcome_gui
        language
        """
        SAQI_welcome_gui.setObjectName("SAQI_welcome_gui")
        SAQI_welcome_gui.resize(1024, 768)  # IPad 1.gen display dimensions 1024 x 768

        self.centralwidget = QtWidgets.QWidget(SAQI_welcome_gui)
        self.centralwidget.setObjectName("centralwidget")

        self.task_label = QtWidgets.QLabel(self.centralwidget)
        self.task_label.setGeometry(QtCore.QRect(50, 80, 521, 91))
        self.task_label.setObjectName("task_label")

        self.age_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.age_combobox.setGeometry(QtCore.QRect(180, 260, 91, 32))
        self.age_combobox.setObjectName("age_combobox")
        self.age_label = QtWidgets.QLabel(self.centralwidget)
        self.age_label.setGeometry(QtCore.QRect(70, 270, 75, 16))
        self.age_label.setObjectName("age_label")

        self.gender_label = QtWidgets.QLabel(self.centralwidget)
        self.gender_label.setGeometry(QtCore.QRect(70, 230, 75, 16))
        self.gender_label.setObjectName("gender_label")
        self.gender_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.gender_combobox.setGeometry(QtCore.QRect(180, 220, 91, 32))
        self.gender_combobox.setObjectName("gender_combobox")
        self.gender_combobox.addItem("")
        self.gender_combobox.addItem("")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 200, 491, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.LE_exp_label = QtWidgets.QLabel(self.frame)
        self.LE_exp_label.setGeometry(QtCore.QRect(20, 100, 341, 51))
        self.LE_exp_label.setObjectName("LE_exp_label")
        self.LE_exp_combobox = QtWidgets.QComboBox(self.frame)
        self.LE_exp_combobox.setGeometry(QtCore.QRect(380, 100, 91, 32))
        self.LE_exp_combobox.setObjectName("LE_exp_combobox")
        self.LE_exp_combobox.addItem("")
        self.LE_exp_combobox.addItem("")
        self.LE_exp_combobox.addItem("")
        self.LE_exp_combobox.addItem("")


        self.BinTech_exp_label = QtWidgets.QLabel(self.frame)
        self.BinTech_exp_label.setGeometry(QtCore.QRect(20, 185, 341, 21))
        self.BinTech_exp_label.setObjectName("BinTech_exp_label")
        self.BinTech_exp_combobox = QtWidgets.QComboBox(self.frame)
        self.BinTech_exp_combobox.setGeometry(QtCore.QRect(380, 185, 91, 32))
        self.BinTech_exp_combobox.setObjectName("BinTech_exp_combobox")
        self.BinTech_exp_combobox.addItem("")
        self.BinTech_exp_combobox.addItem("")


        self.calibrate_btn = QtWidgets.QPushButton(self.centralwidget)
        self.calibrate_btn.setGeometry(QtCore.QRect(130, 460, 113, 32))
        self.calibrate_btn.setObjectName("calibrate_btn")
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(330, 460, 113, 32))
        self.start_btn.setObjectName("start_btn")

        self.frame.raise_()
        self.task_label.raise_()
        self.start_btn.raise_()
        self.age_combobox.raise_()
        self.age_label.raise_()
        self.gender_label.raise_()
        self.gender_combobox.raise_()
        self.calibrate_btn.raise_()

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(80, 768-90, 400, 51))
        self.title_label.setObjectName("title_label")
        self.title_label.raise_()

        line = QtWidgets.QFrame(self.centralwidget)
        line.setGeometry(QtCore.QRect(0, 768-90, 1024, 5))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        line.setStyleSheet("QLineEdit {background : lightblue;}")

        self.openGLWidget = QtSvg.QSvgWidget('GUI/thk_logo_bw_transparent.svg', parent=self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(1024-130, 768-85, 120, 90))
        self.openGLWidget.setObjectName("openGLWidget")

        SAQI_welcome_gui.setCentralWidget(self.centralwidget)
        self.retranslateUi(SAQI_welcome_gui, language)
        QtCore.QMetaObject.connectSlotsByName(SAQI_welcome_gui)

    def retranslateUi(self, SAQI_welcome_gui, language):
        _translate = QtCore.QCoreApplication.translate
        SAQI_welcome_gui.setWindowTitle(_translate("SAQI_welcome_gui", "SAQI Listening Experiment"))
        self.title_label.setText(_translate("SAQI_welcome_gui",
                                            "<html><head/><body><p><span style=\" font-family: Helvetica; font-size:22pt; font-weight:normal; color:#999999;\">SAQI - A Spatial Audio Quality Inventory </span></p></body></html>"))
        self.task_label.setText(_translate("SAQI_welcome_gui",
                                           "<html><head/><body><p align=\"justify\">Welcome to our SAQI Listening Experiment. </p><p align=\"justify\">Please provide us some information about yourselfe and click start </p><p align=\"justify\">to start the experiment.</p></body></html>"))
        if language == 'english':
            self.start_btn.setText(_translate("SAQI_welcome_gui", "start"))
            self.age_label.setText(_translate("SAQI_welcome_gui", "age"))
            self.gender_label.setText(_translate("SAQI_welcome_gui", "gender"))
            self.gender_combobox.setItemText(0, _translate("SAQI_welcome_gui", "female"))
            self.gender_combobox.setItemText(1, _translate("SAQI_welcome_gui", "male"))
            for age in range(1, 99):
                self.age_combobox.addItem(f"{age}")
            self.LE_exp_combobox.setItemText(0, _translate("SAQI_welcome_gui", "no"))
            self.LE_exp_combobox.setItemText(1, _translate("SAQI_welcome_gui", "<3"))
            self.LE_exp_combobox.setItemText(2, _translate("SAQI_welcome_gui", "3-5"))
            self.LE_exp_combobox.setItemText(3, _translate("SAQI_welcome_gui", ">5"))
            self.BinTech_exp_label.setText(
                _translate("SAQI_welcome_gui", "Do you have experince with binaural technology?"))
            self.BinTech_exp_combobox.setItemText(0, _translate("SAQI_welcome_gui", "yes"))
            self.BinTech_exp_combobox.setItemText(1, _translate("SAQI_welcome_gui", "no"))
            self.LE_exp_label.setText(_translate("SAQI_welcome_gui",
                                                 "<html><head/><body><p>Did you already participated in a listening experiments </p><p>and if in how many?</p></body></html>"))
            self.calibrate_btn.setText(_translate("SAQI_welcome_gui", "calibrate"))

        elif language == 'german':
            self.start_btn.setText(_translate("SAQI_welcome_gui", "Start"))
            self.age_label.setText(_translate("SAQI_welcome_gui", "Alter"))
            self.gender_label.setText(_translate("SAQI_welcome_gui", "Geschlecht"))
            self.gender_combobox.setItemText(0, _translate("SAQI_welcome_gui", "weiblich"))
            self.gender_combobox.setItemText(1, _translate("SAQI_welcome_gui", "männlich"))
            for age in range(1, 99):
                self.age_combobox.addItem(f"{age}")
            self.LE_exp_combobox.setItemText(0, _translate("SAQI_welcome_gui", "Nein"))
            self.LE_exp_combobox.setItemText(1, _translate("SAQI_welcome_gui", "<3"))
            self.LE_exp_combobox.setItemText(2, _translate("SAQI_welcome_gui", "3-5"))
            self.LE_exp_combobox.setItemText(3, _translate("SAQI_welcome_gui", ">5"))
            self.BinTech_exp_label.setText(
                _translate("SAQI_welcome_gui", "Haben Sie Erfahrung mit Binaural Synthese?"))
            self.BinTech_exp_combobox.setItemText(0, _translate("SAQI_welcome_gui", "Ja"))
            self.BinTech_exp_combobox.setItemText(1, _translate("SAQI_welcome_gui", "Nein"))
            self.LE_exp_label.setText(_translate("SAQI_welcome_gui",
                                                 "<html><head/><body><p>Haben Sie bereits an einem Hörversuch teilgenommen </p><p>und wenn ja an wie vielen?</p></body></html>"))
            self.calibrate_btn.setText(_translate("SAQI_welcome_gui", "Kalibrieren"))

