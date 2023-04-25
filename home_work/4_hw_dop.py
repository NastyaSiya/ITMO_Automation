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
        a = self.year

    def tp(self, b):
        b = self.tip

    def tsvet(self, c):
        c = self.color


a = Car('Siniy', 'Sedan', '2001')

print(a.god())
