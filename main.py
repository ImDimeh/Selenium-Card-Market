from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
CarteRecherché = input("quel carte voulez-vous ?")
driver = webdriver.Chrome()
# CarteRecherché = "Numéro 17 : Dragon Léviathan"
driver.get('https://www.cardmarket.com/fr/YuGiOh')

driver.find_element(By.XPATH , "/html/body/header/div[1]/div/div/form/div/button").click()
print(10)

# insérer le nom de la carte dans le champ recherché 
driver.find_element(By.XPATH , "/html/body/header/nav[2]/form/div[1]/div/input[1]").send_keys(CarteRecherché)
print(15)



# cliquer sur le boutton afin de lancer la recherche
driver.find_element(By.XPATH , "/html/body/header/nav[2]/form/div/div/button").click()
print(18)

# /html/body/main/section/div[3]/div[2]/div/a[2]
# driver.find_element(By.XPATH , "/html/body/main/section/div[3]/div[2]/div/a[2]").click()
print(20)
#//*[@id="idRarity67ffc29375a99"]
# driver.find_element(By.XPATH , '[@id="idRarity67ffc29375a99"]').click()
time.sleep(4)

# je change la disposition en galerie
element = driver.find_element(By.XPATH, "/html/body/main/section/div[3]/div[2]/div/a[2]").click()
# href = element.get_attribute("href")
# print(href)
#  
# choisir la rareté
driver.find_element(By.XPATH, "/html/body/main/section/div[1]/form/div/div[7]/div[1]/div/button").click()

# avoir toute les rareté
# /html/body/main/section/div[1]/form/div/div[7]/div[2]/div/div[1]/select
time.sleep(5)
select_element = driver.find_element(By.XPATH, '/html/body/main/section/div[1]/form/div/div[7]/div[2]/div/div[1]/select')
select = Select(select_element)
option_list = select.options
ListeRareté = [
    'Tout',
    'Common',
    'Rare',
    'Parallel Rare',
    'Starfoil Rare',
    'Mosaic Rare',
    'Shatterfoil',
    'Super Rare',
    'Super Parallel Rare',
    'Ultra Rare',
    'Ultra Parallel Rare',
    'Gold Rare',
    'Premium Gold Rare',
    'Gold Secret Rare',
    'Secret Rare',
    'Secret Parallel Rare',
    'Extra Secret Rare',
    'Platinum Rare',
    'Platinum Secret Rare',
    'Collectors Rare',
    'Quarter Century Secret Rare',
    'Ultimate Rare',
    'Ghost Rare',
    'Starlight Rare',
    'Holographic Rare',
    'Special',
    'Token',
    'Oversized',
    'Unknown'
]

for option in option_list:
    ListeRareté.append(option.text)
    print(option.text)
print(ListeRareté)
print(21)
time.sleep(60)
