from src.helpers import get_text, get_num_words
from dotenv import load_dotenv
from os import getenv

def main():
  load_dotenv()
  book_path = getenv('BOOK_PATH')
  text = get_text(book_path)
  num_words = get_num_words(text)

main()
