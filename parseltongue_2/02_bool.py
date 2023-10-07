a = [False,True,True,None,True,None,None,False,False,None,True,False]
b = ["or","or","or","==","!=","==","and","==","!=","and","==","or"]
c = [False,False,None,None,True,True,False,True,None,False,True,None]
ls = []
x = 0
for y in a:
    expression = str(a[x]) + " " + b[x] + " " + str(c[x])
    ls.append(expression)
    x = x+1
#print(ls)
#print(ls[0])
#print(type(bool(ls[0])))

#print(type(False or False)) 
for y in ls:
    m = str(eval(y))
    #print(m)
    print(y, "=>", m)
