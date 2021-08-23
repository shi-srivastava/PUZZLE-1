import turtle


def start_game():
    global game_state
    game_state = "game"


# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Game Setup
wn = turtle.Screen()
wn.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
wn.title("Game State Demo by TokyoEdTech")
wn.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()

# Keyboard Bindings
wn.listen()
wn.onkeypress(start_game, "s")

game_state = "gameover"

# Main Game Loop
while True:

    # Clear the screen
    pen.clear()

    # Game code here
    if game_state == "splash":
        wn.bgpic("bg.gif")

    elif game_state == "game":
        wn.bgpic("bg.gif")

    elif game_state == "gameover":
        wn.bgpic("bg.gif")

    # Update the screen
    wn.update()
