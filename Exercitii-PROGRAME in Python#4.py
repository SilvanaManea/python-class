"""1.1) Calculati suma tuturor numerelor de la 1 la 100. Creati o varianta a programului folosind bucle for, iar alta
varianta folosind bucle while. Afisati rezultatul pe ecran intr-un format precum: "Suma numerelor de la A la Z este..."."""

#Varianta cu for
suma = 0
for i in range(1, 101):
   suma = suma + i
print("Suma numerelor de la 1 la 100 este",suma)

#Varianta cu while
suma = 0
i = 1
while(i<=100):
   suma = suma + i
   i +=1
print("Suma numerelor de la 1 la 100 este",suma)

#----------------------------------------------------------------------------------------------------------------------
"""1.2) dinamizati programul prin adaugarea optiunii de introducere a celor doua numere(nr. de inceput si cel de sfarsit)
de la tastatura."""

#Varianta cu for
suma = 0
i = int(input("Introduce numarul de inceput: "))
z = int(input("Introduce numarul de sfarsit: "))
for i in range(i, z):
   suma = suma + i
print("Suma numerelor de la 1 la 100 este",suma)

#Varianta cu while
suma = 0
i = int(input("Introduce numarul de inceput: "))
z = int(input("Introduce numarul de sfarsit: "))
while(i<=z):
   suma = suma + i
   i +=1
print("Suma numerelor de la 1 la 100 este",suma)

#----------------------------------------------------------------------------------------------------------------------
"""2) Creati un joc Hartie-Foarfeca-Piatra la care sa participe 2 persoane.(Nota: folositi-va de functia "input()" pentru
a cere date de la jucatori; in momentul cand cineva satiga, printati un mesaj de felicitari si intrebati utilizatorii daca
sa inceapa un joc nou.)"""
from random import randint

#create a list of playoptions
t = ["Rock", "Paper", "Scrissors"]

#assing  a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
   player = input("Rock, Paper, Scrissors?: ")
   if player == computer:
      print("Tie")
   elif player == "Rock":
      if computer == "Paper":
         print("You lose!",computer,"convers",player)
      else:
         print("You win!",player,"smashes",computer)
   elif player == "Paper":
      if computer == "Scrissors":
         print("You lose!",computer,"cut",player)
      else:
         print("You win!",player,"covers",computer)
   elif player == "Scrissors":
      if computer == "Rock":
         print("You lose!",computer,"smashes",player)
      else:
         print("You win!",player,"cut",computer)
   else:
      print("That's not a valid play. Check your spelling!")
   #player was set to True, but we want it to be False so the loop continues
   player = False
   computer = t[randint(0,2)]