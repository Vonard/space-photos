from download import download_image
from dotenv import load_dotenv
import requests
import os

def fetch_nasa_epic(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pictures = response.json()
    for index, picture in enumerate(pictures):
        date = pictures[index]["date"].split(" ")[0].split("-")
        epic_url = f"https://api.nasa.gov/EPIC/archive/natural/{date[0]}/{date[1]}/{date[2]}/png/{pictures[index]['image']}.png"
        download_image(epic_url, f"epic_{index}.png", api_key)

def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']
    fetch_nasa_epic(api_key )

if __name__ == "__main__":
    main()