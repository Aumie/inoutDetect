from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QTextCharFormat, QIcon
from PyQt5.QtWidgets import QCalendarWidget, QMessageBox
from datetime import datetime
from MainLayers.dialog_box import information_box


def set_calendar(self):
    calendar = self.findChild(QCalendarWidget, 'calendar')
    calendar.setMinimumDate(QDate(datetime.today().year - 1, datetime.today().month - 1, datetime.today().day))
    calendar.setMaximumDate(QDate(datetime.today().year + 1, datetime.today().month + 1, datetime.today().day))
    calendar.setSelectedDate(QDate(datetime.today().year, datetime.today().month, datetime.today().day))
    fm = QTextCharFormat()
    fm.setBackground(Qt.lightGray)
    today = datetime.today()
    ftoday = today.strftime('%Y%m%d')
    calendar.setDateTextFormat(QDate.fromString(ftoday, "yyyyMMdd"), fm)
    calendar.clicked.connect(self.history_popup)


def history_popup(self, cdate):
    year = '{}'.format(cdate.year())
    month = '{}'.format(cdate.month())
    month = '0' + month if len(month) == 1 else month
    day = '{}'.format(cdate.day())
    day = '0' + day if len(day) == 1 else day
    firebase = self.ref.child(year).child(month).child(day)
    data = firebase.get()
    if not data:
        return information_box('Has no data on this day.', -1)
    information_box(
        """Entered : {0}
Exit : {1}
Start time : {2}        
End time : {3}      
        """.format(data['in'], data['out'], data['time_start'], data['time_end']), 1
    )



