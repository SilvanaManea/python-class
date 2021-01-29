"""1) Creeaza un program care contorizeaza si afiseaza in terminal numarul de caractere al urmatoarelor cuvinte. Programul
trebuie sa contina cel putin o functie. 
Exemplu: "programare", "python", "eu stiu sa programez si imi place ceea ce fac", "sunt entuziasmat" """

sirCaractere = input("Introdu un sir de caractere: ")

def numar_caractere(sirCaractereF):
    contorCaractere = 0

    for char in sirCaractereF:
        contorCaractere += 1

    return contorCaractere

print("Numarul de caractere in sirul de caractere " + sirCaractere + " este " + str(numar_caractere(sirCaractere)))

#----------------------------------------------------------------------------------------------------------------------
"""2) Creeaza un program (care va contine o functie) care pentru orice numar (sau string) introdus va intoarce inversul 
acestuia. 
Exemplu: invers(1234)=>4321, invers(python)=>nohtyp"""

numar_sau_string = input("introdu un numar sau un string: ")

def invers(inputF):
    intors = inputF[::-1]
    return intors

print("Inversul lui " + numar_sau_string + " este " + invers(numar_sau_string))