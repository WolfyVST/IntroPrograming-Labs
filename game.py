# black jack game
# las variables que voy a acupar
import random
cartjug1=random.randrange(1,11)
cartjug2=random.randrange(1,11)
cartadel1=random.randrange(1,11)
cartadel2=random.randrange(1,11)
cartfinaldel=cartadel1+cartadel2
cartafinaljug=cartjug1+cartjug2

#cards = []
#cards.append(4)
#sum(cards)

# el mero juego
respuesta=input("Do you want to play baclk jack ").lower()
while respuesta=="yes":
 print("sus cartas son",cartjug1,cartjug2)
 print("las cartas del dealer son:",cartadel1,"??")
 respuesta2 = input("Would you like another card?").lower()
 while respuesta2 == "yes":
     cartafinaljug=cartafinaljug+random.randrange(1,11)
     print("la suma de sus cartas es",cartafinaljug)
     respuesta2=input("Would you like another card")
 if cartafinaljug > 21:
     print("The dealer has won you got busted")
     respuesta="no"
 if cartfinaldel < 16:
   cartfinaldel = cartfinaldel + random.randrange(1 , 11)
 if cartfinaldel > 21:
     print ("you have won dealer got busted")
     respuesta="no"
 if cartfinaldel == 21:
     print("the dealer has won he got a black jack")
     respuesta="no"
 if cartfinaldel > cartafinaljug:
     print("The dealer has won hes got: ",cartfinaldel,"and you have: ",cartafinaljug)
     respuesta="no"
 if cartafinaljug > cartfinaldel:
     print("You have won you got: ",cartafinaljug,"and the dealer has: ",cartfinaldel)
     respuesta="no"
else:
 print("thanks for playing")
