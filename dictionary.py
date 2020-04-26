#CMPT 120 Intro to Programming
# Project 4
# Author: Ricardo Villalobos
# Created: 4/25/2020
def main():
    print("Please enter file name: ")
    filename = input()
    if filename == "dictionary":
        band = True
        while band == True:
            with open("dictionary.txt", "r") as f:
                searchitem = input("Please enter the word your looking for: ")

                lines = f.readlines()
                flag = False

                for i in range(0 ,len(lines)) :
                    line = lines[i]
                    if searchitem == line.rstrip('\n') :
                        print(lines[i+1])
                        flag = True
                if flag == False:
                    print("Word not in the dictionary")
                if searchitem == "":
                    band = False
        f.close()
    else:
        print("Thank your for using the dictionary")
main()