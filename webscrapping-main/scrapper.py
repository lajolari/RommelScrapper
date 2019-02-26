import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
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
        """ Aqui recorremos cada pagina de este """
        for k in range(100):
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
                lista_de_clientes = [['Nombre'+str(x), name], ['Correo'+str(x), correo]]
                wakanda.append(lista_de_clientes)
                contador1+=1
                contador2+=1
            """ Aqui se guarda la lista con los 10 clientes de la primera pagina """
            if contador3 == 10: 
                huachicolero = 1
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td[11]")
            elif contador3 == 20 or contador3 == 30 or contador3 == 40 or contador3 == 50 or contador3 == 60 or contador3 == 70 or contador3 == 80 or contador3 == 90 or contador3 == 100:
                huachicolero = 1
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td[12]")
            else:
                killmonger = driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div[1]/table/tbody/tr[12]/td/table/tbody/tr/td["+str(huachicolero+1)+"]")
                huachicolero+=1
            killmonger.click()
            datos_for_csv.append(wakanda)   
            contador3+=1                    
        """ Area donde se imprime en el CSV (y en la consola) """
        print(datos_for_csv)
        
        with open("prueba.csv", "w") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for line in datos_for_csv:
                    writer.writerow(line)
        print('----------frontera-colombo-venezolana----------')


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()