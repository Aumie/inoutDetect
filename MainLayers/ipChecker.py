from PyQt5.QtCore import pyqtSlot

from MainLayers.cameraDialog import callcameraDialog
from process import isCamsOpen
from MainLayers.checkingThread import LoadingScreen, Worker
from MainLayers.dialog_box import information_box
from process import isCamsOpen


def ipChecker(self):
    # print('ipChecker func')
    self.loading = LoadingScreen()
    # print('after declare')
    self.loading.show()
    # print('after show')
    self.worker = Worker(self.testip)
    # print(self.testip)
    self.worker.isValid.connect(self.update_isValidIp)
    self.worker.isDone.connect(self.update_isTestIpDone)
    self.worker.start()
    # print('isDone '+ self.isTestIpDone)

@pyqtSlot(bool)
def update_isTestIpDone(self, value):
    self.isTestIpDone = value
    self.ipBoxFlag = False

@pyqtSlot(bool)
def update_isValidIp(self, val):
    self.isValidIp = val
    # print('Done from update_isValid')
    message = 'The test{} is Done.\n'.format(self.cameranum+1) + ('valid ip address.' if self.isValidIp else 'invalid ip address.')
    self.loading.stopAnimation()
    if self.isValidIp:
        information_box(message, 1)
        if self.cameranum == 0:
            isCamsOpen.camip = self.testip
        if self.cameranum == 1:
            isCamsOpen.camip1 = self.testip
        if self.cameranum == 2:
            isCamsOpen.camip2 = self.testip
        if self.cameranum == 3:
            isCamsOpen.camip3 = self.testip

        self.ipdialog.close()
        callcameraDialog(self.cameranum)
    else:
        information_box(message, 0)


