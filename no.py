n = int(input("please enter then no."))
sum = 0
mul = 1
for i in range(n):
    op = input('Please enter the operation string')
    op_list = op.split()
    print(op_list)
    
    if op_list[0] == 'add':
        for j in range(1,len(op_list)):
            sum = sum + int(op_list[j])
        print(sum)
    if op_list[0] == 'mul':
        for j in range(1,len(op_list)):
            mul = mul * int(op_list[j])
        print(mul)    



