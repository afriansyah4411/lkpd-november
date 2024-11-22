import turtle

def drawSquare(ttl, x, y, length):
    ttl.penup()  # Angkat pena
    ttl.goto(x, y)  # Pindahkan kura-kura ke posisi awal
    ttl.setheading(0)  # Arahkan kura-kura ke timur
    ttl.pendown()  # Turunkan pena
    for count in range(4):  # Gambar 4 sisi
        ttl.forward(length)  # Maju sejauh length
        ttl.right(90)  # Belok kanan 90 derajat
    ttl.penup()  # Angkat pena

Bob = turtle.Turtle()  # Buat kura-kura bernama Bob
Bob.speed(10)  # Atur kecepatan Bob
Bob.pensize(3)  # Atur lebar garis

drawSquare(Bob, 0, 0, 100)  # Gambar persegi di (0, 0) dengan sisi 100

turtle.done()  # Tahan jendela gambar