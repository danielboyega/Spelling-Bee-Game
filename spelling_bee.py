from get_word import get_word
from score import get_point_value

def spelling_bee():
  letters_input = input("Welcome to Spelling Bee! Enter your 7 letters, separated by commas: \n")
  letters = [letter.strip() for letter in letters_input.split(',')]

  while True:
    required_letter = input(f"Which of these 7 letters {letters} will be your required letter? \n").strip()
    if required_letter in letters:
      break
    else:
      print(f"{required_letter} is not an available letter. Please choose from the following: {letters}")
    
  used_words = []
  score = 0

  while True:
    word = get_word(letters, required_letter, used_words)
    if word == "END":
      print("Your final score is", score)
      break
        
    if required_letter not in word:
      print(f"Your word must contain the letter {required_letter}")
      continue

    if any(letter not in letters for letter in word):
      print(f"{word} is not a valid word. The only letters you can use are {letters}")
      continue

    used_words.append(word)
    points = get_point_value(word, letters)
    score += points

  if len(set(word)) == 7:
    print(f"{word} - Pangram!")
      
spelling_bee()