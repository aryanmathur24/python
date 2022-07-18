n = int(input("Please enter a no."))
for i in range(n):
    op = input('Please enter the operation string')
    op_list = op.split()
    print(op_list)
    if op_list[0] == 'add':
        first_number = int (op_list[1])
        second_number = int (op_list[2])
        print(first_number + second_number)
    elif op_list[0] == 'sub':
        first_number = int (op_list[1])
        second_number = int (op_list[2])
        print(first_number - second_number)
    elif op_list[0] == 'multiplication':
        first_number = int (op_list[1])
        second_number = int (op_list[2])
        print(first_number * second_number)
    elif op_list[0] == 'division':
        first_number = int (op_list[1])
        second_number = int (op_list[2])
        print(first_number + second_number)
