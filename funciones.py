from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

"""
La función selector gestiona las busquedas en la web y diferentes posibilidades de buscadores de elementos de Selenium.
Junto con diferentes funciones. Ej: hacer click, escribir, borrar. 
"""
def selector(chrome, selector, elemento, uso, palabras=""):
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
            a.send_keys(palabras)
        elif selector == "css" and uso == "click":
            a = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
            a.click()
        elif selector == "css" and uso == "escritura":
            a = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, elemento)))
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

