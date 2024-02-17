def get_num_words(text):
  words = text.split()
  return len(words)


def get_text(path):
  with open(path) as f:
    return f.read()


def get_chars_dict(text):
  letter_dict = {}
  for letter in text:
    if letter.isalpha():
      lowered = letter.lower()
      if lowered in letter_dict:
        letter_dict[lowered] += 1
      else:
        letter_dict[lowered] = 1
  return letter_dict

def sort_on(dict):
  return dict["num"]

def print_report(letter_dict, num_words, book_path):
  characters = [{'kind': k, 'num': v} for k, v in letter_dict.items()]
  characters.sort(reverse=True, key=sort_on)

  print(f"--- Begin report of {book_path} ---")
  print(f"{num_words} words found in the document\n\n\n")

  for character in characters:
    print(f"The '{character['kind']}' character was found {character['num']} times")
