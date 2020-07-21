from PyQt5 import QtCore
from PyQt5.QtWidgets import QSpinBox, QLabel

from MainLayers.dialog_box import information_box
from database.linenotify import lineAlert
from process import isCamsOpen


def set_spinBox(self):
    self.spinBox = self.findChild(QSpinBox, 'spinBox')
    self.spinBox.valueChanged.connect(self.spin_update)

    self.status = self.findChild(QLabel, 'status')

    self.limiter_timer = QtCore.QTimer(self)
    self.limiter_timer.timeout.connect(self.line_notify)
    self.limiter_timer.start(1000)


def spin_update(self):
    if self.cameranum == 0:
        isCamsOpen.limit = self.spinBox.value()
    if self.cameranum == 1:
        isCamsOpen.limit1 = self.spinBox.value()
    if self.cameranum == 2:
        isCamsOpen.limit2 = self.spinBox.value()
    if self.cameranum == 3:
        isCamsOpen.limit3 = self.spinBox.value()
    # print(isCamsOpen.limit)


linehistory = [[0, 0], [0, 0]]  # total and limit ,index 0 = new, 1 = old


def line_notify(self):  # also set status
    global linehistory
    context = """Entrance{0} has reached the limit!!!
Status: In -------- {1}
          Out ------- {2}
          Total ----- {3}
          Limit ----- {4}"""
    getin = 0
    getout = 0
    total = 0
    limit = 0
    if self.cameranum == 0:
        getin = isCamsOpen.p_in
        getout = isCamsOpen.p_out
        total = getin - getout
        limit = isCamsOpen.limit
    if self.cameranum == 1:
        getin = isCamsOpen.p_in1
        getout = isCamsOpen.p_out1
        total = getin - getout
        limit = isCamsOpen.limit1
    if self.cameranum == 2:
        getin = isCamsOpen.p_in2
        getout = isCamsOpen.p_out2
        total = getin - getout
        limit = isCamsOpen.limit2
    if self.cameranum == 3:
        getin = isCamsOpen.p_in3
        getout = isCamsOpen.p_out3
        total = getin - getout
        limit = isCamsOpen.limit3

    linehistory[0].pop()
    linehistory[0].insert(0, total)
    if limit > 0:
        print(linehistory)
        linehistory[1].pop()
        linehistory[1].insert(0, limit)

        if linehistory[0][0] != linehistory[0][1] or linehistory[1][0] != linehistory[1][1]:
            if total >= limit:
                self.status.setText('Full')
                lineAlert(context.format(self.cameranum, getin, getout, total, limit))
                # information_box('This entrance{} has reached the limit!!'.format(self.cameranum), 0)
            else:
                self.status.setText('Good')

