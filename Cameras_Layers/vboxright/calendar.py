# not use
# from PyQt5.QtCore import QDate, Qt
# from PyQt5.QtGui import QTextCharFormat
# from PyQt5.QtWidgets import QCalendarWidget
# from datetime import datetime
#
#
# def set_calendar(self):
#     calendar = self.findChild(QCalendarWidget, 'calendarWidget')
#     calendar.setMinimumDate(QDate(datetime.today().year - 1, datetime.today().month - 1, datetime.today().day))
#     calendar.setMaximumDate(QDate(datetime.today().year + 1, datetime.today().month + 1, datetime.today().day))
#     calendar.setSelectedDate(QDate(datetime.today().year, datetime.today().month, datetime.today().day))
#     fm = QTextCharFormat()
#     fm.setBackground(Qt.lightGray)
#     today = datetime.today()
#     ftoday = today.strftime('%Y%m%d')
#     calendar.setDateTextFormat(QDate.fromString(ftoday, "yyyyMMdd"), fm)
#     calendar.clicked.connect(self.history_popup)
#
#
# def history_popup(self, cdate):
#     self.date = '{0}{1}{2}'.format(cdate.year(), cdate.month(), cdate.day())
#     if self.ref.child(self.date).get():
#         print('ye')
#     else:
#         print('nope')
