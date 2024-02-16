from src.helpers import get_text, get_num_words, get_chars_dict
from dotenv import load_dotenv
from os import getenv

def main():
  load_dotenv()
  book_path = getenv('BOOK_PATH')
  text = get_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)

  print(chars_dict)

main()
