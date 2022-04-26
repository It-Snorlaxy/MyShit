class Start:

    def startServer(self):
        if self.check()==True:
         print("returnerer True til Offline objekt")
         return True

    def aktiverSpil(self):
        return True

    def loadSpilData(self):
        return True
    
    def forbindSpillere(self):
        return True
     
    def check(self):
        print("Inde i check funktion")
        if (self.aktiverSpil() and self.loadSpilData() and self.forbindSpillere() == True):
            print("Alle funktioner er startet korrekt")
            return True
    
