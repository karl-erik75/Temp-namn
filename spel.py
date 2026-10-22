global namn
import random
fråga11 = True
print("\033c", end="")
while fråga11 == True:
    namn = input("Vad vill du heta? ")

    age = int(input("vilken ålder vill du vara? "))

    kön = input("vill du vara man eller kvina? ")

    if kön != "man" or kön != "kvina" or kön != "Man" or kön != "Kvina":
        print("du får bara vara en man eller en kvina grr")

    else:
        fråga11 == False
        start()




#-----------------------------------------------------------------------
def start():
    print

#-----------------------------------------------------------------------
    

