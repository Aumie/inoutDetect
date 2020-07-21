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
        # flag of variable that will point to new window
        self.ipdialog = None
        self.loading = None
        self.camdialog = None
        # flag for ip box
        self.isValidIp = False
        self.isTestIpDone = False
        self.ipBoxFlag = False

        self.ipdialog = ipDialog()
        self.ipdialog.setWindowTitle('IP{} Setting'.format(self.cameranum + 1))
        self.ipdialog.show()
        self.ipdialog.okbtn.clicked.connect(self.accept_ip)
        self.ipdialog.clearbtn.clicked.connect(self.clear_curIP)
        self.ipdialog.formatbox.currentTextChanged.connect(self.select_format)
        self.selectedformat = 'r'

    from MainLayers.ipChecker import ipChecker, update_isTestIpDone, update_isValidIp

    def select_format(self):
        text = self.ipdialog.formatbox.currentText()
        if text == 'RSTP':
            self.selectedformat = 'r'
            self.ipdialog.idinput.setText('')
            self.ipdialog.idinput.setReadOnly(False)
            self.ipdialog.pwdinput.setText('')
            self.ipdialog.pwdinput.setReadOnly(False)
        else:
            self.selectedformat = 'h'
            self.ipdialog.idinput.setText('')
            self.ipdialog.idinput.setReadOnly(True)
            self.ipdialog.pwdinput.setText('')
            self.ipdialog.pwdinput.setReadOnly(True)


    def clear_curIP(self):
        if self.cameranum == 0:
            isCamsOpen.camip = None
        if self.cameranum == 1:
            isCamsOpen.camip1 = None
        if self.cameranum == 2:
            isCamsOpen.camip2 = None
        if self.cameranum == 3:
            isCamsOpen.camip3 = None
        information_box('IP{} has been cleared'.format(self.cameranum + 1), 1)

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
            if self.selectedformat == 'r':
                self.testip = 'rtsp://{0}:{1}@{2}:554/stream1'.format(id, pwd, iptext)
            else:
                self.testip = 'http://{}:8081/'.format(iptext)
            # print(isCamsOpen.camip)
            # print(self.testip)

            allip = [isCamsOpen.camip, isCamsOpen.camip1, isCamsOpen.camip2, isCamsOpen.camip3]
            for idx in range(len(allip)):
                if allip[idx] == self.testip:
                    return information_box('You Donky!\nThis IP has already been used.', -1)

            self.ipChecker()
            # print(self.testip)
            self.ipBoxFlag = True
        if iptext == '':
            self.ipdialog.close()
