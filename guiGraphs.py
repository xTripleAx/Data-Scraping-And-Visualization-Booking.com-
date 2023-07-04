from PyQt5.QtWidgets import QWidget , QApplication , QDialog , QGridLayout , QVBoxLayout , QDialogButtonBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import sys

# a gui file that opens to show several plots of the data studying its distributions 

class Graphs(QDialog):
    def __init__(self):
        super(Graphs , self).__init__()
        Scattercanvas = self.getScatterPlot()
        Barcanvas = self.getBarGraph()
        Piecanvas = self.getPieChart()
        Boxcanvas = self.getBoxPlot()
        button_box = QDialogButtonBox(QDialogButtonBox.Close)
        button_box.rejected.connect(self.reject)
        insidelayout = QGridLayout()
        insidelayout.setColumnStretch(2,2)
        insidelayout.addWidget(Scattercanvas,0,0)
        insidelayout.addWidget(Barcanvas,0,1)
        insidelayout.addWidget(Piecanvas,1,0)
        insidelayout.addWidget(Boxcanvas,1,1)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(insidelayout)
        mainLayout.addWidget(button_box)
        self.setLayout(mainLayout)
        self.setWindowTitle("Check The Graphs!")

    
    def getScatterPlot(self):
        data = pd.read_csv("data.csv")
        ScatterWidget = QWidget()
        ScatterWidget.setFixedHeight(250)
        ScatterWidget.setFixedWidth(400)

        x=data['stars']
        y=data['score']
        sizes = data['price']

        ScatterWidget.figure = Figure()
        ScatterWidget.axes = ScatterWidget.figure.add_subplot(111)

        ScatterWidget.axes.scatter(x, y, s=sizes)
        ScatterWidget.axes.set_xticks([3, 4, 5])

        ScatterWidget.axes.set_xlabel('Star Rating')
        ScatterWidget.axes.set_ylabel('Score Rating')
        ScatterWidget.axes.set_title('Hotel Ratings relation with Prices')

        ScatterWidget.canvas = FigureCanvas(ScatterWidget.figure)
        layout = QVBoxLayout()
        layout.addWidget(ScatterWidget.canvas)
        ScatterWidget.setLayout(layout)

        return ScatterWidget
    

    def getBarGraph(self):
        data = pd.read_csv("data.csv")
        BarWidget = QWidget()
        BarWidget.setFixedHeight(250)
        BarWidget.setFixedWidth(400)

        count5 = len(data[data['stars'] == 5])
        count4 = len(data[data['stars'] == 4])
        count3 = len(data[data['stars'] == 3])
        count2 = len(data[data['stars'] == 2])

        x = [2,3,4,5]
        y = [count2 , count3 , count4 , count5]
        colors = ['yellow' , 'orange' , 'red' , 'blue']

        BarWidget.figure = Figure()
        BarWidget.axes = BarWidget.figure.add_subplot(111)

        BarWidget.axes.bar(x,y,color=colors[:len(x)])

        BarWidget.axes.set_xlabel('Star Rating')
        BarWidget.axes.set_ylabel('Number of Residencies')
        BarWidget.axes.set_title('Number Of Rated Residencies in Location')

        BarWidget.canvas = FigureCanvas(BarWidget.figure)
        layout = QVBoxLayout()
        layout.addWidget(BarWidget.canvas)
        BarWidget.setLayout(layout)

        return BarWidget
    

    def getPieChart(self):
        data = pd.read_csv("data.csv")
        PieChart = QWidget()
        PieChart.setFixedHeight(250)
        PieChart.setFixedWidth(400)

        starcounts = data['stars'].value_counts()

        PieChart.figure = Figure()
        PieChart.axes = PieChart.figure.add_subplot(111)
        colors = ["yellow" , "red" , "blue"]

        PieChart.axes.pie(starcounts, labels=starcounts.index, autopct='%1.1f%%' , colors=colors)
        PieChart.axes.set_title('Distribution of Star Ratings')

        PieChart.canvas = FigureCanvas(PieChart.figure)
        layout = QVBoxLayout()
        layout.addWidget(PieChart.canvas)
        PieChart.setLayout(layout)

        return PieChart
    

    def getBoxPlot(self):
        data = pd.read_csv("data.csv")
        BoxPlot = QWidget()
        BoxPlot.setFixedHeight(250)
        BoxPlot.setFixedWidth(400)

        prices = data['price']

        BoxPlot.figure = Figure()
        BoxPlot.axes = BoxPlot.figure.add_subplot(111)
        BoxPlot.axes.boxplot(prices)

        BoxPlot.axes.set_title('Box Plot of Prices Range Distribution')
        BoxPlot.axes.set_ylabel('Night Price') 

        BoxPlot.canvas = FigureCanvas(BoxPlot.figure)
        layout = QVBoxLayout()
        layout.addWidget(BoxPlot.canvas)
        BoxPlot.setLayout(layout)

        return BoxPlot


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Graphs()
    window.show()
    sys.exit(app.exec_())