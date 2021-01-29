"""1) Se da o lista a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Creeaza un program care sa elimine elemetele impare din aceasta lista"""

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(a):
#     if a[i]%2!=0:
#         a.remove(a[i])
#         i += 1
# print(a)

#----------------------------------------------------------------------------------------------------------------------
"""2.1) Creeaza o lista cu numele a 10 prieteni (numele nu trebuie sa fie distincte). Respectand ordinea, rezolvati 
urmatoarele cerinte."""
# nume = ["Vlad", "Anca", "Lucian", "Lucian", "Alex", "Ioana", "Rares", "Bogdan", "Vlad", "George"]

# # X= Sortati lista de nume
# nume.sort()
# print(nume)

# # X= Utilizand o lista auxiliara, determinati numarul de aparitii al fiecarui nume
# from collections import Counter

# lista_aux = Counter(nume)
# print(lista_aux)

# # X= Determinati numele care apare de cele mai multe ori in lista initiala
# def contor(nume): 
#     return max(set(nume), key = nume.count) 

# print(contor(nume))

# # X= Determinati numele care apare de cele mai putine ori in lista initiala
# def contor(nume): 
#     return min(set(nume), key = nume.count) 

# print(contor(nume))

# # X= Revenind la lista initiala de nume, inversati ordinea elementelor
# nume.sort(reverse=True)
# print(nume)

#----------------------------------------------------------------------------------------------------------------------
"""2.2) Formati perechi de cate 2 persoane cu numele din lista initiala si impartiti aceste perechi (in mod egal) in 2 liste. 
Asigurati-va ca acestor perechi nu li se poate modifica valoarea (hint: tupluri). Avand aceste perechi, calculati numarul 
total de caractere pentru fiecare pereche in parte si creati o lista noua in care sa le introduceti in ordine 
descrescatore."""

lista_nume = ["Vlad", "Anca", "Lucian", "Lucian", "Alex", "Ioana", "Rares", "Bogdan", "Vlad", "George"]

lista_nume.sort()
print(lista_nume)




#----------------------------------------------------------------------------------------------------------------------
"""3) Scrieti un script care afiseaza in consola toate numerele pare divizibile cu 7 din intervalul [0, 3463]. Sugestie: 
folositi functia xrange. Ajustati codul astfel incat la aparitia primului multiplu al lui 666, algoritmul sa se opreasca."""





























