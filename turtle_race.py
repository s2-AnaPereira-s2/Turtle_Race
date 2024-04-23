from turtle import Turtle, Screen
import random
import winner_msg
import loser_msg

screen = Screen()
screen.title("Turtle Race")
finish_line = Turtle()
finish_line.penup()
finish_line.goto(350, 300)
finish_line.right(90)
finish_line.pensize(5)
finish_line.pendown()
finish_line.forward(500)
finish_line.hideturtle()
racers_list = []

def racers(name, color, start_point):
    name = Turtle()
    name.shape("turtle")
    name.color(color)
    name.penup()
    name.goto(-400, start_point)
    racers_list.append([name, color])


def run():
    player_choice = screen.textinput("Turtle Race", "Who is your winner? (Red, Blue, Yellow, Green or Black)")
    if player_choice is None:
        screen.bye()
    positions = []
    for _ in range(55):
        for racer in racers_list:
            racer[0].forward(random.randint(5, 21))
    for racer in racers_list:
        positions.append({"racer": racer[-1], "position": racer[0].pos()})
    winner = ""
    highest = 0
    for position in positions:
        if position["position"][0] > highest:
            highest = position["position"][0]
            winner = position["racer"]
    winner_msg.color_winner = winner
    loser_msg.color_winner = winner
    if winner.lower() == player_choice.lower():
        winner_msg.Winn()
    else:
        loser_msg.Losee()

    
racers("red", "red", 0)
racers("blue", "blue", 50)
racers("yellow", "yellow", 100)
racers("green", "green", 150)
racers("black", "black", 200)
run()






