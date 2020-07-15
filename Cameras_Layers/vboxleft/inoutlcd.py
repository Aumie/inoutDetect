# Import database module.
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber
from process import isCamsOpen


def set_inoutlcds(self):
    self.outlcd = self.findChild(QLCDNumber, 'outlcd')
    self.inlcd = self.findChild(QLCDNumber, 'inlcd')
    self.resin = 0
    self.resout = 0

    self.timer_in = QtCore.QTimer(self)
    self.timer_out = QtCore.QTimer(self)

    self.timer_in.timeout.connect(self.update_lcdin)
    self.timer_out.timeout.connect(self.update_lcdout)

    self.timer_in.start(1000)
    self.timer_out.start(1000)


def update_lcdin(self):
    self.inlcd.display(isCamsOpen.p_in)


def update_lcdout(self):
    self.outlcd.display(isCamsOpen.p_out)
