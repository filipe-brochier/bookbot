from src import config
from dotenv import load_dotenv
from os import getenv

def main():
  config.get_config()
  load_dotenv()
  print(getenv("BOOK_PATH"))


main()
