import cv2
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(75,75)
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

        self.label_animate = QLabel(self)
        self.label_animate.setAlignment(Qt.AlignCenter)
        self.movie = QMovie('ui/load.gif')
        self.label_animate.setMovie(self.movie)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.label_animate)
        self.vbox.addWidget(QLabel('testing IP'))
        self.setLayout(self.vbox)
        self.startAnimation()


    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class Worker(QThread):
    '''
    Worker thread
    '''''
    isDone = pyqtSignal(bool)
    isValid = pyqtSignal(bool)

    def __init__(self, testip):
        super(Worker, self).__init__()
        self.ip = testip

    def run(self):
        '''
        Your code goes in this function
        '''
        # print("Thread start")
        cap = cv2.VideoCapture(self.ip)
        if cap is None or not cap.isOpened():
            self.isValid.emit(False)
        else:
            self.isValid.emit(True)
        self.isDone.emit(True)
        # print("Thread complete")





