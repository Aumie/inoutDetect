from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class Camera(QMainWindow):
    def __init__(self):
        super(Camera, self).__init__()
        uic.loadUi('ui/prototype.ui', self)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))

        self.set_time()
        self.set_monitor()
        self.set_inoutlcds()
        self.set_totallcd()


    from Cameras_Layers.vboxright.timedisplay import set_time
    from Cameras_Layers.vboxright.totallcd import set_totallcd
    from Cameras_Layers.vboxmid.monitor import set_monitor, update_image, convert_cv_qt
    from Cameras_Layers.vboxleft.inoutlcd import set_inoutlcds, update_lcdin, update_lcdout
