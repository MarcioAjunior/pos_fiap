"""
Observer é um padrão de criação de classe que permite que a classe possua um observador, mantidos em um array na classe observada,
isso é util para quando é necessário atualizar os valores das clases filhas quando um atributo mudou na classe pai, 
sendo elas notificadas da mundaça por um método da classe pai, nesse notify, que executa o update das classes filhas.
"""

class Observer:
    def update(self, subject):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class ConcreteObserver(Observer):
    def update(self, subject):
        print("Received update from subject")

class ConcreteSubject(Subject):
    def do_something(self):
        # Do something
        self.notify()

# Uso
subject = ConcreteSubject()
observer = ConcreteObserver()
subject.attach(observer)
subject.do_something()
