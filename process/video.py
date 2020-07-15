from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
import gc

from MainLayers.dialog_box import information_box
from process import isCamsOpen


class Camera(QMainWindow):
    def __init__(self):
        super(Camera, self).__init__()
        uic.loadUi('ui/prototype.ui', self)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))

        # set up layouts
        self.set_time()
        self.set_monitor()
        self.set_inoutlcds()
        self.set_totallcd()

        # thread Flag
        self.isThreadInitialized = False

        self.thread.isInitialized.connect(self.isThreadDone_update)




    from Cameras_Layers.vboxright.timedisplay import set_time
    from Cameras_Layers.vboxright.totallcd import set_totallcd
    from Cameras_Layers.vboxmid.monitor import set_monitor, update_image, convert_cv_qt
    from Cameras_Layers.vboxleft.inoutlcd import set_inoutlcds, update_lcdin, update_lcdout

    @pyqtSlot(bool)
    def isThreadDone_update(self, val):
        self.isThreadInitialized = val
        print(self.isThreadInitialized)

    def closeEvent(self, event):
        if not self.isThreadInitialized:
            event.ignore()
            return information_box('Thread is initializing, please wait', 0)

        # kill timer
        self.timer_in.stop()
        del self.timer_in
        self.timer_out.stop()
        del self.timer_out
        self.totaltimer.stop()
        del self.totaltimer

        # kill thread
        self.thread.stopwhile()
        del self.thread
        isCamsOpen.iscamopen = False
        # Does this deallocate memory??? I don't know but it looks good.
        gc.collect()
        event.accept()


