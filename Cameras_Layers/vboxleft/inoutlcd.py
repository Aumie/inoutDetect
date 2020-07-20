# Import database module.
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber
from process import isCamsOpen


def set_inoutlcds(self):
    self.outlcd = self.findChild(QLCDNumber, 'outlcd')
    self.inlcd = self.findChild(QLCDNumber, 'inlcd')

    self.timer_in = QtCore.QTimer(self)
    self.timer_out = QtCore.QTimer(self)

    self.timer_in.timeout.connect(self.update_lcdin)
    self.timer_out.timeout.connect(self.update_lcdout)

    self.timer_in.start(1000)
    self.timer_out.start(1000)


def update_lcdin(self):
    if self.cameranum == 0:
        self.inlcd.display(isCamsOpen.p_in)
    if self.cameranum == 1:
        self.inlcd.display(isCamsOpen.p_in1)
    if self.cameranum == 2:
        self.inlcd.display(isCamsOpen.p_in2)
    if self.cameranum == 3:
        self.inlcd.display(isCamsOpen.p_in3)


def update_lcdout(self):
    if self.cameranum == 0:
        self.outlcd.display(isCamsOpen.p_out)
    if self.cameranum == 1:
        self.outlcd.display(isCamsOpen.p_out1)
    if self.cameranum == 2:
        self.outlcd.display(isCamsOpen.p_out2)
    if self.cameranum == 3:
        self.outlcd.display(isCamsOpen.p_out3)
