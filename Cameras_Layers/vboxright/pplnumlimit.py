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
    print(isCamsOpen.limit)


sent = False


def line_notify(self):  # also set status
    global sent
    context = """Entrance{0} has reached the limit!!!
Status: In -------- {1}
          Out ------- {2}
          Total ----- {3}
          Limit ----- {4}"""
    getin = 0
    getout = 0
    total = 0
    limit = 0
    direct = 'lr'
    if self.cameranum == 0:
        limit = isCamsOpen.limit
        getin = isCamsOpen.p_in
        getout = isCamsOpen.p_out
        direct = isCamsOpen.camdirect

    if self.cameranum == 1:
        limit = isCamsOpen.limit1
        getin = isCamsOpen.p_in1
        getout = isCamsOpen.p_out1
        direct = isCamsOpen.camdirect1

    if self.cameranum == 2:
        limit = isCamsOpen.limit2
        getin = isCamsOpen.p_in2
        getout = isCamsOpen.p_out2
        direct = isCamsOpen.camdirect2

    if self.cameranum == 3:
        limit = isCamsOpen.limit3
        getin = isCamsOpen.p_in3
        getout = isCamsOpen.p_out3
        direct = isCamsOpen.camdirect3


    total = abs(getin - getout)

    # print(limit, isCamsOpen.limit)

    if total < limit != 0:
        self.status.setText('Good')
        sent = False

    if total >= limit != 0:
        self.status.setText('Full')
        if not sent:
            if direct == 'lr':
                lineAlert(context.format(self.cameranum, getin, getout, total, limit))
            else:
                lineAlert(context.format(self.cameranum, getout, getin, total, limit))

        sent = True
        # information_box('This entrance{} has reached the limit!!'.format(self.cameranum), 0)
