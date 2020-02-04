# black jack game
# las variables que voy a acupar
import random
cartjug1=random.randrange(1,11)
cartjug2=random.randrange(1,11)
cartadel1=random.randrange(1,11)
cartadel2=random.randrange(1,11)
cartfinaldel=cartadel1+cartadel2
cartafinaljug=cartjug1+cartjug2
respuesta=input("Do you want to play baclk jack ")
# el mero juego
if respuesta=="yes"or respuesta=="Yes":
 print("sus cartas son",cartjug1,cartjug2)
 print("las cartas del dealer son:",cartadel1,"??")
 if cartfinaldel>21:

 if cartfinaldel==21:
     print"You lost the deler has won the game he got a Black jack"
 else:

else:
    print("thanks for playing")
