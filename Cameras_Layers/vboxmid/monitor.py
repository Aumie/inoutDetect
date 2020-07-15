from PyQt5 import QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from process.people_counter import *


def set_monitor(self):
    self.monitor = self.findChild(QLabel, 'monitor')
    vlmiddle = self.findChild(QVBoxLayout, 'vlmiddle')
    self.disply_width = 640
    self.display_height = 480
    self.monitor.resize(self.disply_width, self.display_height)

    self.thread = VideoThread()
    # connect its signal to the update_image slot
    self.thread.change_pixmap_signal.connect(self.update_image)
    # start the thread
    self.thread.start()
    # print(self.thread.isRun)


@pyqtSlot(np.ndarray)
def update_image(self, cv_img):
    """Updates the image_label with a new opencv image"""
    qt_img = self.convert_cv_qt(cv_img)
    self.monitor.setPixmap(qt_img)


def convert_cv_qt(self, cv_img):
    """Convert from an opencv image to QPixmap"""
    rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
    h, w, ch = rgb_image.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)
