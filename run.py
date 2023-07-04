import csv
from booking import Booking
import sys
from PyQt5.QtWidgets import QApplication , QDialog
from guiInput import Dialog
from guiPreview import Preview


#This is the main file that runs it executes all necessary functions to gather analyze, and represent data

app = QApplication(sys.argv)

file = open('data.csv', 'w' , newline='')
writer = csv.writer(file)
writer.writerow(['Name' , 'stars' , 'score' , 'price'])
file.close()

Dg = Dialog()
bot = Booking()

def handle_results():
    Location = Dg.get_location()
    currency = Dg.get_Currency()
    adults = Dg.get_adult_count()
    children = Dg.get_children_count()
    rooms = Dg.get_room_count()
    Checkin = Dg.get_checkin_date()
    Checkout = Dg.get_checkout_date()
    breakfast = Dg.is_breakfast_included()
    stars = Dg.get_star_rating()

    if Dg.result == QDialog.accepted:
        bot.land_first_page()
        bot.change_currency(currency)
        bot.selectplacetogo(Location)
        bot.select_date(Checkin, Checkout)
        bot.select_occupation(adults, children, rooms)
        bot.clicksearch()
        bot.applyFiltrations(stars, breakfast)
        bot.reportresults()
    else:
        sys.exit()

Dg.finished.connect(handle_results)
Dg.exec_()

Pv = Preview()
Pv.exec_()

#lines outside the indentation are teardown actions conventionally implemented in the exit() magic methods