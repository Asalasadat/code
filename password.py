import random
letters = ['A','B' , 'C' , 'D','E','F','J','K','L','M',
         'N','O','P','Q','R','S','T','U','V','W','X','Y',
         'Z','a','b','c','d','e','f','j','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']
num_letters = int(input("Enter the number of letters: "))
num_numbets = int(input("Enter the number of number: "))
num_symbols = int(input("Enter the number of symbols: "))
password = []
for char in range(1,num_letters+1):
    password.append(random.choice(letters))
for char in range(1,num_numbets+1):
    password.append(random.choice(numbers))
for char in range(1,num_symbols+1):
    password.append(random.choice(symbols))  
PASSWORD=""   
random.shuffle(password)
for test in password:
    PASSWORD+=test
print(PASSWORD) 