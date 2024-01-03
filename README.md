# goes
Code for downloading, processing and using GOES data
This repository contains a Python script for downloading, processing and using GOES(Geostationary Operational Environmental Satellite) data. 

## Dowloading GOES
The script, `downloadgoes.py`, allows users to download images for specific bands or composite products over a specified date and time range.

## Installation
To use this script, you need to have Python installed on your system along with the requests package. If you do not have requests installed, you can install it using pip: `pip install requests`

## Usage
For now the specific data (product, start and end dates) need to be specified at the bottom of `downloadgoes.py`, then use the command line to run the script like so: `python3 downloadgoes.py `. Will add an interface later.
  - <product>: The GOES product to download (e.g., 'GeoColor', '01', '02', ..., '16', 'Sandwhich', etcetera).
  - <start_date>: The starting date and time for downloading images (format: YYYY-MM-DD HH).
  - <end_date>: The ending date and time for downloading images (format: YYYY-MM-DD HH).

### Products available for download
  - GeoColor: A true-color daytime product that combines Bands 2, 3, and 1 to create an image resembling how the human eye would see the Earth from space. At night, it uses an infrared band to depict clouds and ice in shades of gray, resembling moonlight illumination.  
  - Sandwhich: A combination of visible and infrared imagery.  
  - Air Mass RGB: A composite product combining water vapor and infrared imagery. Useful for identifying air mass characteristics, jet streams, and potential storm development.  
  - 01 - Band 1 (Blue) - Visible: Wavelength: ~0.47 µm. Purpose: Provides high-resolution visible imagery, useful for analyzing cloud formation, storm structures, snow/ice cover, fog, and sea ice.  
  - 02 - Band 2 (Red) - Visible: Wavelength: ~0.64 µm. Purpose: Like the blue band but with slightly different sensitivity, useful for daytime images of the Earth's surface and atmosphere.  
  - 03 - Band 3 (Veggie) - Near IR: Wavelength: ~0.86 µm. Purpose: Highlights vegetation, useful for monitoring plant health.  
  - 04 - Band 4 (Cirrus) - Near IR: Wavelength: ~1.37 µm. Purpose: Detects high-altitude cirrus clouds, useful for studying cloud formation and upper-level atmospheric moisture.  
  - 05 - Band 5 (Snow/Ice) - Near IR: Wavelength: ~1.6 µm. Purpose: Differentiates snow, ice, and clouds, helpful in snow cover and ice mapping.  
  - 06 - Band 6 (Cloud Particle Size) - Near IR: Wavelength: ~2.2 µm. Purpose: Detects cloud particle size, useful for understanding cloud composition and structure.  
  - 07 - Band 7 (Shortwave Window) - IR: Wavelength: ~3.9 µm. Purpose: Useful for fire detection, volcanic activity monitoring, and nighttime cloud imaging.  
  - 08 - Band 8 (Upper-Level Water Vapor) - IR: Wavelength: ~6.2 µm. Purpose: Monitors upper-level atmospheric water vapor, important for weather forecasting and identifying jet streams.  
  - 09 - Band 9 (Mid-Level Water Vapor) - IR: Wavelength: ~6.9 µm. Purpose: Focuses on mid-level atmospheric water vapor, aiding in weather analysis and forecasting.  
  - 10 - Band 10 (Lower-Level Water Vapor) - IR: Wavelength: ~7.3 µm. Purpose: Targets lower-level water vapor, useful for understanding lower atmospheric moisture and dynamics.  
  - 11 - Band 11 (Cloud-Top Phase) - IR: Wavelength: ~8.4 µm. Purpose: Helps in determining cloud-top phase (liquid or ice), important for weather prediction and cloud type identification.  
  - 12 - Band 12 (Ozone) - IR: Wavelength: ~9.6 µm. Purpose: Sensitive to atmospheric ozone, useful for ozone mapping and monitoring.  
  - 13 - Band 13 (Clean Longwave Window) - IR: Wavelength: ~10.3 µm. Purpose: A primary band for meteorological applications, useful for monitoring cloud cover, storm systems, and surface temperatures.  
  - 14 - Band 14 (Longwave Infrared) - IR: Wavelength: ~11.2 µm. Purpose: Similar to Band 13 but with different sensitivity, useful for analyzing cloud properties and sea surface temperatures.  
  - 15 - Band 15 (Dirty Longwave Window) - IR: Wavelength: ~12.3 µm. Purpose: Used for cloud height and particle size estimation, also helps in soil and surface temperature analysis.  
  - 16 - Band 16 (CO₂ Longwave Infrared) - IR: Wavelength: ~13.3 µm. Purpose: Sensitive to CO₂, helps in estimating the height of cloud tops and atmospheric temperature.  
  - DMW  
  - DayNightCloudMicroCombo  
  - FireTemperature  
  - Dust  

## Future Enhancements (TODO)
### GOES East:
Support for downloading images from the GOES East satellite is planned for future updates.
### Full Disc Images:
Capability to download Full Disc images covering the entire disk of the Earth as seen by GOES satellites will be added.