n = int(input("Enter an integer: "))
sum = 0

while(n):
    rem = n % 10
    sum = sum + rem
    n = n // 10

print(sum)
