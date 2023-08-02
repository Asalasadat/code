import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
===lives======
''']
end_of_game = False
word_list = ["berry", "bananas","apples","coconuts","strawberry","grapes","kiwi","pineapple","avocado","cherry","fig"
             ,"orange","papaya","peash","pear","plum","watermelon","quince","raspberry","nectaine","lemon","blackcurrant"]
chosse_word = random.choice(word_list)
word_length = len(chosse_word)
lives = 6
display = []
for _ in range(word_length):
    display += "_"
while not end_of_game:
    guess = input("Guess a litter: ").lower()
    for position in range(word_length):
        litter = chosse_word[position]
        if litter == guess:
            display[position] = litter
    if guess not in chosse_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])