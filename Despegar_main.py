import unittest
from selenium import webdriver
from Despegar_set import despegarSet
from Despegar_get import despegarGet
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class despegarMain(unittest.TestCase):
#------------------------------------#
    def setUp(self):
        option = Options()
        self.driver_service = Service(executable_path='C:/Webdriver/chromedriver.exe')
        self.driver = webdriver.Chrome(chrome_options= option, service=self.driver_service)
        self.driver.get('https://despegar.com.ar/')
        self.all_handles = self.driver.window_handles
        self.parent_handles = self.driver.current_window_handle
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)
        self.search = despegarSet(self.driver)
        self.get = despegarGet(self.driver)
    #--------------------------------------#
    
    # @unittest.skip('1')
    def test_home(self):
        self.search.home()
        self.assertTrue('Vuelos' in self.get.getBanner())

    # @unittest.skip('2')
    def test_accommodations(self):
        self.search.accommodations()
        self.assertTrue('TOTAL' in self.get.orderBanner())

    # @unittest.skip('3')
    def test_flights(self):
        self.search.flights()
        self.assertTrue('No hay vuelos disponibles en estas fechas' in self.get.flightsBanner())

    # @unittest.skip('4')
    def test_packages(self):
        self.search.packages()
        self.assertTrue('El paquete que elegiste ya no está disponible. Tranqui, éste es uno de los preferidos por los viajeros.' or 
                        'Este es el paquete que elegiste. ¡Empieza a vivir tu viaje!' in self.get.packageBanner())
        
    # @unittest.skip('5')
    def test_offers(self):
        self.search.offers()
        self.assertTrue('TOTAL' in self.get.offersBanner())

    # @unittest.skip('6')
    def test_rents(self):
        self.search.rents()
        self.assertTrue('ORDENAR POR' in self.get.rentsBanner())
    
    # @unittest.skip('7')
    def test_activities(self):
        self.search.activities()
        self.assertTrue('Detalle de su compra' in self.get.activBanner())
    
    # @unittest.skip('8')
    def test_getaways(self):
        self.search.getaways()
        self.assertTrue('Detalle del pago' in self.get.getawaysBanner())
    
    # @unittest.skip('9')
    def test_cars(self):
        self.search.cars()
        self.assertTrue('Precio final' or '¡Ups! Algo extraño está pasando...' in self.get.carsBanner())
    
    # @unittest.skip('10')
    def test_dsny(self):
        self.search.dsny()
        self.assertTrue('Total a pagar' in self.get.dsnyBanner())
    
    # @unittest.skip('11')
    def test_assist(self):
        self.search.assists()
        self.assertTrue('TOTAL' in self.get.assistBanner())
    
    # @unittest.skip('12')
    def test_transfer(self):
        self.search.transfers()
        self.assertTrue('TOTAL' in self.get.transferBanner())
        
    #----------------------------------------------------------#
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
#-------------------------#
if __name__ == '__main__':
    unittest.main()