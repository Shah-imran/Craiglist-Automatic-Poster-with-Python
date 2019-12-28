from gui_m import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import os
import var 
import threading
import sel

class MyGui(Ui_MainWindow, QtWidgets.QWidget):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(dialog)


class myMainClass():
    def __init__(self):

        GUI.start.clicked.connect(self.startPosting)
        GUI.stop.clicked.connect(self.stop)
        GUI.uploadMessage.clicked.connect(self.uploadMessage)
        GUI.uploadPva.clicked.connect(self.uploadPva)
        GUI.forched_stop.clicked.connect(self.pause)
        GUI.exit.clicked.connect(self.exit)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.monitor)
        self.timer.start(1000)

    def monitor(self):
        cursor = GUI.monitor.textCursor()
        while not var.monitorQ.empty():
            data = var.monitorQ.get()
            # cursor.insertHtml('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("started"))
            # cursor.insertHtml('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span>'''.format("started"))
            cursor.insertHtml(data)

    def startPosting(self):
        print("start button clicked")
        if var.pause == True:
            var.pause = False
            GUI.start.setEnabled(False)
            var.monitorQ.put('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span><br>'''.format("Resumed..."))
        else:
            GUI.start.setEnabled(False)
            self.radioButtonCheck()
            var.monitorQ.put('''<p><span style="color: #0C5E3E; font-size: 30px;">{} </span><br>'''.format("Starting-"))
            threading.Thread(target=sel.main, args=[GUI, ], daemon=True).start()

    def radioButtonCheck(self):
        if GUI.activityPartners.isChecked():
            var.typeSelect = "activity"
        else:
            var.typeSelect = "missedCon"

        if GUI.firefox.isChecked():
            var.browserSelect = "firefox"
        else:
            var.browserSelect = "Chrome"

    def stop(self):
        print("stop button clicked")
        var.terminate = True
        var.monitorQ.put('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("Process Terminated"))

    def uploadMessage(self):
        print("upload message")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        messagePath, _ = QFileDialog.getOpenFileName(None,"Select file", "","Excel Files (*.xlsx)", options=options)
        if messagePath:
            var.messagePath = messagePath
        else:
            pass

    def uploadPva(self):
        print("uploadPva")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        pvaPath, _ = QFileDialog.getOpenFileName(None,"Select file", "","Excel Files (*.xlsx)", options=options)
        if pvaPath:
            var.pvaPath = pvaPath
        else:
            pass

    def pause(self):
        print("forched stop")
        GUI.start.setEnabled(True)
        var.pause = True
        var.monitorQ.put('''<p><span style="color: #D60000; font-size: 30px;">{} </span><br>'''.format("Paused (press start to resume)"))

    def exit(self):
        print("exit")
        sys.exit()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    try:
        def resource_path(relative_path):
            if hasattr(sys, '_MEIPASS'):
                return os.path.join(sys._MEIPASS, relative_path)
            return os.path.join(os.path.abspath("."), relative_path)

        p = resource_path('favicon.ico')
        dialog.setWindowIcon(QtGui.QIcon(p))
    except Exception as e:
        print(e)
        pass

    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowMinimizeButtonHint |
                          QtCore.Qt.WindowSystemMenuHint)
    dialog.setWindowFlags(dialog.windowFlags() |
                          QtCore.Qt.WindowSystemMenuHint |
                          QtCore.Qt.WindowMinMaxButtonsHint)

    GUI = MyGui(dialog)
    dialog.show()

    myMC = myMainClass()

    app.exec_()
    print("Exit")
    sys.exit()