class Kot:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor
        
    def miaucz(self):
        print(f"{self.imie} mówi: Miau!")

kot1 = Kot("Filemon", "szary")
kot1.miaucz()
