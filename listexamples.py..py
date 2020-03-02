colors = [""]
def showtitle():
    print("Color Preference Evaluator?")
def promptForColor():
    color = input(" Please enter a color").upper()
    return color
def confirmColor():
    confirm = promptForColor()
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
    pass
def rediculeUser():
    pass
def main():
    showtitle()

