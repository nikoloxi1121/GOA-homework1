# Write an if-else statement that prints "Good morning!" if the current hour is less than 12 and "Good afternoon!" otherwise.
from datetime import datetime

current_hour = datetime.now().hour

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")