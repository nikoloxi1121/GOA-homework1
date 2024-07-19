# მოიფიქრეთ რამე ამოცანა და დაწერეთ ამოცანის კოდი

limit = int(input("Enter a number: "))

sum_even = 0
num = 2  

while num <= limit:
    sum_even += num
    num += 2  

print(f"The sum of all even numbers from 1 to {limit} is: {sum_even}")