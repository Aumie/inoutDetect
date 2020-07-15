from PyQt5.QtCore import pyqtSlot
from process import isCamsOpen
from MainLayers.checkingThread import LoadingScreen, Worker
from MainLayers.dialog_box import information_box
from process import isCamsOpen


def ipChecker(self, testip):
    # print('ipChecker func')
    self.loading = LoadingScreen()
    # print('after declare')
    self.loading.show()
    # print('after show')
    self.worker = Worker(testip)
    self.worker.isValid.connect(self.update_isValidIp)
    self.worker.isDone.connect(self.update_isTestIpDone)
    self.worker.start()
    # print('isDone '+ self.isDone)

@pyqtSlot(bool)
def update_isTestIpDone(self, value):
    self.isTestIpDone = value
    self.ipBoxFlag = False

@pyqtSlot(bool)
def update_isValidIp(self, val):
    self.isValidIp = val
    # print('Done from update_isValid')
    message = 'The test is Done.\n' + 'valid ip address.' if self.isValidIp else 'invalid ip address.'
    self.loading.stopAnimation()
    if self.isValidIp:
        information_box(message, 1)
        isCamsOpen.camip = self.testip
        self.ipdialog.close()
    else:
        information_box(message, 0)


