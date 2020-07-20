from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

from MainLayers.dialog_box import information_box
from database.initialdb import initialdb
from database.updateToFirebase import loop_update_firebase


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        uic.loadUi('ui/main.ui', self)
        self.setFixedSize(800, 600)
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setAutoFillBackground(True)

        self.ref = initialdb()
        loop_update_firebase()

        self.grid_layout()
        self.set_calendar()

        # initialize variables that will point to new window
        self.cam = None
        self.cam1 = None
        self.cam2 = None
        self.cam3 = None
        self.ipdialog = None
        self.ipdialog1 = None
        self.ipdialog2 = None
        self.ipdialog3 = None
        self.barchart = None

        self.show()

    # gray colour still means it is being used.
    from MainLayers.leftgrid import grid_layout, open_cam, enterip
    from MainLayers.rightlayout.historybtn import set_calendar, history_popup
    from MainLayers.dialog_box import information_box

    def closeEvent(self, event):
        # kill thread updater
        # close all cams
        if self.cam is not None:
            if self.cam.isVisible():
                self.cam.close()
        if self.cam1 is not None:
            if self.cam1.isVisible():
                self.cam1.close()
        if self.cam2 is not None:
            if self.cam2.isVisible():
                self.cam2.close()
        if self.cam3 is not None:
            if self.cam3.isVisible():
                self.cam3.close()
        # close all ipdialog and loading
        if self.ipdialog is not None:
            if self.ipdialog.ipdialog.isVisible():
                self.ipdialog.ipdialog.close()
            if self.ipdialog.loading is not None:
                if self.ipdialog.loading.isVisible():
                    self.ipdialog.loading.close()
        if self.ipdialog1 is not None:
            if self.ipdialog1.ipdialog.isVisible():
                self.ipdialog1.ipdialog.close()
            if self.ipdialog1.loading is not None:
                if self.ipdialog1.loading.isVisible():
                    self.ipdialog1.loading.close()
        if self.ipdialog2 is not None:
            if self.ipdialog2.ipdialog.isVisible():
                self.ipdialog2.ipdialog.close()
            if self.ipdialog2.loading is not None:
                if self.ipdialog2.loading.isVisible():
                    self.ipdialog2.loading.close()
        if self.ipdialog3 is not None:
            if self.ipdialog3.ipdialog.isVisible():
                self.ipdialog3.ipdialog.close()
            if self.ipdialog3.loading is not None:
                if self.ipdialog3.loading.isVisible():
                    self.ipdialog3.loading.close()
        # close barchart
        if self.barchart is not None:
            if self.barchart.isVisible():
                self.barchart.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())
