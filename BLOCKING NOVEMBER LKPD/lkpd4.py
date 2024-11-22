import turtle

def draw_rectangle(x, y, width, height, color):
    """Draw a filled rectangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(x, y, base, height, color):
    """Draw a filled triangle."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(x + base / 2, y + height)
    turtle.goto(x + base, y)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_monas():
    # Base of Monas
    draw_rectangle(-75, -200, 150, 50, "gray")  # Bottom platform
    draw_rectangle(-50, -150, 100, 30, "darkgray")  # Middle platform
    draw_rectangle(-30, -120, 60, 20, "lightgray")  # Top platform

    # Pillar of Monas
    draw_rectangle(-10, -100, 20, 200, "white")

    # Flame at the top
    draw_triangle(-20, 100, 40, 50, "gold")  # Flame base
    draw_triangle(-15, 130, 30, 30, "orange")  # Flame tip

def main():
    turtle.speed(5)
    turtle.bgcolor("white")
    turtle.title("Gambar Monas")

    # Draw Monas
    draw_monas()

    # Finish
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
