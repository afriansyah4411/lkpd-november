import turtle

# Fungsi untuk menggambar belah ketupat
def gambar_belah_ketupat():
    screen = turtle.Screen()
    screen.title("Gambar Belah Ketupat")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(3)
    t.color("blue")
    
    # Panjang sisi belah ketupat
    sisi = 100
    
    # Mulai menggambar belah ketupat
    for angle in [60, 120, 60, 120]:  # Sudut belah ketupat
        t.forward(sisi)
        t.left(angle)
    
    t.hideturtle()
    screen.mainloop()

# Panggil fungsi
gambar_belah_ketupat()

