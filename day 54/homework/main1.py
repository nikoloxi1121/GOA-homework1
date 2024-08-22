# შექმენით ფუნქცია რომელიც შეეკითხება მომხარებელს რიცხვს და დააბრუნებს ლუწია თუ კენტი

def question():
    num = input("Enter the first number: ")
    if num % 2 == 0:
        print("your number is even")
    else:
        print("your number is odd")
        
question()