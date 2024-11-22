import turtle

# Membuat layar turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Gambar Segitiga")

# Membuat pen turtle
pen = turtle.Turtle()
pen.color("blue")
pen.pensize(3)

# Menggambar segitiga
pen.penup()
pen.goto(-100, -50)  # Titik pertama
pen.pendown()
pen.goto(100, -50)   # Titik kedua
pen.goto(0, 100)     # Titik ketiga
pen.goto(-100, -50)  # Kembali ke titik pertama

# Menyelesaikan gambar
pen.hideturtle()

# Menjaga layar tetap terbuka
screen.mainloop()
