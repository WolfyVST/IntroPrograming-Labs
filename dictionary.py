#CMPT 120 Intro to Programming
# Project 4
# Author: Ricardo Villalobos
# Created: 4/25/2020
def main():
    print("Please enter finals name: ")
    filename = input()
    if filename == "dictionary":
        f = open("dictionary.txt", "r")
        print(f.readline())
        f.close()
main()