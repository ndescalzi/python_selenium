import unittest
from selenium import webdriver
import funciones


class SearchCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_cantidad_remeras(self):
        """
        Busca en la web la cantidad de resultado que existen para "remeras" y lo compara con un estandar
        """
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        funciones.selector(driver, "id", "search_query_top", "escritura y ENTER", "remeras")
        funciones.selector(driver, " xpath", '//*[@id="searchbox"]/button/span', "click")
        resultado = driver.find_element_by_css_selector("div > h1> span[class='heading-counter']").text
        resultado = funciones.search_number_string(resultado)
        self.assertEqual(resultado, "0",msg="Se encontraron " + resultado + " articulos.")

    def test_cantidad_t_shirt(self):
        """
        Busca en la web la cantidad de resultado que existen para "t-shirt" y lo compara con un estandar
        """
        driver = self.driver
        driver.get("http://automationpractice.com/index.php")
        funciones.selector(driver, "id", "search_query_top", "escritura y ENTER", "t-shirt")
        funciones.selector(driver, " xpath", '//*[@id="searchbox"]/button/span', "click")
        resultado = driver.find_element_by_css_selector("div > h1> span[class='heading-counter']").text
        resultado = funciones.search_number_string(resultado)
        self.assertEqual(resultado, "0",msg="Se encontraron "+ resultado+" articulos.")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
