# black jack game
# las variables que voy a acupar
import random
cartjug1=random.randrange(1,11)
cartjug2=random.randrange(1,11)
cartadel1=random.randrange(1,11)
cartadel2=random.randrange(1,11)
cartfinaldel=cartadel1+cartadel2
cartafinaljug=cartjug1+cartjug2
score= 0

# el mero juego
print("You enter a tavern after traveling all day long in the sunny dry desert you orlder a drink and sit at the "
      "cornered table")
nombre= input("Someone sits next to you and says: hello fellow traver whats your name?" )
respuesta=input("care fora game of black jack?").lower()
while respuesta=="yes":
 print("your cards are: ",cartjug1,cartjug2)
 print("Dealers Cards are: ",cartadel1,"??")
 respuesta2 = input("Would you like another card? ").lower()
 while respuesta2 == "yes":
     cartafinaljug=cartafinaljug+random.randrange(1,11)
     print("the sum of your cards is: ",cartafinaljug)
     respuesta2=input("Would you like another card")
 if cartafinaljug > 21:
     print("The dealer has won you got busted")
     score= score - 5
     respuesta = input("do you want to play again")
 if cartfinaldel < 16:
    cartfinaldel = cartfinaldel + random.randrange(1 , 11)
 if cartfinaldel > 21:
     print ("you have won dealer got busted")
     score = score + 10
     respuesta = input("do you want to play again")
 if cartfinaldel == 21:
     print("the dealer has won he got a black jack")
     score = score - 5
     respuesta = input("do you want to play again")
 if cartfinaldel > cartafinaljug:
     print("The dealer has won hes got: ",cartfinaldel,"and you have: ",cartafinaljug)
     score = score-5
     respuesta = input("do you want to play again")
 if cartafinaljug > cartfinaldel:
     print("You have won you got: ",cartafinaljug,"and the dealer has: ",cartfinaldel)
     score=score + 10
     respuesta= input("do you want to play again").lower()


else:
 print("Thanks for playing with me",nombre)
 print("your score is:",score)