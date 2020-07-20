import os
import re

from MainLayers.ipInputs import IpInputs
from process import isCamsOpen
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QPushButton
from MainLayers.dialog_box import information_box
from MainLayers.ipDialog import ipDialog
from process.video import Camera
from process import isCamsOpen


# global CONFIG_FILE
# CONFIG_FILE = 'config.pkl'

def ping_check():
    # ping check
    response = os.system("ping -n 1 " + 'google.com')

    # and then check the response...
    if response != 0:
        return False
    return True


def grid_layout(self):
    self.openbtn = self.findChild(QPushButton, 'openbtn')
    self.openbtn1 = self.findChild(QPushButton, 'openbtn1')
    self.openbtn2 = self.findChild(QPushButton, 'openbtn2')
    self.openbtn3 = self.findChild(QPushButton, 'openbtn3')
    self.setipbtn = self.findChild(QPushButton, 'setip')
    self.setipbtn1 = self.findChild(QPushButton, 'setip1')
    self.setipbtn2 = self.findChild(QPushButton, 'setip2')
    self.setipbtn3 = self.findChild(QPushButton, 'setip3')

    self.openbtn.clicked.connect(lambda: self.open_cam(0))
    self.setipbtn.clicked.connect(lambda: self.enterip(0))
    self.openbtn1.clicked.connect(lambda: self.open_cam(1))
    self.setipbtn1.clicked.connect(lambda: self.enterip(1))
    self.openbtn2.clicked.connect(lambda: self.open_cam(2))
    self.setipbtn2.clicked.connect(lambda: self.enterip(2))
    self.openbtn3.clicked.connect(lambda: self.open_cam(3))
    self.setipbtn3.clicked.connect(lambda: self.enterip(3))


def open_cam(self, cameranum):
    if not ping_check():
        return information_box('No connection...', -1)

    if cameranum == 0:
        # print('dialog1')

        if isCamsOpen.iscamopen:
            return information_box('camera1 is Already opened', 0)

        if not isCamsOpen.camip:
            return information_box('camera1\'s ip is required.', 0)

        self.cam = Camera(cameranum)
        self.cam.show()
        isCamsOpen.iscamopen = True
    if cameranum == 1:
        # print('dialog2')

        if isCamsOpen.iscam1open:
            return information_box('camera2 is Already opened', 0)

        if not isCamsOpen.camip1:
            return information_box('camera2\'s ip is required.', 0)

        self.cam1 = Camera(cameranum)
        self.cam1.show()
        isCamsOpen.iscam1open = True
    if cameranum == 2:
        # print('dialog3')

        if isCamsOpen.iscam2open:
            return information_box('camera3 is Already opened', 0)

        if not isCamsOpen.camip2:
            return information_box('camera3\'s ip is required.', 0)

        self.cam2 = Camera(cameranum)
        self.cam2.show()
        isCamsOpen.iscam2open = True
    if cameranum == 3:
        # print('dialog4')

        if isCamsOpen.iscam3open:
            return information_box('camera4 is Already opened', 0)

        if not isCamsOpen.camip3:
            return information_box('camera4\'s ip is required.', 0)

        self.cam3 = Camera(cameranum)
        self.cam3.show()
        isCamsOpen.iscam3open = True


def enterip(self, cameranum):
    if cameranum == 0:
        self.ipdialog = IpInputs(cameranum)
        # print('dialog1')
    elif cameranum == 1:
        self.ipdialog1 = IpInputs(cameranum)
        # print('dialog2')
    elif cameranum == 2:
        self.ipdialog2 = IpInputs(cameranum)
        # print('dialog3')
    elif cameranum == 3:
        self.ipdialog3 = IpInputs(cameranum)
        # print('dialog4')
