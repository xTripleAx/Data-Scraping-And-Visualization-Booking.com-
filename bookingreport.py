from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
import csv

# a class that manages the fetching of data after the search

class BookingReport():
    def __init__(self , sectionelement:WebElement):
        self.sectionelement = sectionelement
        self.deals=self.pull_deals()


    def pull_deals(self): # a function that selects the element that contains the deals in the page
        return self.sectionelement.find_elements(By.CSS_SELECTOR , "div[data-testid='property-card']")


    def getInfo(self): # a function that fetches the data from the element that contains deals
        deals = self.pull_deals()
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for deal in deals:
                try:
                    hotelname = str(deal.find_element(By.CLASS_NAME , "a23c043802").get_attribute('innerHTML')).strip()
                    try:
                        hotelstarrating = str(deal.find_element(By.CLASS_NAME , "e4755bbd60").get_attribute('aria-label')).strip()[0]
                    except:
                        continue
                    try:
                        hotelscore = str(deal.find_element(By.CLASS_NAME , "d10a6220b4").get_attribute('innerHTML')).strip()
                    except:
                        continue
                    pricestring = str(deal.find_element(By.CSS_SELECTOR , "span[data-testid='price-and-discounted-price']").get_attribute('innerHTML')).strip()
                    numericprice = ''.join(filter(str.isdigit,pricestring))
                    data = [hotelname , hotelstarrating , hotelscore , numericprice]
                    writer.writerow(data)
                except:
                    pass