from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

# 1 information 0 warning -1 error
def information_box(message, type):
    dialog = QMessageBox()
    dialog.setWindowIcon(QIcon('ui/spongebob_police.png'))
    dialog.setStyleSheet(open("ui/style.qss", "r").read())

    if type == 1:
        dialog.setIcon(QMessageBox.Information)
        dialog.setText('Information')
        dialog.setWindowTitle('Information')
    elif type == 0:
        dialog.setIcon(QMessageBox.Warning)
        dialog.setText('Warning')
        dialog.setWindowTitle('Warning')
    elif type == -1:
        dialog.setIcon(QMessageBox.Critical)
        dialog.setText('Error')
        dialog.setWindowTitle('Error')

    dialog.setInformativeText(message)
    dialog.exec_()