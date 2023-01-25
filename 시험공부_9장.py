'''
import random

L = []

for i in range(10):
    L.append(random.randint(1,100))

computer = random.choice(L)

cnt = 0

while True:
    you = int(input("컴퓨터가 숨긴 수를 맞춰보세요(1~100) : "))
    
    if you > computer :
        print("틀렸습니다.\n더 작은 수를 선택하세요.")
        cnt = cnt + 1
    elif you < computer:
        print("틀렸습니다.\n더 큰 수를 선택하세요.")
        cnt = cnt + 1
    else:
        cnt = cnt + 1
        print("빙고! %d만에 맞췄네요. 컴퓨터가 숨긴 수는 %d입니다."\
        %(cnt, computer))
        break
'''
import turtle
import random

tt=turtle.Turtle("turtle")
turtle.title("다양한 색깔과 크기의 원을 만들어보기")
turtle.setup(width = 600, height = 600)
tt.speed(10)

for i in range(20):
    rr= random.randint(1,100)
    tt.penup()
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    tt.goto(x,y)
    tt.pendown()
    r=random.random()
    g=random.random()
    b=random.random()   
    tt.begin_fill()
    tt.color(r,g,b)
    tt.circle(rr)
    tt.end_fill()




