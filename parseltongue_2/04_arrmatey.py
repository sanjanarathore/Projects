enter = input("Enter a sentence:")
array  = enter.split()
#print(array)
for x in array:
    ind = str(array.index(x))
    print("Argv of", ind, "is", x)


array = sorted(array, key = lambda x:len(x), reverse=True)
for x in array:
    print(x)

