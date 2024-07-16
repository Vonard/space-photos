from download import download_image
import requests
import argparse
from dotenv import load_dotenv
def fetch_spacex_last_launch(id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for index, link in enumerate(links):
        filename = f"spacex_{index}.jpg"
        download_image(link, filename)

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Download images from Spacex")
    parser.add_argument("--id_spacex", help="ID of the launch for SpaceX API", default="latest")
    args = parser.parse_args()
    fetch_spacex_last_launch(args.id_spacex)


if __name__ == "__main__":
    main()