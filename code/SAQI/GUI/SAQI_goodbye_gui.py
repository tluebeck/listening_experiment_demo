# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Ui_SAQI_goodbye_gui(object):
    def setupUi(self, SAQI_goodbye_gui, language='english'):
        """
        Listening Experiment Py: SAQI - A Spatial Audio Inventory

        (C) 2021 by Tim Lübeck
                TH Köln - University of Applied Sciences
                Institute of Communications Engineering
                Department of Acoustics and Audio Signal Processing

        Parameters
        ----------
        SAQI_goodbye_gui
        """
        SAQI_goodbye_gui.setObjectName("SAQUI_goodbye_gui")
        SAQI_goodbye_gui.resize(1024, 768)

        self.centralwidget = QtWidgets.QWidget(SAQI_goodbye_gui)
        self.centralwidget.setObjectName("centralwidget")

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(80, 768-90, 400, 51))
        self.title_label.setObjectName("title_label")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 200, 491, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.raise_()

        self.task_label = QtWidgets.QLabel(self.centralwidget)
        self.task_label.setGeometry(QtCore.QRect(350, 280, 521, 91))
        self.task_label.setObjectName("task_label")
        self.finish_btn = QtWidgets.QPushButton(self.centralwidget)
        self.finish_btn.setGeometry(QtCore.QRect(440, 350, 113, 32))
        self.finish_btn.setObjectName("start_btn")

        line = QtWidgets.QFrame(self.centralwidget)
        line.setGeometry(QtCore.QRect(0, 768 - 90, 1024, 5))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName("line")
        line.setStyleSheet("QLineEdit {background : lightblue;}")

        self.openGLWidget = QtSvg.QSvgWidget('GUI/thk_logo_bw_transparent.svg', parent=self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(1024 - 130, 768 - 85, 120, 90))
        self.openGLWidget.setObjectName("openGLWidget")

        SAQI_goodbye_gui.setCentralWidget(self.centralwidget)
        self.retranslateUi(SAQI_goodbye_gui, language)
        QtCore.QMetaObject.connectSlotsByName(SAQI_goodbye_gui)

    def retranslateUi(self, SAQI_goodbye_gui, language):
        _translate = QtCore.QCoreApplication.translate
        SAQI_goodbye_gui.setWindowTitle(_translate("SAQUI_goodbye_gui", "SAQUI_main_gui"))
        self.title_label.setText(_translate("SAQI_welcome_gui",
                                            "<html><head/><body><p><span style=\" font-family: Helvetica; font-size:22pt; font-weight:normal; color:#999999;\">SAQI - A Spatial Audio Quality Inventory </span></p></body></html>"))
        if language == 'english':
            self.task_label.setText(_translate("SAQUI_goodbye_gui", "<html><head/><body><p align=\"justify\">Thank you for participating. Please close the app.</p></body></html>"))
            self.finish_btn.setText(_translate("SAQUI_goodbye_gui", "finish"))
        elif language == 'german':
            self.task_label.setText(_translate("SAQUI_goodbye_gui",
                                               "<html><head/><body><p align=\"justify\">Danke für die Teilnahme. Bitte schließe die App.</p></body></html>"))
            self.finish_btn.setText(_translate("SAQUI_goodbye_gui", "ende"))
