from PyQt5 import QtCore
from PyQt5.QtWidgets import QLCDNumber
from process import isCamsOpen


def set_totallcd(self):
    self.totallcd = self.findChild(QLCDNumber, 'totallcd')

    self.totaltimer = QtCore.QTimer(self)
    self.totaltimer.timeout.connect(lambda: self.totallcd.display(isCamsOpen.p_in - isCamsOpen.p_out))
    self.totaltimer.start(1000)
