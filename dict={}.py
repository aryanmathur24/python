dict={}
while True:
    a=input()
    b=a.split()
    if(b[0]=='stop'):
        break
    if(b[0] in dict):
        dict[b[0]]= dict[b[0]].union({b[1]})
        print(dict)
    else:
        dict[b[0]]={b[1]}
        print(dict)
print(dict)
