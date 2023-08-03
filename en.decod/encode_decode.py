litters = ['a','b','c','d','e','f','g','h','i','j ','k','l','m','n',
          'o','p','q','r','s','t','u','v','w','x','y','z']
def caeser(cyber,text_need,num_shift):
        new_string= ""
        if cyber == "decode":
            num_shift*=-1           
        for x in text_need:
            if x in litters:
                position=litters.index(x)
                new_position = position+num_shift
                new_string+=litters[(new_position)%(len(litters))]
            else:
                new_string+=x
        print(f"the {cyber}d test is {new_string}")  
end = False
while not end:
    direction = input(" Enter type what yo do : 'encode' or 'decode':\n " ).lower()
    text = input("Enter the text: \n").lower()
    shift = int(input("Enter the number shift:\n "))
    caeser(cyber=direction,text_need=text,num_shift=shift)
    message = input("If you want to decrypt, press 'yes' and if not press 'no': ").lower()
    if message=="no":
        end = True
        print("GoodBay.")


       

