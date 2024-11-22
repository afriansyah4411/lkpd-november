import turtle

# Pengaturan layar
screen = turtle.Screen()
screen.title("Bangun Datar: Persegi Panjang")
screen.bgcolor("white")

# Membuat objek turtle
pen = turtle.Turtle()
pen.pensize(3)  # Ketebalan garis
pen.color("blue")
pen.fillcolor("lightblue")  # Warna isi
pen.speed(3)  # Kecepatan menggambar

# Ukuran persegi panjang
panjang = 200
lebar = 100

# Menggambar persegi panjang
pen.begin_fill()
for _ in range(2):
    pen.forward(panjang)  # Garis horizontal
    pen.left(90)
    pen.forward(lebar)    # Garis vertikal
    pen.left(90)
pen.end_fill()

# Menyelesaikan gambar
pen.hideturtle()

# Menunggu pengguna menutup jendela
screen.mainloop()
