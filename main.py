from selenium import webdriver
import time
from selenium.webdriver.common.by import By
CarteRecherché = input("quel carte voulez-vous ?")
driver = webdriver.Chrome()
# CarteRecherché = "Numéro 17 : Dragon Léviathan"
driver.get('https://www.cardmarket.com/fr/YuGiOh')

driver.find_element(By.XPATH , "/html/body/header/div[1]/div/div/form/div/button").click()
print(10)

# insérer le nom de la carte dans le champ recherché 
driver.find_element(By.XPATH , "/html/body/header/nav[2]/form/div[1]/div/input[1]").send_keys(CarteRecherché)
print(15)

# /html/body/header/nav[2]/form/div/div/button
# cliquer sur le boutton afin de lancer la recherche
driver.find_element(By.XPATH , "/html/body/header/nav[2]/form/div/div/button").click()
print(18)

# /html/body/main/section/div[3]/div[2]/div/a[2]
# driver.find_element(By.XPATH , "/html/body/main/section/div[3]/div[2]/div/a[2]").click()
print(20)
#//*[@id="idRarity67ffc29375a99"]
# driver.find_element(By.XPATH , '[@id="idRarity67ffc29375a99"]').click()

# element = driver.find_element(By.XPATH, "/html/body/main/section/div[3]/div[2]/div/a[2]")
# href = element.get_attribute("href")
# print(href)
print(21)
time.sleep(60)
