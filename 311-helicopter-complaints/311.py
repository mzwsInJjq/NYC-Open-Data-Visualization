# NYC OpenData 311 Service Requests from 2010 to Present 
# https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9/about_data
# complaint_type="Noise - Helicopter"

# NYC Street Centerline (CSCL)
# https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/inkn-q76z/about_data

import pandas as pd
import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt

cscl = gpd.read_file(r"C:\Users\Chen\Downloads\NYC Street Centerline (CSCL)_20250325.geojson")
cscl = cscl[cscl['rw_type'] != '14']
nybb = gpd.read_file(geodatasets.get_path("nybb"))
nybb = nybb.to_crs(epsg=4326)

fig, ax = plt.subplots(figsize=(20, 20))
cscl.plot(ax=ax, color='k', label='CSCL', linewidth=0.5)
nybb.plot(ax=ax, color='b', label='NYBB', alpha=0.5)

helicopter_complaints = pd.read_csv(r"C:\Users\Chen\Downloads\311_Service_Requests_from_2010_to_Present_20250325.csv")
print(helicopter_complaints.head())
print(helicopter_complaints.info())
print(helicopter_complaints.describe())
print(helicopter_complaints.columns)

# Plot the helicopter complaints
ax.plot(helicopter_complaints['Longitude'], helicopter_complaints['Latitude'], 'rD', markersize=0.75, label='Helicopter Complaints')

plt.savefig('nyc-311-helicopter.pdf', format='pdf', bbox_inches='tight')
plt.savefig('nyc-311-helicopter.png', format='png', bbox_inches='tight', dpi=600)
