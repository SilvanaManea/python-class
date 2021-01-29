lista = []

with open("D:\Ramon Nastase - Platforma IT\PYTHON\fisier1.txt") as f1:
    for linie1 in f1: 
        linie1 = linie1.strip()
        lista.append(int(linie1))
f1.close()

with open("D:\Ramon Nastase - Platforma IT\PYTHON\fisier2.txt") as f2:
    for linie2 in f2: 
        linie2 = linie2.strip()
        lista.append(int(linie2))
f2.close()

with open("D:\Ramon Nastase - Platforma IT\PYTHON\fisier3.txt") as f3:
    for linie3 in f3: 
        linie3 = linie3.strip()
        lista.append(int(linie3))
f3.close()

lista.sort()

with open("D:\Ramon Nastase - Platforma IT\PYTHON\rezultat.txt", "w") as f4:
  f4.write(str(max(lista))+" "+str(len(lista))+"\n")
  for nr in lista:
    f4.write(str(nr)+"\n")
f4.close()