import turtle
import random

def start_game(x, y):
    global num_players, obstacles, boosts

    # Запит кількості гравців з перевіркою
    while True:
        try:
            num_players = int(screen.textinput("Кількість гравців", "Введіть кількість гравців (1-5):"))
            if 1 <= num_players <= 5:
                break
            else:
                screen.textinput("Помилка", "Введіть число від 1 до 5. Натисніть OK і спробуйте ще.")
        except:
            screen.textinput("Помилка", "Невірне введення. Введіть число від 1 до 5. Натисніть OK і спробуйте ще.")

    print(f"Кількість гравців: {num_players}")

    # Малювання поля
    pen.clear()
    pen.penup()
    pen.goto(-350, -250)
    pen.pendown()
    pen.color("black")
    pen.pensize(3)
    for _ in range(2):
        pen.forward(700)
        pen.left(90)
        pen.forward(500)
        pen.left(90)

    start_x, start_y = -350, -200
    finish_x, finish_y = -350, 200

    # Лінії старту і фінішу
    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()
    pen.color("blue")
    pen.forward(700)

    pen.penup()
    pen.goto(finish_x, finish_y)
    pen.pendown()
    pen.color("red")
    pen.forward(700)

    # Написи "Старт" і "Фініш"
    pen.penup()
    pen.goto(start_x - 40, start_y - 20)
    pen.color("blue")
    pen.write("Старт", font=("Arial", 16, "bold"))
    pen.goto(finish_x - 40, finish_y + 20)
    pen.color("red")
    pen.write("Фініш", font=("Arial", 16, "bold"))

    pen.hideturtle()

    # Створення перешкод
    obstacles = []
    for _ in range(10):
        obs = turtle.Turtle()
        obs.shape("triangle")
        obs.color("black")
        obs.penup()
        obs.goto(random.randint(-300, 300), random.randint(-150, 150))
        obstacles.append(obs)

    # Створення бустів
    boosts = []
    for _ in range(5):
        boost = turtle.Turtle()
        boost.shape("circle")
        boost.color("gold")
        boost.shapesize(0.7)
        boost.penup()
        boost.goto(random.randint(-300, 300), random.randint(-150, 150))
        boosts.append(boost)

    # Створення гравців
    turtles = []
    colors = ["red", "blue", "green", "yellow", "gray"]
    shapes = ["turtle", "circle", "square", "triangle", "arrow"]
    for i in range(num_players):
        t = turtle.Turtle()
        t.color(colors[i])
        t.shape(shapes[i])
        t.penup()
        t.goto(start_x + (700 / (num_players + 1)) * (i + 1), start_y)
        t.setheading(90)
        t.pendown()
        turtles.append(t)

    # Створення тексту стану гонки
    status_pen = turtle.Turtle()
    status_pen.penup()
    status_pen.hideturtle()
    status_pen.goto(0, 220)

    # Швидкість кожної черепашки (індивідуальний діапазон)
    speed_ranges = [ (1, 7), (2, 9), (3, 8), (1, 10), (2, 6) ]

    def update_status():
        leading_turtle = max(turtles, key=lambda t: t.ycor())
        leader_color = leading_turtle.color()[0]
        distance_to_finish = max(0, finish_y - leading_turtle.ycor())
        status_pen.clear()
        if int(distance_to_finish) > 0:
            status_pen.write(f"Лідирує: {leader_color}, До фінішу: {int(distance_to_finish)}", align="center", font=("Arial", 16, "normal"))
        else:
            status_pen.goto(0, 0)
            status_pen.write(f"Перемогла черепашка кольору {leader_color}", align="center", font=("Arial", 18, "bold"))

    race_in_progress = True
    while race_in_progress:
        for i, t in enumerate(turtles):
            min_spd, max_spd = speed_ranges[i]
            distance = random.randint(min_spd, max_spd)
            t.forward(distance)

            # Перешкоди
            for obs in obstacles:
                if t.distance(obs) < 20:
                    t.right(90)
                    t.forward(10)
                    t.left(90)

            # Бусти
            for boost in boosts:
                if t.distance(boost) < 20:
                    t.forward(20)  # Бонус
                    boost.goto(1000, 1000)  # Ховаємо

            if t.ycor() >= finish_y:
                race_in_progress = False
                winner = t.color()[0]
                status_pen.goto(0, 0)
                status_pen.write(f"Перемогла черепашка кольору {winner}", align="center", font=("Arial", 18, "bold"))
                break
        update_status()

# Основні об'єкти
screen = turtle.Screen()
pen = turtle.Turtle()

# Кнопка старту
pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)
pen.end_fill()

# Текст на кнопці
pen.penup()
pen.goto(0, -20)
pen.color("white")
pen.write("Почати гру", align="center", font=("Arial", 16, "bold"))
pen.hideturtle()

# Відстеження кліку
screen.onscreenclick(start_game, 1)
screen.mainloop()


