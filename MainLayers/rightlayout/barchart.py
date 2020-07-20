from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView
from PyQt5.QtCore import Qt
from PyQt5.QtChart import QBarCategoryAxis
from PyQt5.QtGui import QPainter, QIcon, QFont
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QWidget


class BarChart(QWidget):
    def __init__(self, data, date):
        super().__init__()
        self.data = data
        self.day, self.month, self.year = date
        self.setWindowTitle("PyQt BarChart")
        self.setStyleSheet(open("ui/style.qss", "r").read())
        self.setMinimumSize(480, 320)
        self.setWindowIcon(QIcon('ui/spongebob_police.png'))

        self.create_bar()

        self.show()

    def create_bar(self):
        set0 = QBarSet('In')
        set1 = QBarSet('Out')
        categories = []

        for i in range(4):
            idx0 = 'in{0}'.format(i)
            idx1 = 'out{0}'.format(i)
            if self.data[idx0] == 0 and self.data[idx1] == 0:
                continue
            categories.append('Camera ' + str(i + 1))
            set0 << self.data[idx0]
            set1 << self.data[idx1]

        series = QBarSeries()
        series.append(set0)
        series.append(set1)

        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('In-Out Barchart')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        axis = QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        vbox = QVBoxLayout()
        chartlbl = QLabel()
        chartlbl.setFont(QFont("Helvetica [Cronyx]", 18))
        chartlbl.setText("History of {0}.{1}.{2}".format(self.day, self.month, self.year))

        summary = QLabel('Start time: {0}, End time: {1}'.format(self.data['time_start'], self.data['time_end']))
        summary.setFont(QFont("Helvetica [Cronyx]", 18))
        summary.setAlignment(Qt.AlignRight)

        vbox.addWidget(chartlbl)
        vbox.addWidget(chartview)
        vbox.addWidget(summary)
        self.setLayout(vbox)
