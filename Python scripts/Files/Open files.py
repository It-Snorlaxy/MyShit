navnefil = open('lastnames.txt')
efternavne = navnefil.readlines()
navnefil.close()

for navn in efternavne:
    navn = navn.strip()
    if len(navn) <= 5:
        print(navn)
