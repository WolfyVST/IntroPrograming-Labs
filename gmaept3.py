from typing import List

places: List[str] = [" town hall-1 ", " park-2 ", " market place-3 ", " blacksmith-4 ", " Guild hall-5 ", " church-6 "]
LocNames = ["The Town hall", "the park","Marketplace","The blacksmith","The guild hall","the church"]
hasbeen = [False,False,False,False,False,False]

def costumization():
    print("")
    sex = input(" Are you female or male ").lower()
    charactersrace = input("Chose a race: Elf , Human , Dragonkin ").lower()
    weponcha = ""
    if charactersrace == "elf":
        weponcha = "staff"
    elif charactersrace == "human":
        weponcha = "Sword"
    elif charactersrace == "dragonkin":
        weponcha = "Metal globes"
    return sex, charactersrace, weponcha
def name():
    print(
        "You wake up in a dark cavern with a blank mind, wondering where you are you hear a voice coming towards you")
    chaname = input("Whats your name o fellow traveler")
    print()

    return chaname


def townhall(action ):
    print("we have arrived in the town hall look there are so many people")
    print("it is pretty nice maybe we can ask people about you and the cave")
    print("after asking a few people you and wolfy don't find anything.")
    if hasbeen[action] == False:
        score =  20
        goal = 1
        hasbeen[0] = True
        return score, goal
    else:
        score = 0
        goal = 0
    return score, goal
def park( action):
    print("we have arrived at the park it is verry calming lets rest while we are here")
    print("after a few hours you feel refreshed you got 10 points fo that ")
    if hasbeen[action] == False:
        score = 10
        hasbeen[1] = True

    else:
        score = 0
    return score
def marketplace(action ):
    print("we have arrived at the market place we can see if they have something to eat im starving Wolfy says!")
    print("after having a meal you feel full of energy ready to go somewhere else")
    if hasbeen[action] == False:
        score = 10
        hasbeen[2] = True
    else:
        score = 0
    return score
def blacksmith( action ):
    print("ohh look a black smith shop we should be able to get some new gear for you")
    print("after browsing for a while you get some new gear, wolfy: you look awsome!!")
    if hasbeen[action] == False:
        score =  20
        goal =  1
        hasbeen[3] = True
    else:
        score = 0
        goal = 0
    return score, goal
def guildhall( action):
    print("receptionist: welcome to the guild hall this is where you can find work for heroes")
    print("Wolfy we can sign up later but for the moment lets find what we need")
    if hasbeen[action] == False:
        score = 10
        hasbeen[4] = True
    else:
        score = 0
    return score
def church( action):
    print("hey there is a church here we can ask the sisters if we can spend the night here")
    print("After talking to the sisters they agreed to let us stay do thats awsome, anyway lets come here after we find the other things we need")
    if hasbeen[action] == False:
        score = 20
        goal = 1
        hasbeen[5] = True
    else:
        score = 0
        goal = 0
    return score , goal

def showpla(curLoc, score):
    print("Current Location: " + curLoc)
    print("Current Score: " + str(score))


def direct(race):
    chace = race
    direction = ""
    if chace == "elf":
        direction = "south"
    elif chace == "human":
        direction = "north"
    elif chace == "dragonkin":
        direction = "west"

    return direction


def main():
    score = 0
    customize = costumization()
    chaname = name()
    wepon = customize[2]
    charace = customize[1]
    playdirect = direct(charace)
    sexo = customize[0]
    result = False
    timer = 0
    print(
        "Hello " + chaname + " My name is Wolfy im a fox spirit traveling the world looking for the memory crystals, who are you and what are you doing in this cavern in the")
    print("You tell Wolfy that you have no idea where are you ")
    print(
        "Woly says ohh thats to bad first lets go near the town since your an " + charace + " we should go " + playdirect)
    print("lets get out of the cave I have a good feeling about metting you, you agree and with wolfy ")
    print("here take this ", wepon, " this would help you defend yourself")
    print()
    print("You have arrived at the and of tha cave succesfully thanks to the gidance of Wolfy")
    score = score + 10
    input("Press Enter to continue...")
    print(score, "for taking your first steps in the world")
    print(
        "In the middle of the way you found a group of slimes you have to decide what to do if atackthem or flee from them.")
    action = input("What would you do Atack or flee")
    if action == "atack":
        print("you have succesfuly defeated the slime group")
        score = score + 50
    else:
        print("you have succesfully flee from the slime group")
        score = score + 20
    print("your score after the action is", score)
    input("Press Enter to continue...")
    print(
        "you have finally arrived at the town, "+chaname+": finally here we are we need three things, find a place to stay, then find soome armor for you and also ask about the cave and see if someone knows who you are")
    print("this are the places we can go: ", places[0:6])
    go = input("are you ready to go ").lower()
    goal = 0
    while go == "yes":
        action2 = input("where should we go first? (select where to go by writing the number next to the place) ")
        plaaction = int(action2) - 1
        while plaaction < 0 :
            action2 = input("where should we go first? (select where to go by writing the number next to the place) ")
            plaaction = int(action2) - 1
        places2 = places[plaaction]
        showpla(LocNames[plaaction],score)
        if places2 == places[0]:

            #townhall(score, goal, plaaction)
            thres = townhall(plaaction)
            score = score + thres[0]
            goal = goal + thres[1]

        if places2 == places[1]:

            #park(score , plaaction)
            parkres = park(plaaction)
            score = score + parkres

        elif places2 == places[2]:

            markres = marketplace(plaaction)
            score = score + markres


        elif places2 == places[3]:

            blackres = blacksmith(plaaction)
            score = score + blackres[0]
            goal = goal + blackres[1]



        elif places2 == places[4]:

            guildres = guildhall(plaaction)
            score = score + guildres

        elif places2 == places[5]:

            churchres = church(plaaction)
            score = score + churchres[0]
            goal = goal + churchres[1]




        timer = timer + 1

        print(goal)
        if timer == 6 :
            if goal == 3:
                print("we have everything we should go to the church and rest")
                go = "no"
                result = True
            else:
                print("you have failed to secured a place!")
                go = "no"

    if result == True :
        print("You have won! Please play again!!")
    else:
        print("Game Over")

main()
