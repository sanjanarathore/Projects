phrase = input("enter a phrase (preferrably with parenthesis):")
alternate = []
for x in range(len(phrase)):
    if (x-1)%2 == 1:
        uppercase = phrase[x].upper()
    else:
        uppercase = phrase[x]
    alternate.append(uppercase)
joined = "".join(alternate)
print(joined)
vowel = ["A","E","I","O","U"]
for x in alternate:
    if x in vowel:
        ind = alternate.index(x)
        alternate[ind] = "*"
joined = "".join(alternate)
print(joined)

if alternate.count("(") == alternate.count(")"):
        print("Balanced? True")
else:
        print("Balanced? False")



