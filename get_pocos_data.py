import geopandas as gpd
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import json

pocos:gpd.GeoDataFrame = gpd.read_file("dados_ibirite.gpkg", driver = "GPKG", layer="pocos")
service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

dados_print = {

}

dados_add = {
    "cota_terreno":[],
    "litologia":[],
    "tipo_aquifero":[],
}

for poco in pocos.itertuples():
    codigo = poco.ponto

    try:
        dados_poco = requests.get(f"https://siagasweb.sgb.gov.br/layout/detalhe.php?ponto={codigo}")
    except Exception as e:
        print(f"Erro no poço {codigo}, {e}")

        for key in dados_add.keys():
            dados_poco[key].append(None)
        continue

    if dados_poco.status_code != 200:
        print(f"Erro no poço {codigo}, Status = {dados_poco.status_code}")

        for key in dados_add.keys():
            dados_poco[key].append(None)
        continue
    
    with open(f"dados_pocos/dados_{codigo}.html", mode="w+", encoding="UTF-8") as arq:
        arq.write(dados_poco.text)
    arq.close()

    link = f"https://siagasweb.sgb.gov.br/layout/detalhe.php?ponto={codigo}"
    print(link)
    
    driver.get(link)
    time.sleep(3)

    # for n, key in enumerate(dados_add.keys()):
    #     val = input(f"{key}?\n")
    #     dados_add[key].append(val)
    input()


# for key in dados_add.keys():
#     pocos[key] = dados_add[key]
# pocos.to_file("dados_ibirite.gpkg", driver="GPKG", layer="pocos")

driver.close()