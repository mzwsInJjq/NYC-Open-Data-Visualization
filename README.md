# NYC Open Data Visualization

This repository contains a Python script that visualizes New York City open data by combining three datasets:

- **NYC Street Centerline (CSCL)**  
  Data source: [NYC Street Centerline](https://data.cityofnewyork.us/City-Government/NYC-Street-Centerline-CSCL-/inkn-q76z)

- **Automated Traffic Volume Counts (ATVC)**  
  Data source: [Automated Traffic Volume Counts](https://data.cityofnewyork.us/Transportation/Automated-Traffic-Volume-Counts/7ym2-wayt)

- **New York City Borough Boundaries (NYBB)**  
  Data provided by the [geodatasets](https://github.com/geopandas/geodatasets) library

## Overview

The `atvc.py` script performs the following steps:

1. **Load Datasets**  
   - Reads the NYC Street Centerline dataset (GeoJSON format).
   - Loads the NYC Borough Boundaries and converts the CRS to EPSG:4326.
   - Reads the Automated Traffic Volume Counts (CSV format).

2. **Data Preparation**  
   - Filters the ATVC dataset to include only the most recent year for each street.
   - Calculates the average traffic volume for each street.
   - Removes streets with zero traffic volume.

3. **Visualization**  
   - Colors the streets based on the average traffic volume using a color mapping (from red to green).
   - Plots the CSCL and NYBB datasets.
   - Saves the resulting plot as a PDF (`nyc_atvc.pdf`).
