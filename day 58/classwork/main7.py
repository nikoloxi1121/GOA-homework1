# მომხმარებელს შემოატანინეთ თავისი ასაკი და შეამოწმეთ თუ მომხმარებლის
# ასაკი მეტია 5 ზე და ნაკლები 12 ზე დაუბეჭდეთ რომ არის ბავშვი , სხვა 
# შემთხვევაში თუ მომხმარებლის ასაკი არის 12 ზე მეტი და 18 ზე ნაკლები 
# დაუბეჭდეთ რომ არის თინეიჯერი და თუ არის 18 ზე მეტი დაუბეჭდეთ რომ არის ზრდასრული

age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if 5 < age < 12:
    print("თქვენი ასაკი არის ბავშვი")
elif 12 <= age < 18:
    print("თქვენი ასაკი არის თინეიჯერი")
elif age >= 18:
    print("თქვენი ასაკი არის ზრდასრული")
else:
    print("თქვენი ასაკი არ შეესაბამება არსებულ კატეგორიას")