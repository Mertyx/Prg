class Dog:

    def __init__(self,name):
        self.name = name
        print('vytvářím objekt pes s jménem')


    def bark(self):
        print(f'{self.name} štěká!')