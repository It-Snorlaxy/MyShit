KarekterBlad = {"Engelsk": 7,"Dansk": 10,"Matematik": 2,"Teknologi": 7,"Kemi" :7,"Fysik": 7,"Programmering": 7,"Kom-it": 10,"psykologi": 7}

def udskrivEnKarakter(fag, bog):
    if fag in bog.keys():
        karakter = bog[fag]
        tilPrint = "Karakteren for {}: {}".format(fag,karakter)
        print(tilPrint)
    else:
        print('Fejl. Der findes ingen karakter for det angivne fag, i den angivne karakterbog.('+ fag + ")")



def udskrivAlleKarakterer(k):
    for key in k.keys():
        udskrivEnKarakter(key,k)




def beregnSnit(k):
    total = 0
    for karakter in k.values():
        total = total + karakter
    snit = total/len(k)
    print("gennemsnit af karakter i {} fag: {}" .format(len(k), snit))

beregnSnit(KarekterBlad)
