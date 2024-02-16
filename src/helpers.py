def get_num_words(text):
  words = text.split()
  return len(words)


def get_text(path):
  with open(path) as f:
    return f.read()


def get_chars_dict(text):
  letter_dict = {}
  for letter in text:
    lowered = letter.lower()
    if lowered in letter_dict:
      letter_dict[lowered] += 1
    else:
      letter_dict[lowered] = 1
  return letter_dict

