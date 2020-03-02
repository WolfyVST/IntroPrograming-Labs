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
def containsElement(it):
    for color in colors[]:
        if it == color :
            return True
    return False
def praiseUser():
    pass
def rediculeUser():
    pass
def main():
    it = 0
    showtitle()
