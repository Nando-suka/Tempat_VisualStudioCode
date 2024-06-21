class motor:
    def roda (self):
        return "Roda dua"
    
class mobil:
    def roda (self):
        return "Roda empat"
    
class truk:
    def roda (self):
        return "Roda enam"
    
def informasiRoda (roda):
    return roda.roda()


Motor = motor()
Mobil = mobil()
Truk = truk()

print("Motor:",informasiRoda(Motor))
print("Mobil:",informasiRoda(Mobil))
print("Truk:",informasiRoda(Truk))
