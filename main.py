from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from rapidfuzz import process

CarteRecherché = input("Quel carte voulez-vous ? ")
RaretéRecherché = input("Quel rareté voulez-vous ? ")

driver = webdriver.Chrome()
driver.get('https://www.cardmarket.com/fr/YuGiOh')

wait = WebDriverWait(driver, 15)

# Accepter les cookies
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div[1]/div/div/form/div/button"))).click()

# Saisir le nom de la carte
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/header/nav[2]/form/div[1]/div/input[1]")))
search_input.send_keys(CarteRecherché)

# Cliquer sur le bouton de recherche
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/nav[2]/form/div/div/button"))).click()

# Cliquer sur le bouton pour changer la vue en galerie
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[3]/div[2]/div/a[2]"))).click()

# Ouvrir le menu déroulant des raretés
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[1]/form/div/div[7]/div[1]/div/button"))).click()

# Attendre le chargement du <select> contenant les raretés
select_element = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section/div[1]/form/div/div[7]/div[2]/div/div[1]/select')))
select = Select(select_element)
option_list = select.options

# Liste de raretés (triée logiquement si nécessaire)
ListeRareté = [
    'Tout', 'Common', 'Rare', 'Parallel Rare', 'Starfoil Rare', 'Mosaic Rare', 'Shatterfoil',
    'Super Rare', 'Super Parallel Rare', 'Ultra Rare', 'Ultra Parallel Rare', 'Gold Rare',
    'Premium Gold Rare', 'Gold Secret Rare', 'Secret Rare', 'Secret Parallel Rare',
    'Extra Secret Rare', 'Platinum Rare', 'Platinum Secret Rare', 'Collectors Rare',
    'Quarter Century Secret Rare', 'Ultimate Rare', 'Ghost Rare', 'Starlight Rare',
    'Holographic Rare', 'Special', 'Token', 'Oversized', 'Unknown'
]
Rareté = process.extractOne(RaretéRecherché,ListeRareté)[0]
print("Raretés choisit :" , Rareté)
select.select_by_visible_text(Rareté)

# cliquer sur le boutton TROUVER
# 
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/main/section/div[1]/form/div/div[6]/input"))).click()


# Garder le navigateur ouvert pour inspection
input("Appuyez sur Entrée pour fermer le navigateur...")
driver.quit()
