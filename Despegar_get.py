from Despegar_set import despegarSet
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class despegarGet():
#------------------#
    def __init__(self, driver):
        self.driver = driver
        self.banner = (By.CSS_SELECTOR, ("#searchbox-sbox-box-flights > div > div > div > div.sbox5-box-header--2c4hh > h1"))
        self.accomodation_total = (By.CSS_SELECTOR, '#chk-total-price > div.col.-sm-4 > p')
        self.result_flights = (By.XPATH, '/html/body/div[8]/div[4]/div/div/div[2]/div[1]/div[2]/div/span[3]/disambiguated-banner/div/div/div[2]/div[1]')
        self.result_package = (By.CSS_SELECTOR, 'body > aloha-app-root > aloha-results > div > div > div.results-wrapper.-eva-3-mt-xlg > div > div.results-items-wrapper > aloha-list-view-container > div.-eva-3-mb-xlg > h3')
        self.result_rents = (By.CSS_SELECTOR, 'body > aloha-app-root > aloha-results > div > div > div > div.results-column > div.results-items-wrapper > aloha-list-view-container > div.secondary-toolbar-wrapper.-eva-3-mb-xlg > aloha-order-inline > div > label')
        self.activ_banner = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[4]/div[2]/resume-pricebox/div[1]/div/div/dl/dt')
        self.getaways_banner = (By.CSS_SELECTOR, ' #checkout-content > div.checkout-details.-fl-sm.col.-sm-12.-lg-4.desktop-qa > pricebox > div.chk-pricebox-title.best-price.-eva-3-hide-medium-down.top-md > p')
        self.cars_banner = (By.CSS_SELECTOR, '#detail-page > div > div > div.eva-3-row > div.col.-lg-4.-sm-12.-md-12 > pricebox-with-requests > div > pricebox-detail > div > div > div.pricebox-content.eva-3-card > div > div.main-fare.main-prices-fare.top-border > div > span.text')
        self.cars_banner2 = (By.CSS_SELECTOR, '#results-page > div > div > div > div > div > div > div > div > div > div > div > error-banner > div > div > div.generic-error-title.margin-bottom-10')
        self.dsny_banner = (By.CSS_SELECTOR, '#bodyID > div:nth-child(2) > div > div:nth-child(2) > div > div > div:nth-child(4) > div.col.-sm-12.-md-5.-lg-4.cart-pricebox-container > resume-pricebox > div.eva-3-cluster-gallery.resume-pricebox.-eva-3-shadow-static.-eva-3-hide-medium-down > div > div > dl > dd.total-text > span.description')
        self.assist_banner = (By.XPATH, '//*[@id="chk-total-price"]/div[1]/p')
        self.transfers_banner = (By.XPATH, '//*[@id="chk-total-price"]/div[1]/p')
        self.switch = despegarSet(self.driver)
    #-----------------------------------------#

    def getBanner(self):
        try:
            return self.driver.find_element(*self.banner).text
        except:
            element = self.driver.find_element(*self.banner)
            text = element.get_attribute("textContent")
            return text

    def orderBanner(self):
        return self.driver.find_element(*self.accomodation_total).text

    def flightsBanner(self):
        try:
            element = self.driver.find_element(*self.result_flights)
            text = element.get_attribute("textContent")
            return text        
        except:    
            self.switch.switch_to_tab(1)
            element = self.driver.find_element(*self.result_flights)
            text = element.get_attribute("textContent")
            return text

    def packageBanner(self):
        self.switch.switch_to_tab(1)
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.result_package)).text

    def offersBanner(self):
        return self.driver.find_element(*self.accomodation_total).text
    
    def rentsBanner(self):
        return self.driver.find_element(*self.result_rents).text
    
    def activBanner(self):
        return self.driver.find_element(*self.activ_banner).text
    
    def getawaysBanner(self):
        return self.driver.find_element(*self.getaways_banner).text
    
    def carsBanner(self):
        try:
            return self.driver.find_element(*self.cars_banner).text
        except:
            return self.driver.find_element(*self.cars_banner2).text
    
    def dsnyBanner(self):
        return self.driver.find_element(*self.dsny_banner).text

    def assistBanner(self):
        return self.driver.find_element(*self.assist_banner).text
    
    def transferBanner(self):
        return self.driver.find_element(*self.transfers_banner).text