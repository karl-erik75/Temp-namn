import time
global namn
global kön6
global land
land = True
import random
global age
global kr
loop = True 
ro_båt = False
fiske_båt = False
small_krigs_skep = False
kr = 7
#saker (kommer att sortera snart, karnse)
#-----------------------------------------------------------------------
def start():
    global styrka
    global fart
    global iq
    global age2
   
    print("\033c", end="")
    print("du heter", (namn), "din ålder är", (age))
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
        åka = input("du kan gå till (affären) eller skafa (jobb)🤮 ")
        if åka == "affären":
            print("du tänkte gå till affären fast du mins att du är fattig så du välger att gå tillbaka ")
            åka = input("du kan gå ock skaffa ett (jobb)🤮 ")
            intro()
            if åka == "jobb":
                intro()


        else:
            input("du valde skafa ett jobb")
            intro()



    elif åka == "affären":
        print("du tänkte gå till affären fast du mins att du är fattig så du välger att gå tillbaka")
        åka = input("du kan gå och skaffa ett (jobb)🤮 ")
        if åka == "jobb":
            intro()


    else:
        input("du valde att skafa ett jobb🤮 ")
        intro()
#-----------------------------------------------------------------------

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
    fråga_land1()     
#-----------------------------------------------------------------------





#affärer#
#-----------------------------------------------------------------------
def båt_affär1():
    global kr
    print("\033c", end="")
    input("-om jag skaffar en fiske båt så kan jag börja sälja de jag fångar för pengar- tänkte du")
    while True:
        print("i affären så kan du sköpa 3 olika båtar eller så kan du gå ivåg")
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
                    if small_krigs_skep == True:
                        print("du har redan ett littet krigs skepp")
                    else:
                        kr -= 1000
                        small_krigs_skep == True
                        input("du äger ett littet krigs skepp nu!")

            elif s_krigs_båt_fråga == "nej":
                input("du ångrar dig")

            
                

        elif frå == "bort":
            fråga_land1()

        else:
            print("du skrev något fell skriv bara det som fins inom parenteserna")
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
def general_store1():
    print("\033c", end="")
    while True:
        global kr
        print("du har", kr)
        fråga = input("vad söker du efter (läkemedel), (vapen), (fiske spö), (krut vapen) eller (övriga grejer) skriv (bak) om du vill till baka")
        #-------------------------------------------------------------------------------------------
        if fråga == "läkemdel":
            fråga2 = input("inom läkemdlet så kan du sköpa (bandage)(första hjälpen) (bak) om du vill till baka ")
            if fråga2 == "bandage":
                fråga3 = input("är du säker du vill köpa bandage för 5 styk `den läker 25 hp av dit 100 hp  (ja) eller (nej) ")
                if fråga3 == "ja":
                     #-----------------------------------------------
                    print("snart")
                     #-----------------------------------------------


                
            elif fråga2 == "första hjälpen":
                fråga3 = input("är du säker att du vill köpa första hjälpen för 25 styck `den läker 80hp av dit 100 hp`(ja) eller (nej) ")
                if fråga3 == "ja":
                 #-----------------------------------------------
                    print("snart")
                 #-----------------------------------------------

            elif fråga2 == "bak":
                print("\033c", end="")
        #-------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------
        elif fråga == "vapen":
            fråga2 = input("dom vapen som fins är (spjut), (svärd), (kniv), (pilbåge) skriv (bak) om du vill till baka")
            if fråga2 == "spjut":
                fråga3 = input("är du säker du vill köpa ett spjut som  kostar 20 styck och gör 25 skada i slag och 40 skada om kastat (ja) eller (nej) ")
                if fråga3 == "ja":
                 #-----------------------------------------------
                   print("snart")
                 #-----------------------------------------------
            #---------------------------------------------------------------------------------------------
            elif fråga2 == "svärd":
                fråga3 = input("är du säker du vill köpa ett svärd som  kostar 40 och gör 30 skada (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if svärd == False and kr >= 40:
                        svärd = True
                        kr -= 40
                        input("du har ett svärd nu!!!")

                    else:
                        input("du har inte nog mycket pengar du behöver 40")


                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
            #---------------------------------------------------------------------------------------------
            elif fråga2 == "kniv":
                fråga3 = input("vill du köpa en kniv för 10 styck och gör 10 skada i slag och 15 kastat (ja) eller (nej) ")
                if fråga3 == "ja":
                 #-----------------------------------------------
                    print("snart")
                 #-----------------------------------------------
            #---------------------------------------------------------------------------------------------
            elif fråga2 == "pilbäge":
                fråga3 = input("är du säker du vill köpa en pilbåge för 50 som gör 25 skade pär skott (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if pilbåge == False and kr >= 50:
                        kr -=50
                        input("du köpte en pilbåge för 50!")
                        pilbåge = True

                    

                    else:
                        input("du har för lite pengar du behöver mins 50")
                        print("\033c", end="")

                    

                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
            #---------------------------------------------------------------------------------------------
            elif fråga2 == "bak":
                print("\033c", end="")
        #-------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------
        elif fråga == "fiske spö":
            fråga2 = input("det fins 3 olika fiske spön (begagnad), (ny), (premium) skriv (bak) om du vill till baka")
         #------------------------------------------------------------------
            if fråga2 == "begagnad":
                fråga3 = input("är du säker du vill köpa ett bagagnad fiske spå för 20 kr?(ja) eller (nej) ")
                if fråga3 == "ja":
            
                    if spö_bg == False and kr >= 20:
                        kr -= 20
                        spö_bg = True
                        print("du äger ett begagnad fiske spö nu!")

                    else:
                        print("du har inte nog mycket pengar du behöver 20")


                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
         #------------------------------------------------------------------ 
            elif fråga2 == "ny":
                fråga3 = input("är du säker du vill köpa ett nyt fiske spå för 50 kr? (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if spö_ny == False and kr >= 50:
                        kr -= 50
                        spö_ny = True
                        print("du äger ett nyt fiske spö nu!")

                    else:
                        print("du har inte nog mycket pengar du behöver 50")
                        print("\033c", end="")

                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
             #-------------------------------------------------------------------------------------------
         #------------------------------------------------------------------
            elif fråga2 == "premium":
                fråga3 = input("är du säker du vill köpa ett premium fiske spå för 150 kr?( ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if spö_prem == False and kr >= 150:
                        kr -= 150
                        spö_perm = True
                        print("du äger ett premium fiske spö nu!")

                    else:
                        print("du har inte nog mycket pengar du behöver 150")
                        print("\033c", end="")
                        
        #-------------------------------------------------------------------------------------------
                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
         #------------------------------------------------------------------
            elif fråga2 == "bak":
                print("\033c", end="")
        #-------------------------------------------------------------------------------------------
        #-------------------------------------------------------------------------------------------
        elif fråga == "krut vapen":
            fråga2 = input("du kan välga melan desa krut vapen (flintlock), (musket), (blunderbuss) skriv (bak) om du vill till baka")
            if fråga2 == "flintlock":
                fråga3 = input("är du säker du vill köpa en fintlock för 70 som gör 75 skada (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if  flintlock == False and kr >= 70:
                        kr -= 70
                        flintlock = True 
                        input("du äger en flintlock nu!")
                        print("\033c", end="")

                    else:
                        print("du har inte nog mycket pengar du behöver 70")






                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
            
            elif fråga2 == "musket":
                fråga3 = input("är du äker du vill köpa en musket för 150 som gör 120 skada (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if musket == False and kr >= 150:
                        kr -= 150
                        musket = True
                        input("du äger en musket nu ")
                        print("\033c", end="")

                    else:
                        input("du har inte pengarna nog för att köpa dena produkt")
                        print("\033c", end="")


                    
                        

                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")
            elif fråga2 == "blundebuss":
                fråga3 = input("är du söker du vill köpa en blunderbuss för 125 som gjör 170 skada närvid men mycket mindre längre bort (ja) eller (nej) ")
                if fråga3 == "ja":
                
                    if blunderbuss == False and kr >= 125:
                        kr -= 125
                        blunderbuss = True
                        input("du har en blunderbuss nu!! ")
                        print("\033c", end="")

                    else:
                        input("du har inte nog mycket pengar för att köpa det här du behöver 125")


                elif fråga3 == "nej":
                    input("du valde att inte köpa något")
                    print("\033c", end="")

            elif fråga2 == "bak":
                input("du valde att inte köpa något")
                print("\033c", end="")        
        #-------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------










#-----------------------------------------------------------------------
def fråga_land1():
    while True:
        frå = input("var vill du gå nu? skriv (karta) för att se vart du kan gå")
        if frå == "karta":
            frå = input("du kan skriva (affär), (arbete), (båt affär), (lager), (försäljare)")
        
        elif frå == "affär":
            general_store1()

        elif frå == "båt affär":
            båt_affär1()

        elif frå == "arbete":
            print("inte klar")

        elif frå == "lager":
            print("wip")

        elif frå == "försäljare":
            print("wip")

        else:
            print("du skrev något fell skriv bara det som fins inom parenteserna!")

    


    


    


    























while loop == True:
    #-----------------------------------------------------------------------
    fråga11 = True
    print("\033c", end="")
    namn = input("Vad vill du heta? ")

    while fråga11 == True:
        age = int(input("vilken ålder vill du vara? "))

        kön = input("vill du vara man eller kvinna? ")

        if age < 14 or age > 100:
            print("(du måste vara melan 14 och 100)")

        fråga11 = False
        loop = False
    else:
        
        start()
    #-----------------------------------------------------------------------

print("SLUT")


    

