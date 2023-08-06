import random
def GUESS():
    print("Welcome to the number guessing game! ")
    flag = input("Choose whether you want a 'hard' or 'easy' game: ")
    rand_number = random.randint(1,100)
    print(f"the number this: {rand_number}")
    if flag=="hard":
        print('You have 5 chances')
        i=5
        while i>0:
            num_you_choose = int(input("Enter the number you choose: "))
            if rand_number==num_you_choose :
                print(f"You got it! the answer was {num_you_choose}")
                break
            else:
                print ("Wrong Answer! , you have a {i-1}")
                i-=1
                if rand_number>num_you_choose>rand_number-5:
                    print("You are close to the answer.")
                else:
                    print("The answer is far away from your choice.")
    elif flag=="easy":
        print('You have 10 chances')
        i=10
        while i>0:
            num_you_choose = int(input("Enter the number you choose: "))
            if rand_number==num_you_choose :
                print(f"You got it! the answer was {num_you_choose}")
                break
            else:
                i-=1
                print (f"Wrong Answer! , you have a {i}")
                if rand_number+5>num_you_choose>rand_number-5:
                    print("You are close to the answer.")
                else:
                    print("The answer is far away from your choice.")

            
GUESS()