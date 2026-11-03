global namn
global kön6
global land
land = True
import random
global age
#-----------------------------------------------------------------------
def start():
    global styrka
    global fart
    global iq
    global age2
   
    print("\033c", end="")
    print("du heter", (namn), "din ålder är", (age), "du är en", (kön))
    if age > 70:
        age2 = "gamal"
        input("du är över 70 vad som gjör att du blir långsamare och svagare men smartare")
        fart = 5
        styrka = 5
        iq = 15
    elif age < 18:
        age2 = "ung"
        input("du är under 18 som gjör dig dunmare! och lite svagare samt långsamare ")
        fart = 15
        styrka = 15
        iq = 5
    
    else:
        age2 = "normal"
        input("du är melan 70 och 18 du blir icke dummare, svagare eller långsamare")
        fart = 10
        styrka = 10
        iq = 10
    start_event()
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def start_event():
    print("\033c", end="")
    #ung
    #-----------------------------------------------------------------------
    event = random.randint(1,3)
    if age2 == "ung" and event == 1:
        input("du och din mama bråkar...")
        input("igen")
        input("-jag står inte ut med dig mera! skriker din mamma")
        input("hon pekar på dören bestämt -ut! skriker hon")
        input("du blir utsparkad från dit häm")
        fråga()

    elif age2 == "ung" and event ==2:

    elif age2 == "ung" and event ==3:

    #-----------------------------------------------------------------------

    #medianålder
    #-----------------------------------------------------------------------
    elif age2 == "normal" and event ==1:

    elif age2 == "normal" and event ==2:

    elif age2 == "normal" and event ==3:

    #-----------------------------------------------------------------------
    #gamal
    #-----------------------------------------------------------------------
    elif age2 == "gamal" and event ==1:

    elif age2 == "gamal" and event ==2:

    elif age2 == "gamal" and event ==3:

    #-----------------------------------------------------------------------
   
    


























#-----------------------------------------------------------------------
fråga11 = True
print("\033c", end="")
while fråga11 == True:
    namn = input("Vad vill du heta? ")

    age = int(input("vilken ålder vill du vara? "))

    kön = input("vill du vara man eller kvina? ")

    if kön != "man" or kön != "kvina" or kön != "Man" or kön != "Kvina":
        print("du får bara vara en man eller en kvina grr")

    if age <= 14 or age >= 100:
        print("du har en orimlig ålder ten en ålder melan 14 och 100")

    else:
        fråga11 == False
        start()
#-----------------------------------------------------------------------




    

