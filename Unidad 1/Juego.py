import random
import os

def run():

    images = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

    DB = [
        "PHYTON",
        "NOJALAPROFE",
        "JAVA",
        "PHP"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("cls")
        for character in spaces:
            print(character, end=" ")
        print(images[attemps])    
        letter = input("Elige una letra")

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found == True

        if not found:
            attemps -= 1

        if "_" not in spaces:
            os.system("cls")
            print("Felicidades Ganaste!!!")
            break
            input()

        if attemps == 0:
            os.system("cls")
            print("Perdiste weon")
            break


if __name__ == '__main__':
    run()
