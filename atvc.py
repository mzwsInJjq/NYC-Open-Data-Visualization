# NYC Street Centerline (CSCL)
# st_label
# https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/inkn-q76z

# Automated Traffic Volume Counts
# street
# https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt

import pandas as pd
import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

# Load the NYC Street Centerline (CSCL) dataset
cscl = gpd.read_file(r"C:\Users\Chen\Downloads\NYC Street Centerline (CSCL)_20250223.geojson")
print(f"CSCL: {cscl.columns}")

# Load the New York City Borough Boundaries (NYBB) dataset
nybb = gpd.read_file(geodatasets.get_path("nybb"))
nybb = nybb.to_crs(epsg=4326)

# Load the Automated Traffic Volume Counts (ATVC) dataset
atvc = pd.read_csv(r"C:\Users\Chen\Downloads\Automated_Traffic_Volume_Counts_20250223.csv")
# Filter the ATVC dataset to only include the most recent year for each street
atvc = atvc.loc[atvc.groupby('street')['Yr'].idxmax()]
# Calculate the average traffic volume for each street
atvc = atvc.groupby('street').agg({'Vol': 'mean'}).reset_index()
# Remove streets with zero traffic volume
atvc = atvc[atvc['Vol'] != 0]

# Print some basic statistics about the datasets
print(f"ATVC: {atvc.columns}")
print(f"Max: {atvc['Vol'].max()}\nMedian: {atvc['Vol'].median()}\nAverage: {atvc['Vol'].mean():.1f}\nMin: {atvc['Vol'].min()}")

print(f"\n# of Streets:\nCSCL: {cscl['st_label'].unique().size}\nATVC: {atvc['street'].unique().size}")
print(atvc['street'].unique())

# Plot the NYC Street Centerline (CSCL) and New York City Borough Boundaries (NYBB) datasets
# Color the streets based on the average traffic volume from the Automated Traffic Volume Counts (ATVC) dataset']
cscl['color'] = cscl['st_label'].apply(lambda x: 'k' if x not in atvc['street'].values else 
    plt.cm.RdYlGn(LogNorm(vmin=atvc['Vol'].min(), vmax=atvc['Vol'].max())(atvc[atvc['street'] == x]['Vol'].values[0])))

fig, ax = plt.subplots(figsize=(20, 20))
cscl.plot(ax=ax, color=cscl['color'], label='CSCL', linewidth=0.6)
nybb.plot(ax=ax, color='b', label='NYBB', alpha=0.5)

plt.savefig('nyc_atvc.pdf', format='pdf', bbox_inches='tight')
plt.show()