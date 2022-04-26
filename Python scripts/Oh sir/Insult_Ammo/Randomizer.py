import random

insult = ''

def importList(file):
    #Åbner
    domeding = open(file)
    #Læser og gemmer indhold i en liste
    list = domeding.readlines()
    #lukker igen
    domeding.close()
    #Fjerner alle \n der evt. er i teksten
    for i in range(len(list)):
        list[i]=list[i].strip()
        #retunerer liste
    return list

def getRandom(liste):
    domething = random.choice(liste)
    return domething

actsListe = importList('acts.txt')
acts = getRandom(actsListe)

joblist = importList('jobs.txt')
jobs = getRandom(joblist)
jobs2 = getRandom(joblist)

while jobs == jobs2:
    jobs2 = getRandom(joblist)

familylist = importList('family.txt')
family = getRandom(familylist)
family2 = getRandom(familylist)

while family == family2:
    family2 = getRandom(familylist)

thingslist = importList('things.txt')
things = getRandom(thingslist)

adjectiveslist = importList('adjectives.txt')
adjectives = getRandom(adjectiveslist)


insult += 'I don’t want to talk to you no more you {} {}!... I {} in your general direction! Your {} was a {} and your {} smelt of {}!'.format(adjectives, jobs, acts, family, jobs2, family2, things)

print(insult)
