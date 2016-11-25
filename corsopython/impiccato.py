import tkinter as tk

class Impiccato(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Le user interface grafiche funzionano in modo gerarchico
        # il primo parametro dei vari costruttori tk.Frame, tk.Canvas, tk.Button eccetera
        # sono l'oggetto parent (genitore) del componente
        # Il parent di tutti gli oggetti è tk.Tk(), che qui è self
        frame_left = tk.Frame(self)
        frame_right = tk.Frame(self)
        frame_left.pack(side=tk.LEFT)
        frame_right.pack(side=tk.RIGHT)

        # qui sopra e in seguito, il metodo pack() serve a calcolare le dimensioni del componente

        # canvas su cui viene disegnato l'omino
        self.canvas = tk.Canvas(frame_right, width=400, height=600)
        self.canvas.pack()

        self.new_game_button = tk.Button(frame_left,
                             text="Nuovo gioco",
                             command=self.new_game)
        self.new_game_button.pack()

        self.letter_entry = tk.Entry(frame_left)
        self.letter_entry.bind("<Return>", self.on_enter_pressed)
        self.letter_entry.pack()

        # imposta un nuovo gioco dell'impiccato
        self.new_game()

    def new_game(self):
        # Usa una parola fissa
        # Miglioramento 1: usare una lista di parole da cui scegliere e selezionarne una casualmente ad
        # ogni nuovo gioco
        # Miglioramento 2: leggere la lista da un file che ha ogni parola per riga, cercare un dizionario
        # testuale su internet
        self.word = "tavolo"
        self.found = [False] * len(self.word) # guardare check_letter dopo per capire l'uso di found'
        self.ended = False
        self.drawing_index = 0

        self.canvas.delete("all")
        # il testo è brutto perché non ci sono spazi intervallati: modificare
        self.canvas.create_text(200, 550, text = "_" * len(self.word), tags = "text")

    def on_enter_pressed(self, event):
        if self.ended:
            # se il gioco è terminato termino subito
            return

        text = self.letter_entry.get()
        # prendo solo il primo carattere
        c = text[0]

        # lista di metodi da chiamare in sequenza
        drawings = [ self.draw_head, self.draw_body, self.draw_left_arm ]

        if self.check_letter(c):
            # inserisco il nuovo testo
            new_text = ''
            for i in range(len(self.word)):
                if self.found[i]:
                    new_text += self.word[i]
                else:
                    new_text += '_'

            #elimino il vecchio testo visualizzato
            self.canvas.delete("text")
            # metto quello nuovo
            self.canvas.create_text(200, 550, text = new_text, tags = "text")
        else:
            if self.drawing_index == len(drawings):
                self.canvas.delete("text")
                self.canvas.create_text(200, 550, text = 'hai perso', tags = "text")
                # imposto il gioco come terminato
                self.ended = True
            else:
                metodo = drawings[self.drawing_index]
                metodo()

            self.drawing_index += 1

        # cancello il testo nella entry box
        self.letter_entry.delete(0, tk.END)

    def check_letter(self, c):
        res = False
        for i in range(len(self.word)):
            if c == self.word[i]:
                res = True
                self.found[i] = True

        return res

    def draw_head(self):
        self.canvas.create_oval(160, 20, 240, 100, 
                                outline='blue', fill='')
    def draw_body(self):
        self.canvas.create_line(200, 100, 200, 350, fill='blue')

    def draw_left_arm(self):
        self.canvas.create_line(200, 130, 140, 200, fill='blue')

app = Impiccato()
# mainloop serve a tkinter per far partire la gestione degli eventi, tipo movimenti del mouse, pressione di tasti...
app.mainloop()
