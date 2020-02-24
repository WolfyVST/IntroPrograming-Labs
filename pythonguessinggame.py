guess = "penguin"
print("Hello ready to play a guessing game?")
print("Try guessing the animal, the animal is know to be a flyles bird livin in cold areas!")
awnser1 = input("ready?").lower()
while awnser1 == "yes" :
    awnser2 = input("whats your guess?").lower()
    if awnser2[0] == "q":
       awnser1 = "no"
    elif awnser2 == guess :
        print("well done, your a genius thanks for playing")
        awnser1 = "no"
    else:
        print("Good guess but it is incorrect :( another hint is that they live in the south pole")