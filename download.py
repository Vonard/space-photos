import os
import requests
from pathlib import Path
from urllib.parse import urlparse
from dotenv import load_dotenv

def download_image(url, images_folder, filename, api_key = ""):
    Path(images_folder).mkdir(parents=True, exist_ok=True)
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{images_folder}/{filename}", 'wb') as file:
        file.write(response.content)

def get_extension(url):
    return os.path.splitext(url)[1]
