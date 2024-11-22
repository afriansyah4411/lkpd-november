import turtle

def gambar_persegi_panjang(t, panjang, lebar):
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(panjang)
        t.left(90)
        t.forward(lebar)
        t.left(90)
    t.end_fill()

def gambar_segitiga(t, sisi):
    t.color("yellow")
    t.begin_fill()
    for _ in range(3):
        t.forward(sisi)
        t.left(120)
    t.end_fill()

def gambar_trapezium(t, atas, bawah, tinggi):
    t.color("green")
    t.begin_fill()
    t.forward(bawah)
    t.left(120)
    t.forward(tinggi)
    t.left(60)
    t.forward(atas)
    t.left(60)
    t.forward(tinggi)
    t.left(120)
    t.end_fill()

def gambar_jajar_genjang(t, alas, tinggi, miring):
    t.color("blue")
    t.begin_fill()
    t.forward(alas)
    t.left(60)
    t.forward(miring)
    t.left(120)
    t.forward(alas)
    t.left(60)
    t.forward(miring)
    t.left(120)
    t.end_fill()

def gambar_segi_lima(t, sisi):
    t.color("purple")
    t.begin_fill()
    for _ in range(5):
        t.forward(sisi)
        t.left(72)
    t.end_fill()

# Pengaturan layar
screen = turtle.Screen()
screen.title("Gambar Bangun Datar")
screen.bgcolor("white")

# Membuat turtle
t = turtle.Turtle()
t.speed(3)

# Gambar bangun datar
t.penup()
t.goto(-300, 200)
t.pendown()
gambar_persegi_panjang(t, 150, 100)

t.penup()
t.goto(0, 200)
t.pendown()
gambar_segitiga(t, 100)

t.penup()
t.goto(-300, 50)
t.pendown()
gambar_trapezium(t, 80, 150, 100)

t.penup()
t.goto(0, 50)
t.pendown()
gambar_jajar_genjang(t, 150, 100, 100)

t.penup()
t.goto(-100, -150)
t.pendown()
gambar_segi_lima(t, 100)

# Sembunyikan turtle
t.hideturtle()

# Tampilkan layar
screen.mainloop()

