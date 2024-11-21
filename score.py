from pangram import is_pangram
def get_point_value(word,letters):
  points = len(word)
  if is_pangram(word, letters):
    print(word, "- Pangram!")
    return points + 7
  else:
    print(word)
    return points