import telegram
import os
import random
import time
import argparse
from dotenv import load_dotenv

def main():
    load_dotenv()
    images_folder = os.environ['IMAGES_FOLDER']
    bot = telegram.Bot(token="7245572263:AAHRGAQE3v8EN4wUvTiKiLONyTiYiCBHLJI")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--timeout", help="", type=int, default=14400)
    args = parser.parse_args()

    while True:
        for root,dirs,files in os.walk(images_folder):
            random.shuffle(files)
            for file in files:
                bot.send_document(chat_id="@space_photos0", document=open(f'{images_folder}/{file}', 'rb'))
                time.sleep(5)
        time.sleep(args.timeout)


if __name__ == "__main__":
    main()



