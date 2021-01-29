"""Creati un program care solicita utilizatorului sa introduca numele si varsta. Aflati un mesaj care-i spune anul in care va 
implini 100 de ani. Faceti asta cu datele a 3 persoane diferite si afisati-le separat, pe cate o linie nou (poti folosi '\n' pentru 
asta)."""
i=1
while i<4:
    numele = input("Cum te numesti?\n")
    varsta = int (input ("Ce varsta ai?\n"))
        
    from datetime import date

    anulCurent = date.today().year
    anulNasterii = anulCurent - varsta

    anul100 = anulNasterii  + 100

    print("Buna,",numele,"!\nTu ai",varsta,"ani.\nIn anul",anul100,"vei avea 100 de ani.\n")
    i += 1

  
    
    
