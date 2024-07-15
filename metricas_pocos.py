import geopandas as gpd

pocos:gpd.GeoDataFrame = gpd.read_file("dados_ibirite.gpkg", driver = "GPKG", layer="pocos")

keys = [
    "desenho",
    "construtivos",
    "geologicos",
    "hidrogeologicos",
    "teste_bomb",
    "analise_quimica",
]

print(f"N pocos {len(pocos.index)}")

for key in keys:
    data = pocos[pocos[key]]
    print(f"  {len(data.index)} items em {key}")

