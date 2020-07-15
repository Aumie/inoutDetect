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
    self.vbox = self.findChild(QVBoxLayout, 'vlayout')
    grpbox = QGroupBox("select a camera.")
    grpbox.setFont(QFont('Times New Romans', 12))

    grid = QGridLayout()
    vbox = QVBoxLayout()

    btn = QPushButton('camera 1', self)
    # btn.setIcon(QIcon('icon.png'))
    btn.setIconSize(QSize(40, 50))
    grid.addWidget(btn, 0, 0)
    btn.clicked.connect(self.open_cam, 0)

    btn1 = QPushButton('camera 2', self)
    # btn1.setIcon(QIcon('icon.png'))
    btn1.setIconSize(QSize(40, 50))
    grid.addWidget(btn1, 0, 1)
    # btn1.clicked.connect(self.open_cam)

    btn2 = QPushButton('camera 3', self)
    # btn2.setIcon(QIcon('icon.png'))
    btn2.setIconSize(QSize(40, 50))
    # btn2.setMinimumHeight(40)
    # btn2.setMaximumHeight(40)
    grid.addWidget(btn2, 1, 0)
    # btn2.clicked.connect(self.open_cam)


    btn3 = QPushButton('camera 4', self)
    # btn1.setIcon(QIcon('icon.png'))
    btn3.setIconSize(QSize(40, 50))
    grid.addWidget(btn3, 1, 1)
    # btn3.clicked.connect(self.open_cam)


    ipsetbtn = QPushButton('Cemeras\' ip setting')
    ipsetbtn.setIconSize(QSize(40, 60))
    ipsetbtn.clicked.connect(self.enterip)

    grpbox.setLayout(grid)
    self.vbox.addWidget(ipsetbtn)
    self.vbox.addWidget(grpbox)

    self.setLayout(vbox)


def open_cam(self, cameranum):
    if cameranum == 0:
        if isCamsOpen.iscamopen:
            return information_box('camera1 is Already opened', 0)

        if not isCamsOpen.camip:
            return information_box('camera\'s ip is required.', 0)

        if not ping_check():
            return 'no connection...'

        self.cam = Camera(cameranum)
        self.cam.show()
        isCamsOpen.iscamopen = True


def enterip(self):
    self.ipdialog = IpInputs()
    # self.ipdialog = ipDialog()
    # self.ipdialog.okbtn.clicked.connect(self.accept_ip)


# def accept_ip(self):
#     # check if ok already clicked
#     if self.ipBoxFlag:
#         return information_box('Please, be patient.', 0)
#     # pattern check
#     pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
#
#     iptext = self.ipdialog.camipinput.text()
#
#     if not pattern.match(iptext):
#         if iptext != '':
#             return information_box('Wrong ip pattern', 0)
#
#     # print(isCamsOpen.camip)
#     if iptext != '':
#         self.testip = 'http://' + iptext + ':8081/'
#         # print(isCamsOpen.camip)
#         # print(self.testip)
#         self.ipChecker()
#         # print(self.testip)
#         self.ipBoxFlag = True

