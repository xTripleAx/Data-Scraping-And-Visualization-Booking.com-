from PyQt5.QtWidgets import QWidget , QApplication , QPushButton , QDialog , QGridLayout , QVBoxLayout , QDialogButtonBox , QLabel , QTableWidget , QTableWidgetItem
from PyQt5.QtCore import Qt
from guiGraphs import Graphs
import pandas as pd
import sys

# a gui file that opens to show data fetched as tables and organized according to several conditions 

class Preview(QDialog):
    def __init__(self):
        super(Preview , self).__init__()
        ScrollArea = self.TableScrollArea()
        BestStars = self.getBeststars()
        BestScore = self.getBestscore()
        BestPrice = self.getBestprice()
        custombtn = QPushButton("Show Graphs!")
        custombtn.clicked.connect(self.ShowGraphs)
        button_box = QDialogButtonBox(QDialogButtonBox.Close)
        button_box.rejected.connect(self.reject)
        insidelayout = QGridLayout()
        insidelayout.setColumnStretch(2,2)
        insidelayout.addWidget(ScrollArea,0,0)
        insidelayout.addWidget(BestStars,0,1)
        insidelayout.addWidget(BestScore,1,0)
        insidelayout.addWidget(BestPrice,1,1)
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(insidelayout)
        mainLayout.addWidget(button_box)
        mainLayout.addWidget(custombtn)
        self.setLayout(mainLayout)
        self.setWindowTitle("Check The Results!")
        

    def TableScrollArea(self):
        data = pd.read_csv("data.csv", encoding="iso-8859-1")
        resultwidget = QWidget()
        table = QTableWidget()
        layout = QVBoxLayout()
        resultwidget.setLayout(layout)

        table.setRowCount(len(data.index))
        table.setColumnCount(len(data.columns))
        table.setHorizontalHeaderLabels(data.columns)
        table.setFixedWidth(450)
        table.setFixedHeight(200)

        for row in range(len(data.index)):
            for col in range(len(data.columns)):
                item = QTableWidgetItem(str(data.iloc[row, col]))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                table.setItem(row, col, item)

        table.resizeColumnsToContents()
        layout.addWidget(QLabel("Your Results!"))
        layout.addWidget(table)

        return resultwidget
    
    def getBeststars(self):
        data = pd.read_csv("data.csv", encoding="iso-8859-1")
        BeststarsWidget = QWidget()
        layout = QVBoxLayout()
        BeststarsWidget.setLayout(layout)

        maxstars = data['stars'].max()
        hotelswithmaxstars = data[data['stars'] == maxstars]

        Beststars = QTableWidget()
        Beststars.setColumnCount(len(hotelswithmaxstars.columns))
        Beststars.setRowCount(len(hotelswithmaxstars))
        Beststars.setHorizontalHeaderLabels(hotelswithmaxstars.columns)
        Beststars.setFixedWidth(450)
        Beststars.setFixedHeight(200)

        for row, values in enumerate(hotelswithmaxstars.values):
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                Beststars.setItem(row, col, item)

        Beststars.resizeColumnsToContents()
        layout.addWidget(QLabel("Best Stars!"))
        layout.addWidget(Beststars)

        return BeststarsWidget
    

    def getBestscore(self):
        data = pd.read_csv("data.csv", encoding="iso-8859-1")
        BestscoreWidget = QWidget()
        layout = QVBoxLayout()
        BestscoreWidget.setLayout(layout)

        maxscore = data['score'].max()
        hotelswithmaxscore = data[data['score'] == maxscore]

        Bestscore = QTableWidget()
        Bestscore.setColumnCount(len(hotelswithmaxscore.columns))
        Bestscore.setRowCount(len(hotelswithmaxscore))
        Bestscore.setHorizontalHeaderLabels(hotelswithmaxscore.columns)
        Bestscore.setFixedWidth(450)
        Bestscore.setFixedHeight(200)

        for row, values in enumerate(hotelswithmaxscore.values):
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                Bestscore.setItem(row, col, item)

        Bestscore.resizeColumnsToContents()
        layout.addWidget(QLabel("Best Score!"))
        layout.addWidget(Bestscore)

        return BestscoreWidget
    

    def getBestprice(self):
        data = pd.read_csv("data.csv", encoding="iso-8859-1")
        BestpriceWidget = QWidget()
        layout = QVBoxLayout()
        BestpriceWidget.setLayout(layout)

        price = data['price'].mean()
        hotelswithbestprice = data[(data['price'] <= price) & ((data['stars'] == 5) | (data['stars'] == 4)) & (data['score'] >= 8)]

        Bestprice = QTableWidget()
        Bestprice.setColumnCount(len(hotelswithbestprice.columns))
        Bestprice.setRowCount(len(hotelswithbestprice))
        Bestprice.setHorizontalHeaderLabels(hotelswithbestprice.columns)
        Bestprice.setFixedWidth(450)
        Bestprice.setFixedHeight(200)

        for row, values in enumerate(hotelswithbestprice.values):
            for col, value in enumerate(values):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                Bestprice.setItem(row, col, item)

        Bestprice.resizeColumnsToContents()
        layout.addWidget(QLabel("Best Prices!"))
        layout.addWidget(Bestprice)

        return BestpriceWidget


    def ShowGraphs(self):
        graphs = Graphs()
        graphs.exec_()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Preview()
    window.show()
    sys.exit(app.exec_())