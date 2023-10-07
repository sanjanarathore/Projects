import time
import random
cats = ["names", "candies", "drinks", "colors", "states"]
n = random.choice(cats)
print("The category is", n + ".", "Enter 10 items in this catagory.")
items = []
for x in range(10):
    entered = input("enter:")
    items.append(entered)
neat = ", ".join(items)
import os
width = os.get_terminal_size().columns
print(neat.center(width))
print("It took you", time.perf_counter(), "seconds to enter 10 items in this category.   ")