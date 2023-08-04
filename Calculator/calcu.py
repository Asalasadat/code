def add(n1,n2):
    return n1+n2

def subtrct(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations={
    '+':add,
    '-':subtrct,
    '*':multiply,
    '/':divide
}
def calcu():
    num1=float(input("What is the first number? "))


    for symble in operations:
        print(symble)

    end = True

    while end:
        
        num2=float(input("What is the last number? "))

        opa=input("pick an operation: ")

        calculator_fun=operations[opa]

        answer=calculator_fun(num1,num2)

        print(f"{num1} {opa} {num2} = {answer}")

        flag = input(f"Enter if you want continue with {answer} press 'Y' OR press 'A' to start again: ").lower()
        if flag=='y':
            num1=answer
        elif flag=='a':
            end = False
            calcu()

calcu()            

      









#------------------------------------(another way)----------------------------------
def calculator(first_number,operations,last_number):
    if operations=='-':
        result = first_number-last_number
        print(f"{first_number} {operations} {last_number} = {result}")
    elif operations=='+':  
        result = first_number+last_number
        print(f"{first_number} {operations} {last_number} = {result}")  
    elif operations=='/':  
        result = first_number/last_number
        print(f"{first_number} {operations} {last_number} = {result}")
    elif operations=='*':  
        result = first_number*last_number
        print(f"{first_number} {operations} {last_number} = {result}")    
    flag = input(f"Enter if you want continue with {result} press 'Y' OR press 'A' to start again: ").lower()
    if flag=='y':
        calculator(result,input("pick an operation: "),int(input("Enter the number: ")))  
    elif flag=='a':
        calculator(int(input("What is the first number? ")),input("pick an operation: "),int(input("What is the last number? "))) 

first = int(input("What is the first number? "))
op = input("pick an operation: ")
last = int(input("What is the last number? "))
calculator(first,op,last)   