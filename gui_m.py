# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pi_image.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 796)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(True)
        MainWindow.setStyleSheet("background-color:  #4AAAA5;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.softwareName = QtWidgets.QLabel(self.centralwidget)
        self.softwareName.setGeometry(QtCore.QRect(380, 10, 361, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.softwareName.setFont(font)
        self.softwareName.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.softwareName.setStyleSheet("font: 48pt \"Times New Roman\";\n"
"color:  #0C3B40;\n"
"background-color: #4AAAA5;\n"
"")
        self.softwareName.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.softwareName.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.softwareName.setObjectName("softwareName")
        self.mainPage = QtWidgets.QTabWidget(self.centralwidget)
        self.mainPage.setEnabled(True)
        self.mainPage.setGeometry(QtCore.QRect(-10, 60, 1101, 741))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mainPage.setFont(font)
        self.mainPage.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainPage.setToolTipDuration(-1)
        self.mainPage.setAutoFillBackground(False)
        self.mainPage.setStyleSheet("color:   #3A4055;\n"
"font: 75 18pt \"Times New Roman\";\n"
"background-color:  #4AAAA5;\n"
"")
        self.mainPage.setTabPosition(QtWidgets.QTabWidget.North)
        self.mainPage.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.mainPage.setIconSize(QtCore.QSize(40, 40))
        self.mainPage.setElideMode(QtCore.Qt.ElideNone)
        self.mainPage.setObjectName("mainPage")
        self.tab_control = QtWidgets.QWidget()
        self.tab_control.setObjectName("tab_control")
        self.start = QtWidgets.QPushButton(self.tab_control)
        self.start.setGeometry(QtCore.QRect(0, 0, 221, 61))
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.start.setStyleSheet("background-color:#41D4CF;\n"
"color: #0C5E3E;\n"
"font: 75 18pt \"Times New Roman\";")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(self.tab_control)
        self.stop.setGeometry(QtCore.QRect(0, 70, 221, 51))
        self.stop.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.stop.setStyleSheet("background-color:#41D4CF;\n"
"color: #D60000;\n"
"font: 75 14pt \"Times New Roman\";")
        self.stop.setObjectName("stop")
        self.forched_stop = QtWidgets.QPushButton(self.tab_control)
        self.forched_stop.setGeometry(QtCore.QRect(0, 580, 221, 51))
        self.forched_stop.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.forched_stop.setStyleSheet("background-color:#41D4CF;\n"
"color: #D60000;\n"
"font: 75 14pt \"Times New Roman\";")
        self.forched_stop.setObjectName("forched_stop")
        self.exit = QtWidgets.QPushButton(self.tab_control)
        self.exit.setGeometry(QtCore.QRect(0, 640, 221, 61))
        self.exit.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.exit.setStyleSheet("background-color:#41D4CF;\n"
"color:  #D60000;\n"
"font: 75 18pt \"Times New Roman\";")
        self.exit.setObjectName("exit")
        self.uploadPva = QtWidgets.QPushButton(self.tab_control)
        self.uploadPva.setGeometry(QtCore.QRect(0, 470, 221, 51))
        self.uploadPva.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.uploadPva.setAcceptDrops(True)
        self.uploadPva.setStyleSheet("background-color:#41D4CF;\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: #000000;")
        self.uploadPva.setObjectName("uploadPva")
        self.uploadMessage = QtWidgets.QPushButton(self.tab_control)
        self.uploadMessage.setGeometry(QtCore.QRect(0, 410, 221, 51))
        self.uploadMessage.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.uploadMessage.setAcceptDrops(True)
        self.uploadMessage.setStyleSheet("background-color:#41D4CF;\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: #000000;")
        self.uploadMessage.setAutoDefault(False)
        self.uploadMessage.setDefault(False)
        self.uploadMessage.setFlat(False)
        self.uploadMessage.setObjectName("uploadMessage")
        self.monitor = QtWidgets.QTextBrowser(self.tab_control)
        self.monitor.setGeometry(QtCore.QRect(220, 0, 881, 711))
        self.monitor.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.monitor.setMouseTracking(True)
        self.monitor.setAcceptDrops(False)
        self.monitor.setToolTip("")
        self.monitor.setToolTipDuration(5)
        self.monitor.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.monitor.setAutoFillBackground(True)
        self.monitor.setStyleSheet("color: #41CD52;\n"
"font: 8pt \"Times New Roman\";\n"
"background-color:#B2FEFE;")
        self.monitor.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.monitor.setDocumentTitle("")
        self.monitor.setObjectName("monitor")
        self.activityType = QtWidgets.QGroupBox(self.tab_control)
        self.activityType.setGeometry(QtCore.QRect(8, 290, 210, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.activityType.setFont(font)
        self.activityType.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.activityType.setStyleSheet("background-color:#41D4CF;\n"
"font: 75 11pt \"Times New Roman\";\n"
"color: #000000;")
        self.activityType.setTitle("")
        self.activityType.setObjectName("activityType")
        self.activityPartners = QtWidgets.QRadioButton(self.activityType)
        self.activityPartners.setGeometry(QtCore.QRect(10, 0, 171, 41))
        self.activityPartners.setMaximumSize(QtCore.QSize(171, 16777215))
        self.activityPartners.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.activityPartners.setStyleSheet("color: #000000;")
        self.activityPartners.setChecked(True)
        self.activityPartners.setObjectName("activityPartners")
        self.radioButton = QtWidgets.QRadioButton(self.activityType)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 191, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.radioButton.setFont(font)
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton.setStyleSheet("color: #000000;")
        self.radioButton.setObjectName("radioButton")
        self.browsers = QtWidgets.QGroupBox(self.tab_control)
        self.browsers.setGeometry(QtCore.QRect(8, 140, 211, 141))
        self.browsers.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browsers.setStatusTip("")
        self.browsers.setWhatsThis("")
        self.browsers.setStyleSheet("background-color:#41D4CF;\n"
"font: 75 12pt \"Times New Roman\";\n"
"color: #000000;")
        self.browsers.setTitle("")
        self.browsers.setCheckable(False)
        self.browsers.setObjectName("browsers")
        self.googleChrome = QtWidgets.QRadioButton(self.browsers)
        self.googleChrome.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.googleChrome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.googleChrome.setStyleSheet("color: #000000;")
        self.googleChrome.setChecked(True)
        self.googleChrome.setObjectName("googleChrome")
        self.edge = QtWidgets.QRadioButton(self.browsers)
        self.edge.setGeometry(QtCore.QRect(10, 50, 71, 20))
        self.edge.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edge.setStyleSheet("color: #000000;")
        self.edge.setObjectName("edge")
        self.firefox = QtWidgets.QRadioButton(self.browsers)
        self.firefox.setGeometry(QtCore.QRect(10, 80, 95, 20))
        self.firefox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firefox.setStyleSheet("color: #000000;")
        self.firefox.setObjectName("firefox")
        self.hideBrowser = QtWidgets.QRadioButton(self.browsers)
        self.hideBrowser.setGeometry(QtCore.QRect(10, 110, 61, 20))
        self.hideBrowser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hideBrowser.setStyleSheet("color: #000000;")
        self.hideBrowser.setObjectName("hideBrowser")
        self.mainPage.addTab(self.tab_control, "")
        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainPage.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ehut LTD."))
        self.softwareName.setText(_translate("MainWindow", "Ehut LTD."))
        self.start.setText(_translate("MainWindow", "start"))
        self.stop.setText(_translate("MainWindow", "stop"))
        self.forched_stop.setText(_translate("MainWindow", "Forced Stop"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.uploadPva.setText(_translate("MainWindow", "Upload PVA"))
        self.uploadMessage.setText(_translate("MainWindow", "Upload Message"))
        self.activityPartners.setText(_translate("MainWindow", "Activity-Partners"))
        self.radioButton.setText(_translate("MainWindow", "Missed-Connections"))
        self.googleChrome.setText(_translate("MainWindow", "Google Chrome"))
        self.edge.setText(_translate("MainWindow", "Edge"))
        self.firefox.setText(_translate("MainWindow", "Firefox"))
        self.hideBrowser.setText(_translate("MainWindow", "Hide"))
        self.mainPage.setTabText(self.mainPage.indexOf(self.tab_control), _translate("MainWindow", "Main Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
