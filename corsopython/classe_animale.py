class Animal:
    # il costruttore può essere omesso
    # sarà creato implicitamente e non effettuerà nessuna operazione
    def speak(self):
        return ""

    def speak_three_times(self):
        for i in range(3):
            print(self.speak())

class Human(Animal):
    def speak(self):
        return "ciao"

class Dog(Animal):
    def speak(self):
        return "woof"

d = Dog()
u = Human()
d.speak_three_times()
u.speak_three_times()