def is_valid_word(word, letters, required_letter, used_words):
  if word == "END":
    return True
  if len(word)<4:
    print("Your word must be at least 4 letters long")
    return False
  if required_letter not in word:
    print("Your word must contain the letter", required_letter)
    return False
  for letter in word:
    if letter not in letters:
      print(letter, "is not a letter you can use. The only letters you can use are", letters)
      return False
  if word in used_words:
    print("Already used")
    return False
  
  return True