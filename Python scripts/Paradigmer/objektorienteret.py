class Fag():

    def __init__(self, navnet, karakteren=None):
        self.navn = navnet
        self.karakter = karakteren

class KarakterBog():

    separator = '~'

    def __init__(self, elev='Navnløs'):
        self.elevNavn = elev
        self.data = []

    def nytFag(self, fag):
        self.data.append(fag)

    def beregnSnit(self):
        total = 0
        for fag in self.data:
            total += fag.karakter
        return 'Karaktergennemsnit af {} fag: {}\n'.format(len(self.data), round(total/len(self.data), 2))

    def udskrivAlleKarakterer(self):
        output = ''
        for fag in self.data:
            output += 'Karakteren i {} er: {}\n'.format(fag.navn.capitalize(), fag.karakter)
        return output

martins = KarakterBog('Martin')

martins.nytFag(Fag('dansk', 4))
martins.nytFag(Fag('programmering', 12))
martins.nytFag(Fag('innovation', -3))
martins.nytFag(Fag('teknologi', -3))
martins.nytFag(Fag('opvask', 12))
martins.nytFag(Fag('racerbil', 12))

batmans = KarakterBog('Batman')

batmans.nytFag(Fag('sperlunking', 7))
batmans.nytFag(Fag('romancing', 2))
batmans.nytFag(Fag('public speaking', -3))
batmans.nytFag(Fag('ninja', 10))
batmans.nytFag(Fag('crime fighting', 12))

def udskrivKarakterbog(bog):
    print(bog.separator * 35 + '\n')
    print('Karakterbog for:', bog.elevNavn, '\n')
    print(bog.beregnSnit())
    print(bog.udskrivAlleKarakterer())
    print(bog.separator * 35 + '\n')

udskrivKarakterbog(batmans)
udskrivKarakterbog(martins)
