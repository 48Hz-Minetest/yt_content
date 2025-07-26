import random
import sys
import time
import turtle as tl

screen = tl.Screen() # создание сцены
screen.setup(height=600, width=400) # размер сцены (x, y)
screen.bgcolor("black") # цвет заднего фона
screen.title("Круги") # заголовок сцены

pen = tl.Turtle() # создание пера
pen.color(random.choice(["blue", "green", "lime", "yellow", "purple", "red", "lightblue"])) # выбор цвета кончика на рандом
pen.hideturtle() # скрывает перо
pen.speed(0) # скорость рисования (в моём случае максимальная)

for i in range(1, 183 + 1):
    pen.forward(i) # рисует полосы
    pen.right(i) # поворачивает полосы
    # со временем начинает формироваться вирус

pen.color("white") # меняется цвет кончика
pen.write("Готов!", align="center", font=("Courier New", 16, "normal")) # выводит сообщение о готовности, print() нельзя!
tl.done() # завершает рисование
# Выйти на Esc или кнопку 'назад'
