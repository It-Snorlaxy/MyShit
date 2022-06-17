import random

Point = 0
a = 1
b = 1
Loss = False

def Opsaetning():
    #Vælger Random kort
    global a,b,Point
    a = random.choice(range(1,13))
    b = random.choice(range(1,13))



def SpillerInput():
        global a,b,Point
        print("Vendt Kort : " + str(a))
        Gæt = input("H eller L? ")
        if Gæt == "H":
            print("Nyt Kort: " + str(b))
            if b >= a:
                #korrekt gæt
                Point += 1
            if b < a:
                #ukorrekt gæt
                print("Desværre det var lavere")
                print("Din Score blev = " + "=== " + str(Point) + " ===")
        if Gæt == "L":
            print("Nyt Kort: " + str(b))
            if b <= a:
                #korrekt gæt
                Point += 1
            if b > a:
                #ukorrekt gæt
                print("Desværre det var højere")
                print("Din Score blev = " + "=== " + str(Point) + " ===")
while Loss == False:
    Opsaetning()
    SpillerInput()
