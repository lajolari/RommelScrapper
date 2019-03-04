import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlwt
from xlwt import Workbook
import pandas as pd

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_inmoperu(self):
        driver = self.driver
        driver.get("http://agenteinmobiliario.vivienda.gob.pe/AgentesInmobiliarios.aspx")
        contador3 = 1
        datos_for_csv = []
        huachicolero = 1
        savior = 0
        wb = Workbook()
        sheet1 = wb.add_sheet('Sheet 1')
        """ Aqui recorremos cada pagina de este """
        for k in range(101):
            lista_de_clientes = []
            wakanda = []
            contador1 = 2
            contador2 = 0
            """ Aqui recorro cada elemento de cada pagina """
            for x in range(10):
                name = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[" + str(contador1) +"]/td[2]").text
                premail = driver.find_element_by_id("ContentPlaceHolder1_gvAngentesInmobiliarios_imbdetalle_" + str(contador2))
                premail.click()
                correo = driver.find_element_by_id("ContentPlaceHolder1_lblCorreo").text
                sheet1.write(savior, 0, name)
                sheet1.write(savior, 1, correo)
                wb.save('list_clientes.xls')
                contador1+=1
                contador2+=1
                savior+=1
                print('esta pagina va por el elemento:'+ str(x))
            """ Aqui se guarda la lista con los 10 clientes de la primera pagina """
            if contador3 == 10: 
                huachicolero = 1
                savior+=1
                print('ya contador3 vale 10 y paso bien por aca')
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td[11]")
            elif contador3 >= 20 and (contador3%10) == 0:
                huachicolero = 1
                print('ya contador3 vale '+str(contador3)+' y sigue bien')
                savior+=1
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td[12]")
            elif contador3 == 51:
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td[4]")
                print('me salte el 51 jiji, voy por el: '+str(contador3))
            else:
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td["+str(huachicolero+1)+"]")
                savior+=1
                print('la secuencia ya vale: '+str(contador3))
                huachicolero+=1
            killmonger.click() 
            contador3+=1                    
        """ Area donde se imprime en el CSV (y en la consola) """        

    def tearDown(self):
        pass
        # self.driver.close()

if __name__ == "__main__":
    unittest.main()