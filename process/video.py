from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel
import gc

from MainLayers.dialog_box import information_box
from process import isCamsOpen


class Camera(QMainWindow):
    def __init__(self, cameranum):
        super(Camera, self).__init__()

        self.cameranum = cameranum

        uic.loadUi('ui/prototype.ui', self)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))
        self.setWindowTitle('Camera{} Streamer'.format(cameranum + 1))
        self.setFixedSize(1280, 800)
        self.monitorlbl = self.findChild(QLabel, 'monitorlbl')
        self.monitorlbl.setText('camera{}'.format(cameranum + 1))
        self.monitorlbl.setFont(QFont("Helvetica [Cronyx]", 15))

        # set up layouts
        self.set_time()
        self.set_monitor()
        self.set_inoutlcds()
        self.set_totallcd()
        self.set_spinBox()

        # thread Flag
        self.isThreadInitialized = False

        self.thread.isInitialized.connect(self.isThreadDone_update)

    from Cameras_Layers.vboxright.timedisplay import set_time
    from Cameras_Layers.vboxright.totallcd import set_totallcd
    from Cameras_Layers.vboxmid.monitor import set_monitor, update_image, convert_cv_qt
    from Cameras_Layers.vboxleft.inoutlcd import set_inoutlcds, update_lcdin, update_lcdout
    from Cameras_Layers.vboxright.pplnumlimit import set_spinBox, spin_update, line_notify

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
        self.limiter_timer.stop()
        del self.limiter_timer

        # kill thread
        self.thread.stopwhile()
        del self.thread
        if self.cameranum == 0:
            isCamsOpen.iscamopen = False
        if self.cameranum == 1:
            isCamsOpen.iscam1open = False
        if self.cameranum == 2:
            isCamsOpen.iscam2open = False
        if self.cameranum == 3:
            isCamsOpen.iscam3open = False
        # Does this deallocate memory??? I don't know but it looks good.
        gc.collect()
        event.accept()
