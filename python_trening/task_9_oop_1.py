from task_9_checks import Checks


class Input(Checks):

    def __init__(self, loc):
        super().__init__(loc)
        self.loc = loc


search = Input(123)

print(search.check_text())

print()

