class Pryamougolnik:

    def __init__(self, shirina, vysota):
        self.shirina = shirina
        self.vysota = vysota

    def ploschad(self):
        return self.shirina * self.vysota

    def perimetr(self):
        return (self.shirina + self.vysota) * 2


p1 = Pryamougolnik(12, 4)
p2 = Pryamougolnik(35, 20)
p3 = Pryamougolnik(100, 70)

print(p1.ploschad())
print(p1.perimetr())

print(p2.ploschad())
print(p2.perimetr())

print(p3.ploschad())
print(p3.perimetr())


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return print(self.a + self.b)

    def multiplication(self):
        return print(self.a * self.b)

    def division(self):
        return print(self.a / self.b)

    def subtraction(self):
        return print(self.a - self.b)


class ElementsSidebar:

    def __init__(self, text, tip='Knopka', loc=''):
        self.text = text
        self.tip = tip
        self.loc = loc

    def push(self):
        return print(f'Klik po knopke {self.text}')


k1 = ElementsSidebar('Text Box')
k2 = ElementsSidebar('Check Box')
k3 = ElementsSidebar('Radio Button')
k4 = ElementsSidebar('Web Tables')
k5 = ElementsSidebar('Buttons')
k6 = ElementsSidebar('Links')
k7 = ElementsSidebar('Broken Links - Images')
k8 = ElementsSidebar('Upload and Download')
k9 = ElementsSidebar('Dynamic Properties')


print(k1.text)
print(k2.text)
print(k3.text)
print(k4.text)
print(k5.text)
print(k6.text)
print(k7.text)
print(k8.text)
print(k9.text)

k1.push()
k2.push()
k3.push()
k4.push()
k5.push()
k6.push()
k7.push()
k8.push()
k9.push()
