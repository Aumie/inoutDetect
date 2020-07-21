import re
from PyQt5.QtCore import pyqtSlot, QThread
from MainLayers.checkingThread import Worker, LoadingScreen
from MainLayers.dialog_box import information_box
from MainLayers.ipDialog import ipDialog
from process import isCamsOpen


class IpInputs(QThread):
    def __init__(self, cameranum):
        super().__init__()
        self.cameranum = cameranum
        self.ipdialog = None
        self.loading = None
        # flag for ip box
        self.isValidIp = False
        self.isTestIpDone = False
        self.ipBoxFlag = False

        self.ipdialog = ipDialog()
        self.ipdialog.setWindowTitle('IP{} Setting'.format(self.cameranum + 1))
        self.ipdialog.show()
        self.ipdialog.okbtn.clicked.connect(self.accept_ip)

    from MainLayers.ipChecker import ipChecker, update_isTestIpDone, update_isValidIp

    def accept_ip(self):
        # check if ok already clicked
        if self.ipBoxFlag:
            return information_box('Please, be patient.', 0)
        # pattern check
        pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

        iptext = self.ipdialog.camipinput.text()
        id = self.ipdialog.idinput.text()
        pwd = self.ipdialog.pwdinput.text()

        if not pattern.match(iptext):
            if iptext != '':
                return information_box('Wrong ip pattern', 0)

        # print(isCamsOpen.camip)
        if iptext != '':
            self.testip = 'rtsp://{0}:{1}@{2}:554/stream1'.format(id, pwd, iptext)
            # print(isCamsOpen.camip)
            # print(self.testip)

            allip = [isCamsOpen.camip, isCamsOpen.camip1, isCamsOpen.camip2, isCamsOpen.camip3]
            for idx in range(len(allip)):
                if allip[idx] == self.testip:
                    return information_box('You Donky!\nThis ip has already been used.', -1)

            self.ipChecker()
            # print(self.testip)
            self.ipBoxFlag = True
        if iptext == '':
            self.ipdialog.close()
