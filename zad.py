class Kot:
    def __init__(self, imie, kolor):
        self.imie = imie
        self.kolor = kolor
        
    def miaucz(self):
        print(f"{self.imie} mówi: Miau!")

kot1 = Kot("Filemon", "szary")
kot1.miaucz()


#1. Конструктор (⁠__init__⁠): принимает параметры ⁠imie⁠ и ⁠kolor⁠ (помимо обязательного ⁠self⁠).

#2. Поля класса: аргументы сохраняются в ⁠self.imie⁠ и ⁠self.kolor⁠.

#3. Метод ⁠miaucz⁠: выводит с помощью f-строки имя объекта и фразу ⁠" говорит: Miau!"⁠.

#4. Создание объекта и вызов: создается экземпляр ⁠kot1⁠ с аргументами ⁠"Filemon"⁠ и ⁠"szary"⁠, после чего вызывается метод ⁠miaucz()⁠.