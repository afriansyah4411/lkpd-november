import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Trapesium dengan Python Turtle")

# Membuat turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.color("blue")
pen.speed(5)

# Fungsi untuk menggambar trapesium
def draw_trapezium():
    # Panjang sisi
    atas = 100
    bawah = 200
    tinggi = 120
    
    # Gambar trapesium
    pen.penup()
    pen.goto(-bawah/2, 0)  # Mulai dari sisi bawah tengah
    pen.pendown()
    pen.forward(bawah)  # Sisi bawah
    pen.left(120)
    pen.forward(tinggi)  # Sisi miring kiri
    pen.left(60)
    pen.forward(atas)  # Sisi atas
    pen.left(60)
    pen.forward(tinggi)  # Sisi miring kanan
    pen.left(120)

# Memanggil fungsi
draw_trapezium()

# Menyembunyikan turtle dan menampilkan hasil
pen.hideturtle()
screen.mainloop()
