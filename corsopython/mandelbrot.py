import png

# limiti x e y del piano (di Gauss)
# provare a modificarli per zoomare in certi punti del frattale
x_boundaries = [-2.0, 1.0]
y_boundaries = [-1.0, 1.0]

img_width = 750
# calcolo dell'altezza dellimmagine in base alle proporzioni
img_height  = int(img_width * (y_boundaries[1] - y_boundaries[0])/(x_boundaries[1] - x_boundaries[0]))

# come colorare?
# modificare is_in_mandelbrot in modo che max_iterations sia un terzo parametro
# ritornare i invece di vero/falso e spostare il controllo nel codice chiamante
# infine, nel caso il punto non appartenga all'insieme di Mandelbrot, invece
# di colorarlo di bianco, usare un gradiente di colore basato sul numero di 
# iterazioni fatto (ossia il valore ritornate da is_in_mandelbrot).
# Questo metodo di colorazione del frattale di Mandelbrot viene detto 
# escape time algorithm, perché si basa su quanto il punto ci mette a "uscire" dall'insieme"
def is_in_mandelbrot(x, y):
    c = complex(x,y)
    z = 0
    max_iterations = 64
    for i in range(max_iterations):
        z = z*z + c
        if abs(z) > 2:
            break

    return i == max_iterations - 1
 
x_step = (x_boundaries[1] - x_boundaries[0]) / img_width
y_step = (y_boundaries[1] - y_boundaries[0]) / img_height

# columns sarà una lista di liste, ogni lista innestata è una colonna di pixel dell'immagine
columns = []
for y in range(0, img_height):
    column = []
    set_y = y_boundaries[1] - y * y_step
    for x in range(0, img_width):
        set_x = x_boundaries[0] + x * x_step  

        if is_in_mandelbrot(set_x, set_y):
            # i tre numeri sono le componenti del colore (rosso, verde, blu) e vanno da 0 a 255
            column.append([0,0,0])
        else:
            column.append([255, 255, 255])
    columns.append(column)

png.from_array(columns, 'RGB').save('mandelbrot.png')