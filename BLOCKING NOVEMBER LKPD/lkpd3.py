import turtle

def gambar_bendera():
    # Pengaturan layar
    screen = turtle.Screen()
    screen.title("Bendera Indonesia")
    screen.bgcolor("black")

    # Membuat turtle
    t = turtle.Turtle()
    t.speed(3)

    # Ukuran bendera
    lebar = 300
    tinggi = 200

    # Gambar bagian merah
    t.penup()
    t.goto(-lebar / 2, tinggi / 2)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(lebar)
        t.right(90)
        t.forward(tinggi / 2)
        t.right(90)
    t.end_fill()

    # Gambar bagian putih
    t.penup()
    t.goto(-lebar / 2, 0)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(lebar)
        t.right(90)
        t.forward(tinggi / 2)
        t.right(90)
    t.end_fill()

    # Hapus turtle
    t.hideturtle()

    # Tampilkan layar
    screen.mainloop()

# Panggil fungsi
gambar_bendera()
