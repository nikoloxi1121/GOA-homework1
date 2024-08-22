# შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და დააბრუნებს მათ ჯამს

def sum_two_numbers():
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    total = int(num1) + int(num2)

    return(total)

sum_two_numbers()