#Funktioner
#bygBumliste er en Funktion som laver en liste hvor vi gemmer et eller flere bumtal
#vi bruger while til at stoppe spilleren fra ikke at indtaste et bumtal
def bygBumliste():
    bummer = []
    nyBum = None
    while nyBum!="":
        nyBum = input("skiv nogle bumtal:")
        if nyBum.isdigit():
            bummer.append(int(nyBum))
    return bummer

#checkforbum er en funktion der kontrolere om vi har ramt et bumtal og derefter returnere True eller False
def checkforbum(tal, bumtal):
    if tal % bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False

#variabler
#spiller indeholder hvilken af spillernes tur det er.
spiller = 1
#bumliste bruger vi til at kalde vores bumliste
bumliste = bygBumliste()

#loop
#dette loop tæller for os fra 1 til 50 og holder styr på om spilleren indtaster rigtigt
for i in range(1, 51):
    tal = i
    valg = input("tal eller BUM?")
#Denne del kigger efter spillerens svar og kontrolere om det er rigtigt eller forkert.
#hvis korret er BUM så stopper vi loopet
    korrekt = str(i)
    for bumtal in bumliste:
        print('checker', bumtal)
        if checkforbum(tal, bumtal):
            korrekt = "BUM"
        else:
            korrekt = str(tal)
        if korrekt == "BUM":
            break
#dette er et feedback til spilleren Yay=rigtigt og BUH!=forkert
    if valg == korrekt:
        print("yay!")
    else:
        print("BUH!")
#denne del kontrolere tur mellem de to spillerer
    if checkforbum(i, bumtal):
        print("BUM!")
    else:
        print(i)
    if spiller == 1:
        spiller = 2
    else:
        spiller = 1
    print("tur", spiller)
