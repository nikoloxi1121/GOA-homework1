# Enter a number to the user and then using a for loop output the sum of all the numbers up to this number
# (for example, if he enters 10, output the sum of all the numbers up to 10, for example).
sum = 0
num = int(input("enter random number: "))
for i in range(num):
    sum += i
print(sum)