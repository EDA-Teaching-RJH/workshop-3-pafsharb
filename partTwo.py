import random

secret_number = random.randint(1, 10)
x = int(input("Guess a number."))
if x > 10:
   print("Too High.")
if x < 1:
   print("Too Low.")

else:
   print("Your number is within the range.")

