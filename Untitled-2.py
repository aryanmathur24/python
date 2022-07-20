# n=input("enter the key you want to know the string:")
# def hh(n):
#     for i in n:
#         if i==i.upper():
#          return ("True")
#          break
#     else :
#         return ("False")
# output = hh(n)
# print(output)

# m= input("enter the string:")
# def ordo (m):
#     sum=0
#     for i in m:
#         sum+= ord(i)
#     return sum 
# print(ordo(m))

# user=input('enter the username')
# password = input ('enter the password')
# def generate_password (username, password):
#     str1 = user[0:4] + password[-4:]
#     print(str1)
# generate_password(user, password)

# user = input('enter the character:')
# def gef (user):
#     count=0
#     for i in range(0,len(user)):
#         for j in range(1,len (user)):
#             if ord(user[i]) == (ord(user[j])-1):
#                 count += 1
#     print(count) 
# gef(user)

num = [1,2,3,4,5,6,7,8]
def p(num):
    for i in num:
        if (i% 2  == 0):
            print(i)
        else: 
            print("odd")
p(num)
    
    
    
