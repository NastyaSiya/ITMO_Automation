class Checks:

    def __init__(self, loc):
        self.loc = loc

   def check_text(self):
       with open('task_9_oop_1.py', 'a') as o:
           o.write(self.loc)
