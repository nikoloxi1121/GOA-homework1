list = []
More = []
Less = []

for i in range(10):
    number = int(input("please enter a number: "))
    if number == 100:
        continue
    elif number < 100:
        Less.append(number)
    else:
        More.append(number)
print("these numbers are greater that 100", More)
print("these numbers are less that 100", Less)
