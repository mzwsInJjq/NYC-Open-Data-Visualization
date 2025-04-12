# NYC Street Centerline (CSCL)
# https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/inkn-q76z/about_data

import pandas as pd
import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt

cscl = gpd.read_file(r"C:\Users\Chen\Downloads\Centerline_20250412.geojson")
cscl = cscl[cscl['rw_type'] != '14']
nybb = gpd.read_file(geodatasets.get_path("nybb"))
nybb = nybb.to_crs(epsg=4326)

fig, ax = plt.subplots(figsize=(20, 20))
ax.axis('off')

cscl.plot(ax=ax, color='k', label='CSCL', linewidth=0.4)
nybb.plot(ax=ax, color='b', label='NYBB', alpha=0.5)

plt.savefig('nyc-cscl.pdf', format='pdf', bbox_inches='tight')