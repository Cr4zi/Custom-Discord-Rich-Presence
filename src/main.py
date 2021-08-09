from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from mainwindow import Ui_MainWindow
from pypresence import Presence


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setToolTip(f'Discord Custom Rich Presence')
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ConnectButton.clicked.connect(self.connect)
        self.ui.DisconnectButton.clicked.connect(self.disconnect)
        self.rpc = None

    def get_id(self):
        return str(self.ui.ID_textInput.toPlainText())
    
    def get_details(self):
        return str(self.ui.Details_textInput.toPlainText())
        
    def get_state(self):
        return str(self.ui.State_textInput.toPlainText())

    def get_large_key(self):
        return str(self.ui.keylarge_input.toPlainText())

    def get_large_text(self):
        return str(self.ui.Textlarge_input.toPlainText())

    def get_small_key(self):
        return str(self.ui.keylarge_input.toPlainText())
    
    def get_small_text(self):
        return str(self.ui.Textsmall_input.toPlainText())

    def get_buttonone_text(self):
        return str(self.ui.Textone_input.toPlainText())

    def get_buttonone_url(self):
        return str(self.ui.Urlone_input.toPlainText())

    def get_buttontwo_text(self):
        return str(self.ui.Texttwo_input.toPlainText())
    
    def get_buttontwo_url(self):
        return str(self.ui.Urltwo_input.toPlainText())

    def connect(self):
        self.id = self.get_id()
        self.details = self.get_details()
        self.state = self.get_state()
        self.LargeKey = self.get_large_key()
        self.largeText = self.get_large_text()
        self.SmallKey = self.get_small_key()
        self.SmallText = self.get_small_text()
        self.Button1Text = self.get_buttonone_text()
        self.Button1Url = self.get_buttonone_url()
        self.Button2Text = self.get_buttontwo_text()
        self.Button2Url = self.get_buttontwo_url()
        self.ui.DisconnectButton.setStyleSheet(u"background-color: lightGray; font: 22pt \"Segoe UI\";")
        self.ui.ConnectButton.setStyleSheet(u"background-color: white; font: 22pt \"Segoe UI\";")
        self.rpc = Presence(self.id)
        self.rpc.connect()

    def disconnect(self):
        if self.rpc is not None:
            self.rpc.close()
            self.ui.DisconnectButton.setStyleSheet(u"background-color: white; font: 22pt \"Segoe UI\";")
            self.ui.ConnectButton.setStyleSheet(u"background-color: lightGray; font: 22pt \"Segoe UI\";")
        else:
            return

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()