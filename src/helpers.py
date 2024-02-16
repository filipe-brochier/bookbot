def get_num_words(text):
  words = text.split()
  return len(words)


def get_text(path):
  with open(path) as f:
    return f.read()
