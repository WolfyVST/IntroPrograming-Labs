guess = "lion"
print("Hello ready to play a guessing game?")
print("Try guessing the animal, the animal is know as the king of the jungle!")
awnser1 = input("ready?").lower()
while awnser1 == "yes" :
    awnser2 = input("whats your guess?").lower()
    if awnser2== "quit":
        awnser1 = "no"
    elif awnser2 == guess :
        print("well done, your a genius thanks for playing")
        awnser1 = "no"
    else:
        print("Good guess but it is incorrect :( another hint is that the animal has a huge mane")