import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException , StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import constants as const
from selenium import webdriver
from bookingfiltration import bookingfiltration as bf
from bookingreport import BookingReport as br

#This class is the main class that uses the selenium driver to automate tasks accros the website using a bunch of functions
#such as find_element send_keys , and click to interact and fill in the website

class Booking(webdriver.Chrome):

    def __init__(self, options=None):  # constructor of the class
        driver = ChromeDriverManager().install()
        if options is None:
            options = webdriver.ChromeOptions()
        super(Booking, self).__init__(executable_path=driver, options=options)
        self.maximize_window()


    def land_first_page(self):  #The object goes to the website
        self.get(const.WEBSITE)


    def change_currency(self , currency=None):  #a function that takes user currency and selects it on the websites
        changeclicked = False
        currency_element = self.find_element(By.CSS_SELECTOR , 'button[data-testid="header-currency-picker-trigger"]')
        while not changeclicked:
            try:
                currency_element.click()
                changeclicked = True
                print("clicked!")
            except:
                pass
        self.implicitly_wait(10)
        while True:
            try:
                dismisssignin = self.find_element(By.CSS_SELECTOR , 'button[aria-label="Dismiss sign-in info."]')
                dismisssignin.click()
                break
            except:
                pass
        Selected_Currency = self.find_element(By.XPATH,f"//span[text()='{currency}']")
        currencyclicked = False
        while not currencyclicked:
            try:
                Selected_Currency.click()
                currencyclicked = True
                print("clicked!")
            except:
                pass


    def selectplacetogo(self , place=None):  #a function that takes user desired location to travel to and inserts it in inputss
        searchfeild = self.find_element(By.ID , ":Ra9:")
        searchfeild.clear()
        searchfeild.send_keys(place)
        time.sleep(2)
        suggestion = self.find_element(By.CLASS_NAME , "a80e7dc237")
        suggestion.click()


    def select_date(self , checkin , checkout):  #a function that takes user desired date to travel and inserts it in inputss
        for _ in range(15):
            try:
                checkinelemnt = self.find_element(By.CSS_SELECTOR , f'span[data-date="{checkin}"]')
                checkinelemnt.click()
                print("Check-in Clicked!")
                checkoutelement = self.find_element(By.CSS_SELECTOR , f'span[data-date="{checkout}"]')
                checkoutelement.click()
                print("Check-out Clicked!")
                break
            except NoSuchElementException:
                    nextdatetable = self.find_element(By.CLASS_NAME , "be298b15fa")
                    nextdatetable.click()
       


    def select_adults(self , adultcount=1): # a function that takes user input of number of adults and inserts it in the input
        parentofvalues = self.find_element(By.CLASS_NAME , "df856d97eb")
        children_elements = parentofvalues.find_elements(By.XPATH , "./*")
        decreasebtn = children_elements[0].find_element(By.CLASS_NAME , "cd7aa7c891")
        increasebtn = children_elements[0].find_element(By.CLASS_NAME , "d64a4ea64d")
        value = children_elements[0].find_element(By.CLASS_NAME , "e615eb5e43")
        while int(value.text) != 1:
            decreasebtn.click()
            print("Decrease Adults Clicked")
        while int(value.text) != adultcount:
            increasebtn.click()
            print("Increase Adults Clicked")


    def select_children(self , childrencount=1): # a function that takes user input of children number
        parentofvalues = self.find_element(By.CLASS_NAME , "df856d97eb")
        children_elements = parentofvalues.find_elements(By.XPATH , "./*")
        decreasebtn = children_elements[1].find_element(By.CLASS_NAME , "cd7aa7c891")
        increasebtn = children_elements[1].find_element(By.CLASS_NAME , "d64a4ea64d")
        value = children_elements[1].find_element(By.CLASS_NAME , "e615eb5e43")
        while int(value.text) != 0:
            decreasebtn.click()
            print("Decrease Children Clicked")
        while int(value.text) != childrencount:
            increasebtn.click()
            print("Increase Children Clicked")
        
        if int(value.text) != 0:
            parentofages = self.find_element(By.CSS_SELECTOR , "div[data-testid='kids-ages']")
            children_elements = parentofages.find_elements(By.XPATH , "./*")
            for child in children_elements:
                selectelement = child.find_element(By.CSS_SELECTOR , "select[name='age']")
                selectelement = Select(selectelement)
                selectelement.select_by_value("17")


    def select_rooms(self , roomcount=1): # a function that takes user input of how many rooms needed
        parentofvalues = self.find_element(By.CLASS_NAME , "df856d97eb")
        children_elements = parentofvalues.find_elements(By.XPATH , "./*")
        if int(children_elements[1].find_element(By.CLASS_NAME , "e615eb5e43").text) != 0:
            decreasebtn = children_elements[4].find_element(By.CLASS_NAME , "cd7aa7c891")
            increasebtn = children_elements[4].find_element(By.CLASS_NAME , "d64a4ea64d")
            value = children_elements[4].find_element(By.CLASS_NAME , "e615eb5e43")
            while int(value.text) != 1:
                decreasebtn.click()
                print("Decrease Rooms Clicked")
            while int(value.text) != roomcount:
                increasebtn.click()
                print("Increase Rooms Clicked")
        else:
            decreasebtn = children_elements[2].find_element(By.CLASS_NAME , "cd7aa7c891")
            increasebtn = children_elements[2].find_element(By.CLASS_NAME , "d64a4ea64d")
            value = children_elements[2].find_element(By.CLASS_NAME , "e615eb5e43")
            while int(value.text) != 1:
                decreasebtn.click()
                print("Decrease Rooms Clicked")
            while int(value.text) != roomcount:
                increasebtn.click()
                print("Increase Rooms Clicked")


    def select_occupation(self , adultcount=1 , childrencount=0 , roomcount=1): # a function that combines the last three to call in the main file
        toshowbutton = self.find_element(By.CLASS_NAME , "b7d08821c3") 
        toshowbutton.click()
        self.select_adults(adultcount)
        self.select_children(childrencount)
        self.select_rooms(roomcount)


    def clicksearch(self): # a function that clicks the search button to search for deals
        searchbtn = self.find_element(By.CLASS_NAME , "aa11d0d5cd")
        searchbtn.click()

    
    def applyFiltrations(self , star="All" , breakfast=False): # a function that uses bookingfiltration file according to user inptuts
        filtration = bf(driver=self)
        if star != "All":
            filtration.applyStarRating(star)
        if breakfast:
            filtration.BreakfastInc(breakfast)
        time.sleep(5)

    def checkifclickable(self): # a function that ensures the availability of the next page of deals to fetch data from
        while True:
            try:
                element = self.find_element(By.CSS_SELECTOR , "button[aria-label='Next page']")
                if element.is_enabled():
                    element.click()
                    return True
                else:
                    return False
            except StaleElementReferenceException or NoSuchElementException:
                return False


    def reportresults(self): # a function that uses booking report file to fetch the data (recursion is for multiple pages)
        dealbox = self.find_element(By.CLASS_NAME , "d4924c9e74")
        report = br(dealbox)
        report.getInfo()
        if self.checkifclickable():
            time.sleep(5)
            self.reportresults()
        else:
            print("done!")
        