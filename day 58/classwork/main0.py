# შექმენით პროგრამა სადაც მომხმარებელი შემოიტანს 5 რციხვს, ხოლო ამ 5
# რიცხვს შორის გამოიყენეთ ყველა არითმეტიკული ოპერაცია (+,-,*,/,%,//), 
# საბოლოოდ დაბეჭდეთ შედეგები ტერმინალში + ახსენით თითოეული ნაწილი 
# კოდის რატომ დაწერეთ კონკრეტული ხაზი და რას აკეთებს.

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2

print(f"შეყვანილი რიცხვების დამატება: {addition}")
print(f"შეყვანილი რიცხვების შემცირება: {subtraction}")
print(f"შეყვანილი რიცხვების გამრავლება: {multiplication}")
print(f"შეყვანილი რიცხვების გაყოფა: {division}")
print(f"შეყვანილი რიცხვების ნარჩენი: {modulus}")