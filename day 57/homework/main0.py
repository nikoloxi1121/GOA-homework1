print("Hello, World!")


user_input = input("Enter something: ")
print("You entered:", user_input)


print("Hello with comments!")


def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

greet("Alice")


long_string = "This is a long string that we " \
              "are splitting across multiple lines."
print(long_string)



x = 10

print(x)

def add_numbers(a, b):
    """
    This function takes two numbers, adds them together,
    and returns the result.
    """
    return a + b

print(True, False)

a, b = True, False; print(a and b, a or b, not a)



print(5 > 3, 5 == 3, 5 != 3)

condition = True; print("Condition is True") if condition else print("Condition is False")

def is_even(num): return num % 2 == 0; print(is_even(4))

x, y = 10, 5; print(x + y, x - y, x * y, x / y, x % y)

x = 10; x += 5; print(x)

print(10 > 5, 10 < 5, 10 == 10, 10 != 5)

a, b = True, False; print(a and b, a or b, not a)

a, b = [1, 2], [1, 2]; print(a is b, a is not b)

my_list = [1, 2, 3]; print(my_list)

my_list = [1, 2]; my_list.append(3); my_list.remove(2); print(my_list)

my_list = [3, 1, 2]; my_list.sort(); print(my_list)

squares = [x ** 2 for x in range(5)]; print(squares)

my_list = [1, 2, 3]; print(len(my_list))

x = 10; 
if x > 5: print("x is greater than 5")



x = 4; print("x is even") if x % 2 == 0 else print("x is odd")

x = 15; print("x is negative") 

x = 10;



x = 7; result = "Even" if x % 2 == 0 else "Odd"; print(result)

i = 0;
while i < 3: print(i); i += 1

i = 0; 
while True: print(i); 
if i == 2:
    i += 1



i = 0; 
while i < 3: i += 1; 
if i == 2: print(i)

