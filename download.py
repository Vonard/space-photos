import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

def download_image(url, filename, api_key = ""):
    images_folder = os.environ['IMAGES_FOLDER']
    Path(images_folder).mkdir(parents=True, exist_ok=True)
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{images_folder}/{filename}", 'wb') as file:
        file.write(response.content)

def get_extension(url):
    return os.path.splitext(url)[1]

def main():
    load_dotenv()
    

if __name__ == "__main__":
    main()