age = int(input("What is your age?")) 
student = str(input("Are you a student? Please answer yes or no"))
if age < 12 or age >= 65:
    print("Your ticket is £5.") 
elif student == "yes":
    print("Your ticket is £8.")
else:
    print("Your ticket is £10.")

