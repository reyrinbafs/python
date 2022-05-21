import random
n=int(input("Enter length of the password: "))
pass_data = "qwertyuiopasdfgjklzxcvbnm1234567890[];',./!@#$%^&*()_+:<>?"
p="".join(random.sample(pass_data,n))
print(p)
