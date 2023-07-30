weight = float(input("Enter the number of Weight: "))
hight = float(input("Enter the number of hight: "))
bmi = round( weight / hight**2)
if bmi<18.5 :
    print(f"{bmi} , Under Weight ")
elif 25>bmi:
    print(f"{bmi} , Normal weight")
elif 30>bmi:
    print(f"{bmi} , Over weight")
elif 35>bmi:
    print(f"{bmi} , Obese") 
else:
    print(f"{bmi} , clinically obese")       