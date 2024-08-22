def print_min_max(numbers):
    if len(numbers) == 0:
        print("სია ცარიელია.")
        return
    
    min_number = numbers[0]
    max_number = numbers[0]
    
    for number in numbers:
        if number < min_number:
            min_number = number
        if number > max_number:
            max_number = number
    
    print(f"მინიმალური რიცხვი: {min_number}")
    print(f"მაქსიმალური რიცხვი: {max_number}")

numbers_list = [4, 2, 9, 11, -3, 7]
print_min_max(numbers_list)