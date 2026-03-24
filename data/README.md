# Datasets

## Quick Start

```bash
# Download small samples (~200 MB) for testing
python setup/download_datasets.py --mode sample

# Download full datasets (~10 GB) for the complete course
python setup/download_datasets.py --mode full
```

## Dataset Overview

### 1. NYC Yellow Taxi Trip Records
- **Source:** [NYC TLC](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Format:** Parquet
- **Size:** ~2-3 GB/year
- **Used in:** Weeks 1-3, 8, 9, 11
- **License:** Public domain (NYC Open Data)
- **Key columns:** pickup/dropoff datetime & location, trip distance, fare, payment type, passenger count

### 2. NYC PLUTO Property Assessment
- **Source:** [NYC Planning](https://www.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page)
- **Format:** CSV, Shapefile
- **Size:** ~200 MB
- **Used in:** Weeks 3, 8, 11
- **License:** Public domain (NYC Open Data)
- **Key columns:** borough, block, lot, zoning, land use, assessed value, building class, year built

### 3. EPA Air Quality System (AQS)
- **Source:** [EPA AirData](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
- **Format:** CSV (zipped)
- **Size:** ~1-5 GB (multi-year)
- **Used in:** Weeks 4, 7, 9
- **License:** Public domain (US Government)
- **Key columns:** date, site, parameter, sample duration, arithmetic mean, AQI

### 4. CHIRPS Rainfall
- **Source:** [CHC UCSB](https://www.chc.ucsb.edu/data/chirps)
- **Format:** NetCDF, GeoTIFF
- **Size:** ~1-6 GB
- **Used in:** Weeks 5, 11
- **License:** Public domain
- **Key variables:** precipitation (mm), lat, lon, time

### 5. ERA5 Climate Reanalysis
- **Source:** [Copernicus CDS](https://cds.climate.copernicus.eu/)
- **Format:** NetCDF, GRIB
- **Size:** Variable (subset by region/time)
- **Used in:** Week 5
- **License:** Copernicus License (free for research/education)
- **Note:** Requires free CDS account registration
- **Key variables:** temperature, wind, precipitation, pressure

### 6. WHO Global Health Observatory
- **Source:** [WHO GHO](https://www.who.int/data/gho)
- **Format:** CSV, JSON (API)
- **Size:** Variable
- **Used in:** Week 7
- **License:** CC BY-NC-SA 3.0 IGO
- **Key indicators:** Life expectancy, disease prevalence, health expenditure

### 7. US Census / ACS
- **Source:** [Census Bureau](https://www.census.gov/programs-surveys/acs/data.html)
- **Format:** CSV, API
- **Size:** ~500 MB
- **Used in:** Weeks 3, 11
- **License:** Public domain (US Government)
- **Key variables:** Population, income, education, housing characteristics

### 8. OpenStreetMap Extracts
- **Source:** [Geofabrik](https://download.geofabrik.de/)
- **Format:** PBF, Shapefile
- **Size:** 1-10 GB (by region)
- **Used in:** Week 11
- **License:** ODbL 1.0 (attribution required)
- **Key features:** Roads, buildings, POIs, land use
