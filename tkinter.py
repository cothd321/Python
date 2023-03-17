##다각형 표현하기
'''
from tkinter import *
import random
import turtle

win = Tk()
win.title("다양한 다각형 표현하기")

drw = Canvas(win, width = 500, height = 500)
drw.pack()

t = turtle.RawTurtle(drw)
t.shape("arrow")

def poly(size, angle):
            for i in range(angle): 
                t.forward(size)
                t.left(360/angle)
                
def create_circle():
    num = int(in_num.get())

    for i in range(num):
        t.penup()
        t.goto(x = random.randint(-200, 200), y = random.randint(-200, 200))
        t.pendown()
        t.begin_fill()
        r = random.random()
        g = random.random()
        b = random.random()
        t.color(r, g, b)
        poly(random.randint(1, 50),  random.randint(3,12))
        t.end_fill()
            
la_txt = Label(win, text = " 다양한 다각형 표시하기 \n다각형을 표현할 개수 입력")
la_txt.pack(side = LEFT)

in_num = Entry(win)
in_num.pack()

btn = Button(win, text = "확인", command = create_circle)
btn.pack(side = RIGHT)

win.mainloop()
'''

##게임 만들기

from tkinter import *
import random

win = Tk()
win.title("컴퓨터가 숨긴 수를 맞춰보세요")

computer = random.randint(1,100)
cnt = 1

def func_guess():
    global cnt
    guess = int(my_guess.get())

    if guess == computer:
        result.configure(text = "빙고!~ 축하합니다. {}번만에 맞췄네요~".format(cnt))

    elif guess > computer:
        cnt = cnt + 1 
        result.configure(text = "틀렸습니다. \n더 작은 수를 선택하세요.")
        
    else :
        cnt = cnt +1
        result.configure(text = "틀렸습니다. \n더 큰 수를 선택하세요.")
        

def func_reset():
    cnt = 1
    computer = random.randint(1,100)
    result.configure(text = "게임을 다시 시작합니다.")


first = Label(win, text = "컴퓨터가 숨긴 수를 맞춰보세요")
result = Label(win, text = "1~100사이 컴퓨터가 숨긴 수를 맞춰보세요")
my_guess = Entry(win)
btn1 = Button(win, text = "확인", bg = "yellow", command = func_guess)
btn2 = Button(win, text = "게임 다시 시작", bg = "yellow", command = func_reset)


first.pack()
my_guess.pack()
btn1.pack()
btn2.pack()
result.pack()

win.mainloop()
