from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from datetime import datetime


def set_time(self):
    self.time = self.findChild(QLabel, 'timenumlbl')
    self.clock = QtCore.QTimer(self)
    self.clock.timeout.connect(lambda: self.time.setText("{}".format(datetime.today().strftime('%H : %M : %S'))))
    self.clock.start(1000)




