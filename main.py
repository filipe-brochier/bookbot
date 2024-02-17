from src.helpers import get_text, get_chars_dict, get_num_words, print_report
from dotenv import load_dotenv
from os import getenv

def main():
  load_dotenv()
  book_path = getenv('BOOK_PATH')
  text = get_text(book_path)
  num_words = get_num_words(text)
  chars_dict = get_chars_dict(text)

  print_report(chars_dict, num_words, book_path)

main()
