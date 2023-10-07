import random
words = ["water", "mouse", "salad", "mouth", "ruler", "happy"]
chosen = random.choice(words).upper()
#print(chosen)
first = chosen[0].upper()
print("The secret word begins with", first + ".")
n = 1
while n <= 10:
    guessed = str(input("Guess:")).upper()
    if guessed == "":
        print("You have wasted a guess =P")
        n = n + 1
        continue
    elif len(guessed) != 5:
        print("0, 1, 2, 3, 4 that's how we count to five!")
        n = n + 1
        continue
    elif guessed[0] != first:
        print("ABCDEFGHIJKLMNOPQRSTVUVWXYZ")
        continue
    elif guessed == chosen:
        print("Good Job! You are one with the Source")
        break
    else:
        print("You have", 10-n, "guesses left!")
        n = n + 1