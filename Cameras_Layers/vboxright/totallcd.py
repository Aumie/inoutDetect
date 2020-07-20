from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber
from process import isCamsOpen


def set_totallcd(self):
    self.totallcd = self.findChild(QLCDNumber, 'totallcd')

    self.totaltimer = QtCore.QTimer(self)
    if self.cameranum == 0:
        self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in - isCamsOpen.p_out))
    if self.cameranum == 1:
        self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in1 - isCamsOpen.p_out1))
    if self.cameranum == 2:
        self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in2 - isCamsOpen.p_out2))
    if self.cameranum == 3:
        self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in3 - isCamsOpen.p_out3))
    self.totaltimer.start(1000)
