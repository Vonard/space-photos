from download import download_image
from download import get_extension
from dotenv import load_dotenv
import requests
import os

def fetch_nasa_apod(api_key ):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": api_key,
               "count": 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()

    for index, picture in enumerate(pictures):
        if get_extension(picture["url"]):
            extension = get_extension(picture["url"])
            filename = f"nasa_{index}{extension}"
            download_image(picture["url"], filename)

def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_apod(api_key)

if __name__ == "__main__":
    main()
