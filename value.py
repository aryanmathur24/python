n = int(input("please enter then no. you want to getr the ascii value"))
main_string = ''
for i in range(n):
    num = int(input('enter a number between 50-100 for its ascii value:'))
    str=chr(num)
    main_string = str + main_string
print (main_string)

