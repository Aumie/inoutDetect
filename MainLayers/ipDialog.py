from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton


class ipDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.dialog_setup()
        self.show()

    def dialog_setup(self):
        uic.loadUi('ui/ipdialog.ui', self)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))
        self.setFixedSize(330, 180)
        self.camipinput = self.findChild(QLineEdit, 'camipinput')
        self.idinput = self.findChild(QLineEdit, 'idinput')
        self.pwdinput = self.findChild(QLineEdit, 'pwdinput')
        self.okbtn = self.findChild(QPushButton, 'okbtn')
