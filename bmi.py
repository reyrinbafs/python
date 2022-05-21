weight = int(input("Enter weight in kg: "))
height = int(input("Enter height in  cm: "))
bmi = weight / (height/100)**2
if  bmi <= 18.4 :
    print("you are underweight.")
elif  bmi <= 24.9 :
    print("you are normal weight.")
elif  bmi <= 29.9 :
    print("you are over weight.")
elif  bmi <= 34.9 :
    print("you are obesity.")
else:
    print("You are severely obese.")