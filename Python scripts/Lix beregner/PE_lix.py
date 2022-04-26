import requests
import json

Paragraphs = requests.get('https://loripsum.net/api/10/long/plaintext')


if Paragraphs.status_code == 200:
    Wordcount = len(Paragraphs.text.split(' '))
    Dotcount = Paragraphs.text.count('.')
    longwords = 0
    Sværhedsgræd = 'Sværhedsgræd'
    for Words in Paragraphs.text.split(' '):
        for letters in ".,!;:?":
            Words = Words.replace(letters, '')
        if len(Words) > 6:
            longwords = longwords + 1
    print('Wordcount:' + str(Wordcount))
    print('Dotcount:' + str(Dotcount))
    print('Longwords:' + str(longwords))
    Lix = int(Wordcount/Dotcount + (longwords * 100)/Wordcount)
    if Lix <= 24:
        print(Sværhedsgræd + 'Let for alle læsere')
    if Lix >= 25 and <=34:
        print(Sværhedsgræd + 'Let for øvede')
    if Lix >= 35 and <=44:
        print(Sværhedsgræd + 'Middel f.eks dagblade og tidsskrifter.')
    if Lix >= 45 and <=54:
        print(Sværhedsgræd + 'Svær, f.eks. saglige bøger, populærvidenskabelige værker, akademiske udgivelser.')
    if >= 55:
        print(Sværhedsgræd +
              'Meget svær, faglitteratur på akademisk niveau, lovtekster.')


Text_holder = open('Text_holder', 'w')
Text_holder.write(Paragraphs.text)
Text_holder.close()
