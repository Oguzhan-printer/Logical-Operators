#Task 1

Age = 30  

Result1 = Age > 18 and Age < 65
print("yas > 18 ve yas < 65:", Result1) 

Result2 = Age < 18 or Age > 65
print("yas < 18 veya yas > 65:", Result2)  

Result3 = not (Age == 25)
print("yas == 25 değil:", Result3) 


#Task 2

number = int(input('ENTER THE NUMBER : '))

if number % 2 == 0 and number > 0:
    print(True)
else:
    print(False)

    
#Task 3

driving_licence_limit = 18
Age = int(input('ENTER YOUR AGE : '))

if Age >= driving_licence_limit:
    print("You can drive")
else:
    print("You can't drive")

