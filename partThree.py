import math

score = int(input(0,100))
if score < 60:
    print("F")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 90 and score <= 100:
    print("A")

elif score < 0 or score > 100:
    print("Invalid")