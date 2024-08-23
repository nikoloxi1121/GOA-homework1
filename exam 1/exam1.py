# 1.create account
# 2.Deposit
# 3.Withdraw
# 4.Exit
# თქვენი დავალება იქნება გააკეთოთ ბანკის სისტემა მოცემული სექციებით
# პითონში,რაც აქამდე ისწავლეთ გააკეთეთ იმ მასალით გამოიყენეთ თქვენი
# მაქსიმალური ცოდნა,მერე კი ჩვენ შევამოწმეთ თუ რა დონის ცოდნა გამოიყენეთ და იმის მიხედვით შეიგიმოწმებთ!!!

def create_account():
    print("welcome to GOA Bank!")
    username = input("enter username: ")
    password = input("enter password: ")
    print(f"hello {username}, your account was created succesfully")
create_account()

def deposit_withdraw():
    balance = (0)
    question = input("do you want to deposit money?: ")
    if question == "yes":
        amount = int(input("enter the amount: "))
        if amount > 0:
            balance += amount
            print("amount successfully added to balance!")
        else:
            print("error")
    else:
        print("")

    question = input("do you want to withdraw money?: ")
    if question == "yes":
        amount = int(input("enter the amount: "))
        if amount > 0:
            balance -= amount
            print("amount successfully withdrawed from your balance!")
        else:
            print("error")
    else:
        print("")
    question2 = input("do you want to see your balance?: ")

    if question2 == "yes":
        print(f"your balance is {balance}$")
    else:
        print("okay no problem")

deposit_withdraw()