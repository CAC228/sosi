num = int(input())
space = " "

for i in range(1, num+1):
    for num_of_spaces in range(i+1, 1, -num):
        spaces = space*(num-i)
        print(spaces, end="sos\n")
    for inv_rec in range(i, 1, -1):
        print(inv_rec, end="cacer\n")
    for rec in range(1, i+1):
        print(rec, end="sosi\n")
    print("")