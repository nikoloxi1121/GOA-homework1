# მომხმარებელს შემოატანინეთ 1 დან 7-ის ჩათვლით რომელიმე 
# რიცხვი ამის შემდეგ კი გამოიყენეთ if elif else რომ შეუსაბამოდ
# კვირის დღე 1 ორშაბათისთვის 2 სამშაბათისთვის 3 ოთხშაბათისთვის და ასე 

number = int(input("shemoitane ricxvi 1-7 is chatvlit: "))

if number == 1:
    print("orshabati")
elif number == 2:
    print("samshabati")
elif number == 3:
    print("otxshabati")
elif number == 4:
    print("xutshabati")
elif number == 5:
    print("paraskevi")
elif number == 6:
    print("shabati")
elif number == 7:
    print("kvira")
else:
    print("sheiyvane ricxvi 1-7 mde!")