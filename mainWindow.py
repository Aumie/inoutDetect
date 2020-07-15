from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from database.initialdb import initialdb
from database.updateToFirebase import loop_update_firebase


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        uic.loadUi('ui/main.ui', self)
        self.setFixedSize(700, 600)
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setAutoFillBackground(True)

        self.ref = initialdb()
        loop_update_firebase()

        self.grid_layout()
        self.set_calendar()

        # initialize variables that will point to new window
        self.cam = None
        self.ipdialog = None
        self.loading = None
        # flag for ip box
        self.isValidIp = False
        self.isTestIpDone = False
        self.ipBoxFlag = False
        self.show()

    # gray colour still means it is being used.
    from MainLayers.ipChecker import ipChecker, update_isTestIpDone, update_isValidIp
    from MainLayers.leftgrid import grid_layout, open_cam, enterip, accept_ip
    from MainLayers.rightlayout.historybtn import set_calendar, history_popup
    from MainLayers.dialog_box import information_box

    def closeEvent(self, event):
        if self.cam is not None:
            if self.cam.isVisible():
                self.cam.close()
        if self.ipdialog is not None:
            if self.ipdialog.isVisible():
                self.ipdialog.close()
        if self.loading is not None:
            if self.loading.isVisible():
                self.loading.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
