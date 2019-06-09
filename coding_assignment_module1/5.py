st = input("Enter a string: ")
n = len(st)

flag = 0

for i in st:
    if not i.isdigit():
        flag = 1

if(flag):
    print("The string is not numeric")
else:
    print("The string is numeric")
