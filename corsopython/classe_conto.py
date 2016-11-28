class Conto:
    # metodo costruttore
    # self rappresenta l'oggetto da costruire e inizializzare
    # quando si nizializza un oggetto, spesso gli si attribuiscono
    # delle variabili, dette "variabili membro", o "proprietà"
    # in questo caso, un conto avrà la propietà amount che indica
    # il numero di soldi presenti (un numero reale anche negativo nel caso di debiti)
    def __init__(self):
        # un nuovo conto è senza denaro
        self.amount = 0

    def aggiungi_denaro(self, x):
        self.amount += x

    def togli_denaro(self, x):
        self.amount -= x

    def in_rosso(self):
        return self.amount < 0

    def denaro_presente(self):
        return self.amount

# creazione di un oggetto di classe Conto
c = Conto() # così si chiama implicitamente il costruttore, come se fosse scritto Conto.__init__(c)
c.aggiungi_denaro(10)
print(c.denaro_presente())

d = Conto() # si possono creare più oggetti, indipendenti tra loro
d.togli_denaro(1)
print(d.in_rosso())