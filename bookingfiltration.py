from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

# This File is a class with methods that are responsible for filtration of results

class bookingfiltration():
    def __init__(self , driver:WebDriver):
        self.driver = driver

    
    def applyStarRating(self,stars): # a function that handles star filtrations
        classbox = self.driver.find_element(By.CSS_SELECTOR , "div[data-filters-group='class']")
        classchildren = classbox.find_elements(By.CSS_SELECTOR , "*")
        if(stars != 'All'):
            for starelement in classchildren:
                while True:
                    try:
                        if str(starelement.get_attribute('innerHTML')).strip() == f'{stars} stars':
                            starelement.click()
                        break
                    except:
                        continue
        else:
            pass


    def BreakfastInc(self , breakfast): # a function that handles breakfast filtration
        if breakfast == True:
            mealbox = self.driver.find_element(By.CSS_SELECTOR , "div[data-filters-group='mealplan']")
            breakfastincluded = mealbox.find_element(By.CSS_SELECTOR , "div[data-filters-item='mealplan:mealplan=1']")
            breakfastincluded.click()