import telegram
import os
import random
import time
import argparse
from dotenv import load_dotenv

def main():
    load_dotenv()
    images_folder = os.environ['IMAGES_FOLDER']
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(description="Launches the telegram bot, that sends pictures.")
    parser.add_argument("--timeout", help="Selects the time after which the bot starts sending pictures again.", type=int, default=14400)
    args = parser.parse_args()

    while True:
        for root,dirs,files in os.walk(images_folder):
            random.shuffle(files)
            for file in files:
                with open(f'{images_folder}/{file}', 'rb') as file:
                    bot.send_document(chat_id=chat_id, document=file)
                time.sleep(5)
        time.sleep(args.timeout)


if __name__ == "__main__":
    main()



