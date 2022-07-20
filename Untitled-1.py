n = input("enter any string")
st1 = n.lower()
dict = {}
for i in st1: 
    if i in dict:
        dict[i] += 1
    else :
        dict[i] = 1
print(dict)
