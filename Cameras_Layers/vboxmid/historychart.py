# not use
# from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView
# from PyQt5.QtCore import Qt
# from PyQt5.QtChart import QBarCategoryAxis
# from PyQt5.QtGui import QPainter
# from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget
#
#
# def create_bar(self):
#     set0 = QBarSet('In')
#
#     for i in range(50):
#         set0 << i
#
#     series = QBarSeries()
#     series.append(set0)
#
#     chart = QChart()
#     chart.addSeries(series)
#     chart.setTitle('BarChart Example')
#     chart.setAnimationOptions(QChart.SeriesAnimations)
#
#     categories = []
#     for i in range(50):
#         categories.append('day ' + str(i))
#
#     axis = QBarCategoryAxis()
#     axis.append(categories)
#     chart.createDefaultAxes()
#     chart.setAxisX(axis, series)
#
#     chart.legend().setVisible(True)
#     chart.legend().setAlignment(Qt.AlignBottom)
#
#     chartview = QChartView(chart)
#     chartview.setRenderHint(QPainter.Antialiasing)
#
#     vbox = QVBoxLayout()
#     chartlbl = QLabel()
#     chartlbl.setText("History")
#
#     vbox.addWidget(chartlbl)
#     vbox.addWidget(chartview)
#     widget = self.findChild(QWidget, 'widget')
#     widget.setLayout(vbox)