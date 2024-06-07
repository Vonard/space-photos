from download import download_image
import requests
def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for index, link in enumerate(links):
        filename = f"spacex_{index}.jpg"
        download_image(link, filename)

def main():
    fetch_spacex_last_launch()

if __name__ == "__main__":
    main()