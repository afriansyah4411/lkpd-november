import turtle as t
import colorsys as cs

# Mengatur kecepatan turtle dan ukuran jendela
t.speed(10)
t.setup(800, 800)
t.tracer(10)
t.width(2)
t.bgcolor("black")

# Membuat pola bunga
for j in range(25):
    for i in range(15):
        # Menghasilkan warna menggunakan HSV (Hue, Saturation, Value)
        t.color(cs.hsv_to_rgb(i/15, j/25, 1))
        
        # Menggambar kelopak bunga
        t.right(90)
        t.circle(200-j*4, 90)
        t.left(90)
        t.circle(200-j*4, 90)
        
        # Menggambar bagian tengah bunga
        t.right(180)
        t.circle(50, 24)

# Menyembunyikan kura-kura dan menjaga jendela tetap terbuka
t.hideturtle()
t.done()
