class Pracownik:
    def __init__(self, imie, pensja):
        self.imie = imie
        self.pensja = pensja
        
    def podwyzka(self, procent):
        self.pensja += self.pensja * (procent / 100)

# Проверка (эффект конечный):
p1 = Pracownik("Ola", 5000)
p1.podwyzka(10)
print(p1.pensja)
# Выведет: 5500.0
