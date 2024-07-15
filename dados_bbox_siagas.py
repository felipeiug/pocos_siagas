import requests
import geopandas as gpd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import numpy as np
import time

# Entrada dos dados
area:gpd.GeoDataFrame = gpd.read_file("dados_ibirite.gpkg", driver="GPKG", layer = "area_drenagem_sup")

# Código
def float_to_gg_mm_ss(val):
    is_neg = False
    if val < 0:
        is_neg = True

    val = abs(val)
    g = np.floor(val)
    m = np.floor((val - g)*60)
    s = np.floor((val - g - (m/60))*3600)

    return (-1 if is_neg else 1) * g, m, s


print("Obtendo o BBOX")
area.to_crs("EPSG:4326")
bbox = area.total_bounds

lat1 = float_to_gg_mm_ss(bbox[3])
long1 = float_to_gg_mm_ss(bbox[0])

lat2 = float_to_gg_mm_ss(bbox[1])
long2 = float_to_gg_mm_ss(bbox[2])

print(f"lat1: {lat1}")
print(f"long1: {long1}")
print(f"lat2: {lat2}")
print(f"long2: {long2}")

print("Obtendo o driver do selenium")
service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

print("Abrindo o SIAGAS")
link = "https://siagasweb.sgb.gov.br/layout/pesquisa_coordenada.php"
driver.get(link)

time.sleep(5)

#Lat1
latgrau1 = driver.find_element(By.TAG_NAME, 'input')
latminuto1 = driver.find_element(By.NAME, 'latminuto1')
latsegundo1 = driver.find_element(By.NAME, 'latsegundo1')

latgrau1.clear()
g, m, s = float_to_gg_mm_ss(bbox[1])
latgrau1.send_keys(str())

#Long1
longgrau1 = driver.find_element(By.NAME, 'longgrau1')
longminuto1 = driver.find_element(By.NAME, 'longminuto1')
longsegundo1 = driver.find_element(By.NAME, 'longsegundo1')

#Lat2
latgrau2 = driver.find_element(By.NAME, 'latgrau2')
latminuto2 = driver.find_element(By.NAME, 'latminuto2')
latsegundo2 = driver.find_element(By.NAME, 'latsegundo2')

#Long2
longgrau2 = driver.find_element(By.NAME, 'longgrau2')
longminuto2 = driver.find_element(By.NAME, 'longminuto2')
longsegundo2 = driver.find_element(By.NAME, 'longsegundo2')

#Botão do pesquisar
serach_btn = driver.find_element(By.NAME, 'Pesquisar')
serach_btn.click()




input("Pressione qualquer tecla para finalizar")
driver.close()