# d = {"nume": "Florentina", "varsta": 20, "domeniu": "IT"}
# d2 = {"nume": "ALex", "varsta": 23, "domeniu": "Financiar"}

# print(d.get("nume"))

# print(d.keys())

# l = [d, d2]

# for i in l:
#     print("In baza de data avem:")
#     print(i.get("nume"))

"""1.1) Creati cu ajutorul unui dictionar o baza de date la care sa retineti numerele de telefon a 10 prieteni"""

agenda = {
    "pers1" : {
        "nume": "Mara",
        "numar": "0765432423"
    },
    "pers2" : {
        "nume": "Alex",
        "numar": "0765332423"
    },
    "pers3" : {
        "nume": "Vlad",
        "numar": "0762332423"
    },
    "pers4" : {
        "nume": "Mateo",
        "numar": "0764332423"
    },
    "pers5" : {
        "nume": "Matei",
        "numar": "07656532423"
    },
    "pers6" : {
        "nume": "Robert",
        "numar": "07654762423"
    },
    "pers7" : {
        "nume": "Lucian",
        "numar": "0765454423"
    },
    "pers8" : {
        "nume": "Stefan",
        "numar": "07654398423"
    },
    "pers9" : {
        "nume": "Livia",
        "numar": "0765437823"
    },
    "pers10" : {
        "nume": "Ioana",
        "numar": "07654327623"
    }
}

for x in agenda.items():
    print(x)
    
print("Dupa sortare: ")
for i, j in agenda.items():
    sorted_agenda = {i: sorted(j)}
    print(sorted_agenda)

1.2) Afisati intrarile din aceasta baze
