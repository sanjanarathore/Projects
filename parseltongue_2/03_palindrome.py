word = input("Enter a word or phrase:")
#word = word.replace(" ","")
bad = [".",",","?","!"," ",":"]
for char in word:
    if char in bad:
        word = word.replace(char,"")
word = word.lower()
index = len(word)//2
for x in range(index):
    if word[x] == word[-(x+1)]:
        ans = "yes"
    else:
        ans = "no"
        break
print("Is the input a palindrome?", ans)

