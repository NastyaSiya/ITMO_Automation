def task_1(a: int, b: float, c: str, d: list, e: bool) -> tuple:

    return type(a), type(b), type(c), type(d), type(e)


print(task_1(5, 3.45, '5, 5, hi, 50', ['nice', 2, 'see', 'u'], True))


def task_2(a) -> list:
    return a[0:3]


print(task_2([1, 2, 3, 5, 8, 13, 21]), '- eto chisla Fibonacci')


def task_3(a: int) -> int:
    return a**2


print(task_3(9))
