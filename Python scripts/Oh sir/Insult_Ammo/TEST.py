import requests, json, random

insult = ''

def importList(file):
    domeding = open(file)
    list = domeding.readlines()
    domeding.close()
    return list


actsListe = importList('acts.txt')

insult += '{} is what I do everyday'.format(actsListe)

print(insult)
