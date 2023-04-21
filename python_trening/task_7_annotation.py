a: int = 5
b: str = 'stroka'
c: list = [1, 2]

def indent(s: str, widht: int) -> str:
    return ' ' * (max(0, widht - len(s))) + s

print(indent('123', 123))
