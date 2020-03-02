colors = ["RED","BLUE","YELLOW"]
def showtitle():
    print("Color Preference Evaluator?")
def promptForColor():
    color = input(" Please enter a color").upper()
    return color
def confirmColor(confirm ):
    userconfirm = input("You have entered "+ confirm + " Is this correct (Y/N)").upper()
    if userconfirm == "Y":
        return True
def containsElement(colors2):
    it= 0
    for color in colors[it]:
        if colors2 == color :
            return True
        it = it + 1
    return False
def praiseUser():
    print("well done ")
def rediculeUser():
    print("what a terrible color!!")
def main():
    showtitle()
    ready = input("Are you ready?")
    while ready == "yes":
        color = promptForColor()
        cont=confirmColor(color)
        if cont == True:
            next = confirmColor(color)
            if next == True:
                praiseUser()
            else:
                rediculeUser()
    print("thanks for participating")

main()




