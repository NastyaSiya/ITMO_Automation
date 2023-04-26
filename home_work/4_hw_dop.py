class Car:

    def __init__(self, color, tip, year):
        self.color = color
        self.tip = tip
        self.year = year

    def zapusk(self):
        return print('Avtomobil zaveden')

    def otkluchenie(self):
        return print('Avtomobil zagluschen')

    def god(self, a):
        self.year = a
        return print(self.year)

    def tp(self, b):
        self.tip = b
        return print(self.tip)

    def tsvet(self, c):
        self.color = c
        return print(self.color)


a = Car('Siniy', 'Sedan', '2001')

a.god('2021')
