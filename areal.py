import os
import pi
import pow

# Funksjon for å tømme terminalen
def clear():
    os.system('cls')

# Funskjon for å skrive hovedmenyen til skjerm
def skriv_meny():
    print("\nHovedmeny for beregning av areal\n")
    print("1. Beregn areal for kvadrat")
    print("2. Beregn areal for rektangel")
    print("3. Beregn areal for trekant")
    print("4. Beregn areal for parallellogram")
    print("5. Beregn areal for rombe")
    print("6. Beregn areal for trapes")
    print("7. Beregn areal for sirkel")
    print("8. Avslutt")

# Jonas
def kvadrat(s):
    areal = s*s
    return areal


def rektangel(g, h):
    areal = g*h
    return areal

def trekant(g, h):
    areal = g*h
    areal = areal/2
    return areal

def parallellogram(g,h):
    areal = g*h
    return areal
# Slutt

# Trym
# Funksjon for å beregne arealet av en rombe skrives her. Funsjonen skal ta imot to parameter (g og h)
def rombe(g,h):
    areal = g*h
    return areal
# Funksjonen skal returnere arealet

# Utvikler 2 har ansvaret for å lage denne funksjonen




# Funksjon for å beregne arealet av en trapes skrives her. Funsjonen skal ta imot tre parameter (a, b og h)
def trapes(a,b,h):
    areal = 0,5 * (a+b) * h
    return areal
    
# Funksjonen skal returnere arealet

# Utvikler 2 har ansvaret for å lage denne funksjonen



# Funksjon for å beregne arealet av en sirkel skrives her. Funsjonen skal ta imot et parameter (r)
def sirkel(r):
    areal = 2 * 3.14 * r
    return areal
# Funksjonen skal returnere arealet

# Utvikler 2 har ansvaret for å lage denne funksjonen


   

# Programmet starter her
ans="Start"
while ans != "8":
    clear()
    skriv_meny()
    
    ans=input("Hva ønsker du å gjøre. Velg tall? ") 

    # Jonas
    if ans == "1":
        clear()
        side = int(input("Hvor stor er siden?: "))
        areal = kvadrat(side)
        print("Arealet av kvadratet er:", areal)
        venter = input("Trykk ENTER for å fortsette!") 
    elif ans=="2":
        clear()
        lengde = int(input("Lengde?: "))
        bredde = int(input("Bredde?: "))
        areal = rektangel(lengde, bredde)
        print("Arealet av rektangelet er:", areal)
        venter = input("Trykk ENTER for å fortsette!") 
    elif ans=="3":
        clear()
        grunnlinje = int(input("Grunnlinje?: "))
        hoyde = int(input("Høyde?: "))
        areal = trekant(grunnlinje, hoyde)
        print("Arealet av rektangelet er:", areal)
        venter = input("Trykk ENTER for å fortsette!")  
    elif ans=="4":
        clear()
        grunnlinje = int(input("Grunnlinje?: "))
        hoyde = int(input("Høyde?: "))
        areal = parallellogram(grunnlinje, hoyde)
        print("Arealet av rektangelet er:", areal)
        venter = input("Trykk ENTER for å fortsette!")  
    # Slutt
        
        
    elif ans=="5":
        clear()
        print("\nHer bergnes arealet av en rombe")
        venter=input("Trykk ENTER for å fortsette!") 
    elif ans=="6":
        clear()
        print("\nHer bergnes arealet av en trapes")
        venter=input("Trykk ENTER for å fortsette!")         
    elif ans=="7":
        clear()
        print("\nHer bergnes arealet av en sirkel")
        venter=input("Trykk ENTER for å fortsette!") 
    
print("\nTakk for at du brukte areal-programmet! Velkommen igjen!\n")          
    
        