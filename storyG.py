#fantasy driven game
#variables
sword = 10
axe = 15
Daggers = 5
slime = 20
shodow = 50
playerlife = 100
DemondLord = 150
equipment = 0
#the main game
respuesta = input("Are you ready to start? ").lower()
while respuesta == "yes":
    print("you wake up in a cave, dark and glomy. when you start thinking about what just happen you hear a sound. "
          "Some says: Hello Great hero we need your help in the calamity that has been vestoud apon us."
          "You try to look for the person talking to you but found no one."
          "you ask who are you? it responds me Im Wolfy a spirit trapted in the castle, please great hero help me!"
          "you: Fine ill help you wolfy where should I go first? "
          "Wolfy: head north from here but first chose your wepon oh hero ")
    weapon = input("Chose your weapon oh grat hero, you can chose a Sword forged in the depths of a volcano, "
                   "An Axe coming from the scales of dragons and their power"
                   "and lastly the Dagger's of the best assasins past downs for generations").lower()
    if weapon == "sword":
        print("you have chose the sword great hero")
        equipment = sword
    if