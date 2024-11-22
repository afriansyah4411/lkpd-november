import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Gambar Jajar Genjang")
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.pensize(3)
pen.color("blue")
pen.speed(3)

# Fungsi untuk menggambar jajar genjang
def draw_parallelogram(base, side, angle):
    pen.forward(base)         # Sisi bawah
    pen.left(180 - angle)     # Sudut miring
    pen.forward(side)         # Sisi miring
    pen.left(angle)           # Sudut lurus
    pen.forward(base)         # Sisi atas
    pen.left(180 - angle)     # Sudut miring lagi
    pen.forward(side)         # Sisi miring terakhir
    pen.left(angle)           # Kembali ke awal

# Gambar jajar genjang
base_length = 150
side_length = 100
angle = 60  # Sudut antara sisi bawah dan sisi miring

draw_parallelogram(base_length, side_length, angle)

# Selesai
pen.hideturtle()
screen.mainloop()
