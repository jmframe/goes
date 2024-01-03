import requests
import os
from datetime import datetime, timedelta

def download_goes_west(product, start_date, end_date, save_dir):
    """
    Downloads GOES-West images for a specified product from a start date to an end date.

    Parameters:
    product (str): The GOES product to download (e.g., 'GeoColor', 'Band 01').
    start_date (datetime): The starting date for downloading images.
    end_date (datetime): The ending date for downloading images.
    save_dir (str): Directory where the images will be saved.

    Returns:
    list: List of paths to the downloaded images.
    """
    # Mapping of products to their base URLs
    product_urls = {
        "Sandwich": "https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/Sandwich/",
        "DMW": "https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/DMW/",
        "DayNightCloudMicroCombo": "https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/DayNightCloudMicroCombo/",
        "FireTemperature": "https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/FireTemperature/",
        "Dust": "https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/Dust/"
    }
    # Adding Bands 01 to 16
    for i in range(1, 17):
        band_key = f"{str(i).zfill(2)}"
        product_urls[band_key] = f"https://cdn.star.nesdis.noaa.gov/GOES18/ABI/CONUS/{str(i).zfill(2)}/"

    base_url = product_urls.get(product)
    if not base_url:
        raise ValueError(f"Product '{product}' not found in available products.")

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    downloaded_images = []
    logfile = os.path.join(save_dir, "download_log.txt")

    current_date = start_date
    while current_date <= end_date:
        start_hour = current_date.hour if current_date.date() == start_date.date() else 0
        for hour in range(start_hour, 24):
            for minute in range(60):
                timestamp = current_date.replace(hour=hour, minute=minute, second=0, microsecond=0).strftime('%Y%j%H%M')
                url = f"{base_url}{timestamp}_GOES18-ABI-CONUS-{product}-416x250.jpg"

                try:
                    response = requests.get(url, stream=True, timeout=10)
                    if response.status_code == 200:
                        image_path = os.path.join(save_dir, f"{product}_{timestamp}.jpg")
                        with open(image_path, 'wb') as f:
                            for chunk in response:
                                f.write(chunk)
                        downloaded_images.append(image_path)
                        with open(logfile, 'a') as log:
                            log.write(f"{image_path}\n")
                        print(f"Downloaded: {url}")
                    else:
                        print(f"No image found at: {url}")
                except requests.RequestException as e:
                    print(f"Error accessing {url}: {e}")
                current_date += timedelta(minutes=1)

                if current_date >= end_date:
                    break
            if current_date >= end_date:
                break

    return downloaded_images

# Example usage
product = "Sandwich"  # Replace with the desired product
start_date = datetime(2024, 1, 3, 14)
end_date = start_date + timedelta(hours=1)  # Setting end date to tomorrow
save_directory = "./downloaded_goes_west_images"

downloaded = download_goes_west(product, start_date, end_date, save_directory)
