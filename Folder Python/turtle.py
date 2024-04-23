import turtle

# Fungsi untuk menggambar kepala binatang
def gambar_kepala():
    turtle.circle(50)

# Fungsi untuk menggambar badan binatang
def gambar_badan():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.circle(70)

# Fungsi untuk menggambar kaki binatang
def gambar_kaki():
    turtle.penup()
    turtle.goto(-30, -120)
    turtle.pendown()
    for _ in range(4):
        turtle.forward(60)
        turtle.backward(60)
        turtle.right(90)

# Fungsi untuk menggambar ekor binatang
def gambar_ekor():
    turtle.penup()
    turtle.goto(0, -120)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(70)
    turtle.backward(140)
    turtle.forward(70)

# Fungsi utama untuk menggambar binatang
def gambar_binatang():
    turtle.speed(1)
    gambar_kepala()
    gambar_badan()
    gambar_kaki()
    gambar_ekor()
    turtle.done()

# Panggil fungsi utama untuk menggambar binatang
gambar_binatang()
