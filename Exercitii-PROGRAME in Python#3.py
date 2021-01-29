"""1)Creeaza un program care determina daca un numar (introdus de la tastatura) este par sau impar. Se va afisa (print) in
terminal un mesaj similar cu: "Numarul introdus X este par", in cazul in care nnumarul este par, iar "Numarul este impar",
in cazul in care numarul este impar."""

numar = int(input("Introdu un numar: "))

if numar % 2 == 0:
    print("Numarul este par.")
else:
    print("Numarul este impar.")

#----------------------------------------------------------------------------------------------------------------------

"""2)Creeaza un chestionar de intrebari pe care o persoana din departamentul de resurse umane le poate adresa la interviul
de angajare. Vor exista 5 intrebari (similare cu cele de mai jos) pe care le vei adresa persoanei care va rula programul
si care va putea sa le raspunda prin input sau de la tastatura. In timpul executiei programului, acesta stocheaza datele,
iar la sfarsitul acestor intrebari se vor afisa sub forma urmatoare: "Candidatul X, a raspun astfel la intrebarile de mai 
sus." 

Intrebarile: "Cum te numesti?", "Ce job iti doresti?", "In cat timp crezi ca poti obtine acest job", "Care sunt pasii pe 
care trebuie sa-i urmezi pentru a te putea angaja?", "De cand doresti sa incepi?" """

print("Chestionar de intrebari pentru angajare:\n")

print("Intrebare 1:")
intrebare1 = str(input("Cum te numesti?\n"))
print("\nIntrebare 2:")
intrebare2 = str(input("Ce job iti doresti?\n"))
print("\nIntrebare 3:")
intrebare3 = str(input("In cat timp crezi ca poti obtine acest job\n"))
print("\nIntrebare 4:")
intrebare4 = str(input("Care sunt pasii pe care trebuie sa-i urmezi pentru a te putea angaja?\n"))
print("\nIntrebare 5:")
intrebare5 = str(input("De cand doresti sa incepi?\n"))

print("Candidatul",intrebare1,",a raspuns astfel la intrebarile de mai sus:\n")
print("Intrebare1: ",intrebare1,"\nIntrebare2: ",intrebare2,"\nIntrebare3: ",intrebare3,"\nIntrebare4: ",intrebare4,"\nIntrebare5: ",intrebare5)


#----------------------------------------------------------------------------------------------------------------------
"""3)Creeaza un program care determina daca cuvantul (string) introdus de catre utilizator (de la tastatura) este 
Palindrom sau nu. Un palindrom este un sir de caractere care citit de la stanga la dreapta sau de la dreapta la stanga 
ramane neschimbat."""
#Varianta_1
def palindrom(cuvant):
    return cuvant == cuvant[::-1]

cuvant = str(input("Introduceti un cuvant: "))
rasp = palindrom(cuvant)

if(rasp):
    print("Cuvantul este palindrom.")
else:
    print("Cuvantul nu este palindrom.")

#Varianta_2
def palindrom(cuvant):
    invCuvant = ''.join(reversed(cuvant))

    if(cuvant == invCuvant):
        return True
    return False

cuvant = str(input("Introduceti un cuvant: "))
rasp = palindrom(cuvant)

if(rasp):
    print("Cuvantul este palindrom.")
else:
    print("Cuvantul nu este palindrom.")
