import requests
import os
import yaml
from datetime import datetime, timedelta
from dateutil import parser as date_parser
import argparse

class GOESDownloader:
    def __init__(self):
        """
        Initializes the downloader without configuration.
        """
        pass

    def initialize(self, config_path):
        """
        Loads the configuration from a YAML file and sets up the downloader.
        
        Parameters:
        config_path (str): Path to the YAML configuration file.
        """
        with open(config_path, 'r') as file:
            self.config = yaml.safe_load(file)
        
        # Support multiple products
        self.products = self.config['products']  # Expecting a list of products now
        self.start_date = date_parser.parse(self.config['start_date'])
        self.end_date = date_parser.parse(self.config['end_date'])
        self.satellite = self.config['satellite']
        self.save_dir = self.config['save_dir']
        self.proxies = {
            "http": "http://130.160.26.252:3128",
            "https": "http://130.160.26.252:3128"
        }

    def _get_product_url(self, product):
        """ Helper function to get the base URL for a given product """
        product_urls = {
            "AirMass":  f"https://cdn.star.nesdis.noaa.gov/GOES{self.satellite}/ABI/CONUS/AirMass/",
            "GEOCOLOR": f"https://cdn.star.nesdis.noaa.gov/GOES{self.satellite}/ABI/CONUS/GEOCOLOR/",
            "Sandwich": f"https://cdn.star.nesdis.noaa.gov/GOES{self.satellite}/ABI/CONUS/Sandwich/",
        }
        for i in range(1, 17):
            band_key = f"{str(i).zfill(2)}"
            product_urls[band_key] = f"https://cdn.star.nesdis.noaa.gov/GOES{self.satellite}/ABI/CONUS/{str(i).zfill(2)}/"
        
        base_url = product_urls.get(product)
        if not base_url:
            raise ValueError(f"Product '{product}' not found in available products.")
        return base_url
    
    def download_goes(self):
        """
        Downloads GOES-West images for multiple products from a start date to an end date.
        
        Returns:
        downloaded_images: List of downloaded images.
        """
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        downloaded_images = []
        logfile = os.path.join(self.save_dir, "download_log.txt")

        current_date = self.start_date
        while current_date <= self.end_date:
            start_hour = current_date.hour if current_date.date() == self.start_date.date() else 0
            for hour in range(start_hour, 24):
                for minute in range(60):
                    timestamp = current_date.replace(hour=hour, minute=minute, second=0, microsecond=0).strftime('%Y%j%H%M')

                    for product in self.products:
                        url = f"{self._get_product_url(product)}{timestamp}_GOES{self.satellite}-ABI-CONUS-{product}-416x250.jpg"
                        
                        try:
                            print(url)
                            response = requests.get(url, stream=True, timeout=10, proxies=self.proxies)
                            if response.status_code == 200:
                                image_path = os.path.join(self.save_dir, f"{product}_{timestamp}.jpg")

                                # Check if file already exists
                                if os.path.exists(image_path):
                                    print(f"File already exists: {image_path}")
                                    continue

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

                    if current_date >= self.end_date:
                        break
                if current_date >= self.end_date:
                    break

        return downloaded_images
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download GOES images based on a configuration file.")
    parser.add_argument('config_path', type=str, help='Path to the YAML configuration file')
    args = parser.parse_args()

    downloader = GOESDownloader()
    downloader.initialize(args.config_path)
    downloaded_images = downloader.download_goes()
