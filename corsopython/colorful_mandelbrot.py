import png

# limiti x e y del piano (di Gauss)
# provare a modificarli per zoomare in certi punti del frattale
x_boundaries = [-2.0, 1.0]
y_boundaries = [-1.0, 1.0]
img_width = 750
# calcolo dell'altezza dell'immagine in base alle proporzioni
img_height  = int(img_width * (y_boundaries[1] - y_boundaries[0])/(x_boundaries[1] - x_boundaries[0]))

def mandelbrot_escape_time(x, y, max_iterations):
    c = complex(x,y)
    z = 0
    for i in range(max_iterations):
        z = z*z + c
        if abs(z) > 2:
            break

    return i
 
x_step = (x_boundaries[1] - x_boundaries[0]) / img_width
y_step = (y_boundaries[1] - y_boundaries[0]) / img_height

# columns sarà una lista di liste, ogni lista innestata è una colonna di pixel dell'immagine
columns = []
for y in range(0, img_height):
    column = []
    set_y = y_boundaries[1] - y * y_step
    for x in range(0, img_width):
        set_x = x_boundaries[0] + x * x_step  

        max_iterations = 512
        t = mandelbrot_escape_time(set_x, set_y, max_iterations)
        if t == max_iterations - 1:
            column.append([0,0,0])
        else:
            r1, g1, b1 = 3, 25, 32
            r2, g2, b2 = 252, 131, 61

            a = t/max_iterations
            column.append( [int((r2-r1)*a), g1 + int((g2-g1)*a), b1 + int((b2-b1)*a)] )
    columns.append(column)

png.from_array(columns, 'RGB').save('mandelbrot.png')

