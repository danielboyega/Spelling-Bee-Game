def is_pangram(guess, letters):
  for letter in letters:
    if  letter not in guess:
      return False
  return True