# შექმენით ორი სია ერთში თქვენი ხელით ჩაწერეთ ლუწი რიცხვები,
# მეორეში კენტი რიცხვები შემდეგ კი ეს ორი სია გააერთიანეთ extend ის გამოყენებით 

mixed_numbers = [2, 7, 4, 1, 6, 9, 8, 3, 10, 5]

even_numbers = []
odd_numbers = []

for i in mixed_numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

even_numbers.extend(odd_numbers)

print("esxtended list", even_numbers)
