from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QComboBox, QPushButton

from process import isCamsOpen


class cameraDialog(QDialog):
    def __init__(self, cameranum):
        super().__init__()
        self.cameranum = cameranum
        self.dialog_setup()
        self.show()

    def dialog_setup(self):
        uic.loadUi('ui/cameradialog.ui', self)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))
        self.setWindowTitle('Camera{} Directions'.format(self.cameranum + 1))
        self.setFixedSize(260, 110)

        self.okbtn = self.findChild(QPushButton, 'okbtn')
        self.inbox = self.findChild(QComboBox, 'inBox')
        self.outbox = self.findChild(QComboBox, 'outBox')
        self.inbox.currentTextChanged.connect(self.inbox_update)
        self.outbox.currentTextChanged.connect(self.outbox_update)
        self.okbtn.clicked.connect(self.acceptdirection)

    def acceptdirection(self):
        direct = 'lr' if self.inbox.currentText() == 'Left' else 'rl'
        if self.cameranum == 0:
            isCamsOpen.camdirect = direct
        if self.cameranum == 1:
            isCamsOpen.camdirect1 = direct
        if self.cameranum == 2:
            isCamsOpen.camdirect2 = direct
        if self.cameranum == 3:
            isCamsOpen.camdirect3 = direct
        self.close()


    def inbox_update(self):
        textin = self.inbox.currentText()
        if textin == 'Left':
            self.outbox.setCurrentIndex(0)
        else:
            self.outbox.setCurrentIndex(1)

    def outbox_update(self):
        textout = self.outbox.currentText()
        if textout == 'Left':
            self.inbox.setCurrentIndex(1)
        else:
            self.inbox.setCurrentIndex(0)

    def closeEvent(self, event) -> None:
        direct = 'lr' if self.inbox.currentText() == 'Left' else 'rl'
        if self.cameranum == 0:
            isCamsOpen.camdirect = direct
        if self.cameranum == 1:
            isCamsOpen.camdirect1 = direct
        if self.cameranum == 2:
            isCamsOpen.camdirect2 = direct
        if self.cameranum == 3:
            isCamsOpen.camdirect3 = direct
        # print(direct)
        event.accept()


def callcameraDialog(cameranum):
    dialog = cameraDialog(cameranum)
    dialog.exec_()
