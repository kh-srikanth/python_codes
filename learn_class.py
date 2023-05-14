class human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == 'tennis player':
            print(self.name, 'plays tennis')
        elif self.occupation == 'actor':
            print(self.name, 'is an actor')

    def speak(self):
        print(self.name, ': How do you do?')


tom = human('Tom Cruise', 'actor')
maria = human('Maria Sharapova', 'tennis player')
srikanth = human('srikanth kahndavalli','coder')
tom.do_work()
tom.speak()
