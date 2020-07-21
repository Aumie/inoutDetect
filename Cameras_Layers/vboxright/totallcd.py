from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber
from process import isCamsOpen


def set_totallcd(self):
    self.totallcd = self.findChild(QLCDNumber, 'totallcd')

    self.totaltimer = QtCore.QTimer(self)

    if self.cameranum == 0:
        if isCamsOpen.camdirect == 'lr':
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in - isCamsOpen.p_out))
        else:
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_out - isCamsOpen.p_in))

    if self.cameranum == 1:
        if isCamsOpen.camdirect1 == 'lr':
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in1 - isCamsOpen.p_out1))
        else:
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_out1 - isCamsOpen.p_in1))

    if self.cameranum == 2:
        if isCamsOpen.camdirect2 == 'lr':
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in2 - isCamsOpen.p_out2))
        else:
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_out2 - isCamsOpen.p_in2))

    if self.cameranum == 3:
        if isCamsOpen.camdirect3 == 'lr':
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in3 - isCamsOpen.p_out3))
        else:
            self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_out3 - isCamsOpen.p_in3))

    self.totaltimer.start(1000)
