#CMPT 120 Intro to Programming
# Project 4
# Author: Ricardo Villalobos
# Created: 4/25/2020
def main():
    print("Please enter finals name: ")
    filename = input()
    if filename == "dictionary":
        with open("dictionary.txt", "r") as f:
            searchitem = input("Please enter the word your looking for: ")
            lines = f.readlines()
            for i in range(0 ,len(lines)):
                line = lines[i]
                if searchitem == line.rstrip('\n') :
                    print(lines[i+1])
    f.close()
    else:
        print()
main()