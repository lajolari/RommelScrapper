import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import csv

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_inmoperu(self):
        driver = self.driver
        driver.get("http://agenteinmobiliario.vivienda.gob.pe/AgentesInmobiliarios.aspx")
        elem = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[2]/td[2]")
        elem1 = driver.find_element_by_id("ContentPlaceHolder1_gvAngentesInmobiliarios_imbdetalle_0")
        elem1.click()
        correo = driver.find_element_by_id("ContentPlaceHolder1_lblCorreo")
        print(correo.text)
        
        

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()