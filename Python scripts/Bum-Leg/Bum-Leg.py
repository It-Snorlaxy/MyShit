#dette er funktionen der checker for bumtal
bumtal = None

bumtal = int(input("Hvad er dit bumtal?\n" ))

#dette er funktionen der checker for bumtal
def checkforbum(tal, bumtal):
    if tal % bumtal == 0:
        return True
    elif str(bumtal) in str(tal):
        return True
    else:
        return False


# dette er en counter den tæller for 1-50
for i in range(1, 51):
    if checkforbum(i, bumtal):
        print("BUM!")
    else:
        print(i)
