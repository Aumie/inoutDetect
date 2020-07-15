import re
from PyQt5.QtCore import pyqtSlot, QThread
from MainLayers.checkingThread import Worker, LoadingScreen
from MainLayers.dialog_box import information_box
from MainLayers.ipDialog import ipDialog
from process import isCamsOpen


class IpInputs(QThread):
    def __init__(self):
        super().__init__()
        self.ipdialog = None
        self.loading = None
        # flag for ip box
        self.isValidIp = False
        self.isTestIpDone = False
        self.ipBoxFlag = False

        self.ipdialog = ipDialog()
        self.ipdialog.okbtn.clicked.connect(self.accept_ip)

    from MainLayers.ipChecker import ipChecker, update_isTestIpDone, update_isValidIp

    def accept_ip(self):
        # check if ok already clicked
        if self.ipBoxFlag:
            return information_box('Please, be patient.', 0)
        # pattern check
        pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

        iptext = self.ipdialog.camipinput.text()

        if not pattern.match(iptext):
            if iptext != '':
                return information_box('Wrong ip pattern', 0)

        # print(isCamsOpen.camip)
        if iptext != '':
            self.testip = 'http://' + iptext + ':8081/'
            # print(isCamsOpen.camip)
            # print(self.testip)
            self.ipChecker()
            # print(self.testip)
            self.ipBoxFlag = True
