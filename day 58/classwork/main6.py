# შექმენით ისეთი while ციკლი რომელიც 0 დან 10 ის ჩათვლით დაბეჭდავს 
# ყველა რიცხვს და if else  გამოყენებით გაიგეთ არის თუ არა ლუწი ან კენტი
# დასერჩეთ how to know if number is even or odd in python

number = 0

while number <= 10:
    if number % 2 == 0:
        print(f"{number} არის ლუწი")
    else:
        print(f"{number} არის კენტი")
    
    number += 1