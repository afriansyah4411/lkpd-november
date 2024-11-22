import turtle

# Buat jendela gambar dan atur warna latar belakang menjadi putih
screen = turtle.Screen()
screen.bgcolor("white")

# Buat kura-kura baru dan atur kecepatannya ke paling cepat
pen = turtle.Turtle()
pen.speed(0)

# Atur warna pengisian menjadi merah dan mulai pengisian
pen.fillcolor("red")
pen.begin_fill()

# Gambar lingkaran dengan radius 100 pixel
pen.circle(100)

# Akhiri pengisian dan hentikan penggambaran
pen.end_fill()

# Sembunyikan kura-kura
pen.hideturtle()

# Jaga jendela gambar tetap terbuka sampai ditutup secara manual
turtle.done()
