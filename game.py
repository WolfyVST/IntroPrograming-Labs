# black jack game
# las variables que voy a acupar
import random
cartjug1=random.randrange(1,11)
cartjug2=random.randrange(1,11)
cartadel1=random.randrange(1,11)
cartadel2=random.randrange(1,11)
cartfinaldel=cartadel1+cartadel2
cartafinaljug=cartjug1+cartjug2
# el mero juego
respuesta=input("Do you want to play baclk jack ")
if respuesta=="yes"or respuesta=="Yes":
 print("sus cartas son",cartjug1,cartjug2)
 print("las cartas del dealer son:",cartadel1,"??")
 respuesta2 = input("Would you like another card?")
 if respuesta2 =="yes" or respuesta2=="Yes":
     cartafinaljug=cartafinaljug+random.randrange(1,11)
     print("la suma de sus cartas es",cartafinaljug)

 if cartfinaldel>21:
     print("you have won dealer got busted")
 if cartfinaldel==21:
     print("the dealer has won he got a black jack")


else:
    print("thanks for playing")
