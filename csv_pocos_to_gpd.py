import geopandas as gpd
import pandas as pd
import numpy as np

df_dados:pd.DataFrame = pd.read_csv("relatorio.csv", encoding="UTF-8", sep=";")
area:gpd.GeoDataFrame = gpd.read_file("dados_ibirite.gpkg", driver="GPKG", layer = "area_drenagem_sup")

latitudes = df_dados.pop("latitude_decimal")
latitudes = np.array(latitudes, dtype=str)
latitudes = np.char.replace(latitudes, ",", ".")

longitudes = df_dados.pop("longitude_decimal") 
longitudes = np.array(longitudes, dtype=str)
longitudes = np.char.replace(longitudes, ",", ".")

points = gpd.points_from_xy(longitudes, latitudes, crs="EPSG:4326")
gdf:gpd.GeoDataFrame = gpd.GeoDataFrame(df_dados, geometry=points)

mask = area.geometry.values[0].contains(gdf.geometry)
gdf = gdf[mask]

gdf.to_file("dados_ibirite.gpkg", driver="GPKG", layer="pocos")