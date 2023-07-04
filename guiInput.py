from PyQt5.QtWidgets import QApplication , QLineEdit , QGroupBox , QDialog , QVBoxLayout , QComboBox , QDialogButtonBox , QFormLayout , QLabel , QSpinBox , QCalendarWidget , QCheckBox
import sys

# a gui file that opens to take input from the user and insert into functions to fetch data 

class Dialog(QDialog):

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept_dialog)
        buttonBox.rejected.connect(self.reject_dialog)
        
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        
        self.setWindowTitle("Choose Your Location!")
        
    def createFormGroupBox(self):
        self.resize(700,700)
        self.formGroupBox = QGroupBox("Enter the Requirments!")
        layout = QFormLayout()
        self.location = QLineEdit()
        self.adultbox = QSpinBox()
        self.adultbox.setMinimum(1)
        self.roombox = QSpinBox()
        self.roombox.setMinimum(1)
        self.childrenbox = QSpinBox()
        self.Currency = QComboBox()
        self.Currency.addItem("U.S. Dollar")
        self.Currency.addItem("Euro")
        self.Currency.addItem("Australian Dollar")
        self.Currency.addItem("Turkish Lira")
        self.Currency.addItem("United Arab Emirates Dirham")
        self.Currency.addItem("Egyptian Pound")
        self.Currency.addItem("Saudi Arabian Riyal")
        self.breakfastIN = QCheckBox()
        self.StarRating = QComboBox()
        self.StarRating.addItem("3")
        self.StarRating.addItem("4")
        self.StarRating.addItem("5")
        self.StarRating.addItem("All")
        layout.addRow(QLabel("Location:"), self.location)
        layout.addRow(QLabel("adult count:"), self.adultbox)
        layout.addRow(QLabel("children count:"), self.childrenbox)
        layout.addRow(QLabel("room count:"), self.roombox)
        layout.addRow(QLabel("Currency:"), self.Currency)
        layout.addRow(QLabel("Breakfast Included"), self.breakfastIN)
        layout.addRow(QLabel("Star Rating"),self.StarRating)
        self.calendarcheckin = QCalendarWidget()
        calendarcheckinlabel = QLabel("Select check-in")
        self.calendarcheckout = QCalendarWidget()
        calendarcheckoutlabel = QLabel("Select check-out")
        layout.addRow(calendarcheckinlabel, self.calendarcheckin)
        layout.addRow(calendarcheckoutlabel, self.calendarcheckout )
        self.formGroupBox.setLayout(layout)

        def updatecheckinqlabel():
            selected_date = self.calendarcheckin.selectedDate().toString("yyyy-MM-dd")
            calendarcheckinlabel.setText(f"{selected_date}")
        
        def updatecheckoutqlabel():
            selected_date = self.calendarcheckout.selectedDate().toString("yyyy-MM-dd")
            calendarcheckoutlabel.setText(f"{selected_date}")
        
        self.calendarcheckin.selectionChanged.connect(updatecheckinqlabel)
        self.calendarcheckout.selectionChanged.connect(updatecheckoutqlabel)
    
    def get_location(self):
        return self.location.text().strip()
    
    def get_Currency(self):
        return self.Currency.currentText().strip()
    
    def get_adult_count(self):
        return self.adultbox.value()
    
    def get_children_count(self):
        return self.childrenbox.value()
    
    def get_room_count(self):
        return self.roombox.value()
    
    def is_breakfast_included(self):
        return self.breakfastIN.isChecked()
    
    def get_star_rating(self):
        return self.StarRating.currentText().strip()
    
    def get_checkin_date(self):
        return self.calendarcheckin.selectedDate().toString("yyyy-MM-dd")
    
    def get_checkout_date(self):
        return self.calendarcheckout.selectedDate().toString("yyyy-MM-dd")
    
    def accept_dialog(self):
        self.result = QDialog.accepted
        self.accept() 
    
    def reject_dialog(self):
        self.result = QDialog.rejected
        self.reject()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())