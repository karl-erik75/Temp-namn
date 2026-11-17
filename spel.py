import time
global namn
global kön6
global land
land = True
import random
global age
global kr 
ro_båt = False
fiske_båt = False
kr = 7
#saker (kommer att sortera snart, karnse)
#-----------------------------------------------------------------------
def start():
    global styrka
    global fart
    global iq
    global age2
   
    print("\033c", end="")
    print("du heter", (namn), "din ålder är", (age), "du är en", (kön))
    if age >= 70:
        age2 = "gamal"
        input("du är över 70 vad som gjör att du blir långsamare och svagare men smartare")
        fart = 5
        styrka = 5
        iq = 15
    elif age <= 18:
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
    input("du vaknar up en fin somar dag")
    input("du välger att gå ner i köket")
    #ung
    #-----------------------------------------------------------------------
    event = random.randint(1,3)
    if age2 == "ung" and event == 1:
        input("du och din mama börjar bråka...")
        input("igen")
        input("-jag står inte ut med dig mera! skriker din mamma")
        input("hon pekar på dören bestämt -ut! skriker hon")
        input("du blir utsparkad från dit häm")
        input("om dom inte vill ha dig där varför skule du vilja gå tillbaka? säger du till dig skälv")
        hem_by_fråga()

    elif age2 == "ung" and event ==2:
        input("du komerihåg att du inte står ut med dina föräldrar längre")
        input("du välger att fly hämifrån")
        hem_by_fråga()

    elif age2 == "ung" and event ==3:
        input("-du börjar bli för gamal nu! skirker din far när han ser dig i köket")
        input("han ger dig inget och sparkar ut dig")
        hem_by_fråga()


    #-----------------------------------------------------------------------

    #medianålder
    #-----------------------------------------------------------------------
    elif age2 == "normal" and event ==1:
        input("du mins att du avkyr din sambo och du välger att fly från hern utan att säga ett pip")
        hem_by_fråga()

    elif age2 == "normal" and event ==2:
        input("din far tycker du är för gamal för att bo med han!")
        print("för fan du är ju", age, "nu! skriker han")
        input("du blir ut sparkad")
        hem_by_fråga()

    elif age2 == "normal" and event ==3:
        input("sen mins du...")
        input("du är ensam")
        input("du har inga kompisar")
        input("du har inget jobb")
        input("du har ingen som älskar dig")
        input("du stinker")
        input("och ingen gillar dig")
        input("börja gjöra något bror!")
        hem_by_fråga()

    #-----------------------------------------------------------------------
    #gamal
    #-----------------------------------------------------------------------
    elif age2 == "gamal" and event ==1:
        input("ålderdomshämets personal står inte ut med dig mera")
        input("du blir utsparkad")
        hem_by_fråga()

    elif age2 == "gamal" and event ==2:
        input("dit barn barn tar dig till sofan med en stor stark kille brevid han")
        input("-papa jag gillar men, säger dit barn barn")
        input("dit ända barn barn är gay?!?!")
        input("du springer för ditt liv för att du vill inte få gay baciller")
        hem_by_fråga()

    elif age2 == "gamal" and event ==3:
        input("du ser din fru med en ung snyg star karr")
        input("du inser du att...")
        input("en ung grab stal din sambo hur vågar han!")
        input("du springer iväg och gråter samtidigt ")
        hem_by_fråga()

    #-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
def hem_by_fråga():
    print("\033c", end="")
    input("du vill aldrig gå tillbaka igen! du välger att fly och starta ett nyt liv!")
    åka = input("vart vill du gå nu? skriv (karta) om du vill see vart man kan gå ")
    if åka == "karta":
        åka = input("du kan gå till (affären) eller skafa (jobb)🤮")
        if åka == "affären":
            print("du tänkte gå till affären fast du mins att du är fattig så du välger att gå tillbaka")
            åka = input("du kan gå ock skaffa ett (jobb)🤮")
            if åka == "jobb":
                intro()


        else:
            input("du valde skafa ett jobb")
            intro()



    elif åka == "affären":
        print("du tänkte gå till affären fast du mins att du är fattig så du välger att gå tillbaka")
        åka = input("du kan gå ock skaffa ett (jobb)🤮")
        if åka == "jobb":
            intro()


    else:
        input("du valde att skafa ett jobb🤮")
        intro()
#-----------------------------------------------------------------------
def intro():
    global age
    global kr
    age += 3
    kr = 2500
    print("\033c", end="")
    input("du har jobbat som en diskare i 3 år nu")
    input("året är nu 1720")
    input("du förlorade dit jobb")
    input("du fick i totalt 2500 pengar över från de 3 år du jobbade 😬")
    input("2 månader senare du har fortfarande inget jobb... ")
    input("du har också förlorat dit hus som du köpte igår 😬")
    input(":(")
    while True:
        fråg = input("vart vill du gå nu? skriv (karta) om du vill see vsrt du kan gå")
        if fråg == "karta":
            print("skriv (affär) får att gå till affären. skriv (jobb) för att skafa jobb. skriv (båt affär) för att sköpa en båt")
        
        elif fråg == "affär":
            print("de är stängda just nu")

        elif fråg == "jobb":
            print("ingen vill anstäla dig ")

        elif fråg == "båt affär":
            input("du gick till båt affären")
            båt_affär()


        else:
            print("du skrev något fell skriv exact det som fins inom parentesna")
#-----------------------------------------------------------------------





#affärer#
#-----------------------------------------------------------------------
def båt_affär():
    print("\033c", end="")
    input("-om jag skaffar en fiske båt så kan jag börja sälja de jag fångar för pengar- tänkte du")
    while True:
        input("i affären så kan du sköpa 3 olika båtar eller så kan du gå ivåg")
        print("du har", kr)
        frå = input("(ro båt) (fiske båt) (littet krigs skepp) (bort)")
        if frå == "ro båt":
            ro_båt_fråga = input("vill du sköpa en robåt för 700? skriv (info) om du vill ha info om båten")
            if ro_båt_fråga == "info":
                input("En robåt rymer 5 personer, 5 föremål och 10 fiskar.")
            elif ro_båt_fråga == "ja":
                if kr - 700 < 0:
                    print("sorry broshan du är för fatig 😮‍💨")

                elif kr - 700 > 0:
                    if ro_båt == True:
                        print("du har redan en ro båt")
                    else:
                        kr -= 700
                        ro_båt == True
                        input("DU ÄGER EN RO BÅT NUU!!!!!!")
                    

            elif ro_båt_fråga == "nej":
                input("du ångrar dig")


        elif frå == "fiske båt":
            fiske_båt_fråga = input("vill du sköpa en fiske båt för 1000? skriv (info) om du vill ha info om båten")
            if fiske_båt_fråga == "info":
                input("En fiske båt rymer 7 personer, 20 föremål och 70 fiskar.")
            elif fiske_båt_fråga == "ja":
                if kr - 1000 < 0:
                    print("sorry broshan du är för fatig 😮‍💨")

                elif kr - 1000 > 0:
                    if fiske_båt == True:
                        print("du har redan en fiske båt")
                    else:
                        kr -= 1000
                        ro_båt == True
                        input("du äger en fiske båt nu!")

            elif fiske_båt_fråga == "nej":
                input("du ångrar dig")


        elif frå == "littet krigs skepp":
            s_krigs_båt_fråga = input("(ja) om vill du sköpa ett littet krigs skepp för 3500? skriv (info) om du vill ha info om båten. (nej) om du inte vill")
            if s_krigs_båt_fråga == "info":
                input("ett krigs skepp rymer 35 personer, 100 föremål  8 cannoner,")
            elif s_krigs_båt_fråga == "ja":
                if kr - 1000 < 0:
                    print("sorry broshan du är för fatig 😮‍💨")

                elif kr - 1000 > 0:
                    if fiske_båt == True:
                        print("du har redan en fiske båt")
                    else:
                        kr -= 1000
                        ro_båt == True
                        input("du äger en fiske båt nu!")

            elif s_krigs_båt_fråga == "nej":

            
                

        elif frå == "bort":
            fråga()

        else:
            print("du skrev något fell skriv bara det som fins inom parenteserna")

#-----------------------------------------------------------------------
def general_store():




def fråga():
    


    


    























while loop == True:
    #-----------------------------------------------------------------------
    fråga11 = True
    print("\033c", end="")
    namn = input("Vad vill du heta? ")

    while fråga11 == True:
        age = int(input("vilken ålder vill du vara? "))

        kön = input("vill du vara man eller kvinna? ")

        if kön != "man" and kön != "kvinna" and kön != "Man" and kön != "Kvinna" or age < 14 or age > 100:
            print("du kan bara vara en (man) eller (kvinna) arnars orimlig ålder (du måste vara melan 14 och 100)")

        
        loop = False
    else:
        fråga11 == False
        start()
    #-----------------------------------------------------------------------

print("SLUT SLUT SLUTAAA!")


    

