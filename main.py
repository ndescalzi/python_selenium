import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC



class SearchCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    """
    def test_PopUp(self):
        ### Verifica el texto que figura en el Pop Up sea el correcto y valida la alerta.
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_form_input_types.asp")
        selector(driver, "css", "div > input[value='Click Me!']", "click")
        alert = driver.switch_to.alert
        time.sleep(2)
        text = alert.text
        alert.accept()
        time.sleep(2)
        self.assertEqual(text, "Hello World!")
    """
    def test_CompletarCampos_Validacion(self):
        ### Modifica el texto por default y valida que se procese correctamente.
        driver = self.driver
        driver.get("https://www.w3schools.com/html/html_form_elements.asp")
        selector(driver, "css", 'fieldset > input[name="firstname"]', "escritura", "Juan")
        selector(driver, "css", 'fieldset > input[name="lastname"]', "escritura", "Perez")
        original_window = driver.current_window_handle
        selector(driver, "css", "fieldset > input[type='submit']", "click")
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break

        resultado = driver.find_element(By.CSS_SELECTOR,"body> div[class='w3-container w3-large w3-border']").text
        nombre = resultado.find("Juan")
        apellido = resultado.find("Perez")
        if nombre != -1 and apellido != -1:
            resultado = True
        else:
            resultado = False

        self.assertTrue(resultado, msg="El nombre y apellido no son los correctos.")

    def tearDown(self):
        self.driver.quit()

def selector(chrome, selector, elemento, uso, palabras=""):
    """
    La función selector gestiona las busquedas en la web y diferentes posibilidades de buscadores de elementos de Selenium.
    Junto con diferentes funciones. Ej: hacer click, escribir, borrar.
    """
    espera = WebDriverWait(chrome, 15)
    a = None
    try:
        if selector == "id" and uso == "click":
            a = espera.until(EC.presence_of_element_located((By.ID, elemento)))
            a.click()
        elif selector == "id" and uso == "escritura":
            a = espera.until(EC.presence_of_element_located((By.ID, elemento)))
            a.send_keys(palabras)
        elif selector == "id" and uso == "borrar":
            a = espera.until(EC.presence_of_all_elements_located((By.ID, elemento)))
            chrome.find_element_by_id(elemento).clear()
        elif selector == "id" and uso == "texto":
            a = espera.until(EC.presence_of_element_located((By.ID, elemento)))
            a.text
        elif selector == "id" and uso == "escritura y ENTER":
            a = espera.until(EC.presence_of_element_located((By.ID, elemento)))
            a.send_keys(palabras + Keys.ENTER)
        elif selector == "xpath" and uso == "click":
            a = espera.until(EC.element_to_be_clickable((By.XPATH, elemento)))
            a.click()
        elif selector == "xpath" and uso == "escritura":
            a = espera.until(EC.presence_of_element_located((By.XPATH, elemento)))
            a.clear()
            a.send_keys(palabras)
        elif selector == "css" and uso == "click":
            a = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
            a.click()
        elif selector == "css" and uso == "escritura":
            a = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
            a.clear()
            a.send_keys(palabras)
        elif selector == "css" and uso == "texto":
            a = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
            a.text
    except Exception as e:
        if selector == "id" and uso == "click":
            a = espera.until(EC.visibility_of_element_located((By.ID, elemento)))
            a.click()
        elif selector == "id" and uso == "escritura":
            a = espera.until(EC.visibility_of_element_located((By.ID, elemento)))
            a.send_keys(palabras)
        elif selector == "id" and uso == "borrar":
            a = espera.until(EC.visibility_of_element_located((By.ID, elemento)))
            a.clear()
        elif selector == "id" and uso == "texto":
            a = espera.until(EC.visibility_of_element_located((By.ID, elemento)))
            a.text
        elif selector == "xpath" and uso == "click":
            a = espera.until(EC.visibility_of_element_located((By.XPATH, elemento)))
            a.click()
        elif selector == "xpath" and uso == "escritura":
            a = espera.until(EC.visibility_of_element_located((By.XPATH, elemento)))
            a.send_keys(palabras)
        elif selector == "css" and uso == "click":
            a = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
            a.click()
        elif selector == "css" and uso == "escritura":
            a = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
            a.send_keys(palabras)
        elif selector == "css" and uso == "texto":
            a = espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, elemento)))
            a.text
    return a

def search_number_string(String):
    # Esta funcion recorre un string y retorna los numeros que hay en ella.
    index_list = []
    del index_list[:]
    for i, x in enumerate(String):
        if x.isdigit() == True:
            index_list.append(i)
    start = index_list[0]
    end = index_list[-1] + 1
    number = String[start:end]
    return number

if __name__ == '__main__':
    unittest.main()
