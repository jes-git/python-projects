import random

words=["good", "simple","dialogue","blue"]
chosen_word=random.choice(words)
word_display=["_" for _ in chosen_word]
attempts=8
print("Welcome to Hangaman")

while attempts > 0 and '_' in word_display:
    print("\n"+" ".join(word_display))
    guess=input("Enter a letter:").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter ==guess:
                word_display[index]=guess
    else:
        print("Letter not in word")
        attempts-=1
if '_' not in word_display:
    print("You guessed the word!")
    print(''.join(word_display))
    print('You survived!')

else:
    print("You ran out of attempts.")
    print("The word was "+chosen_word)