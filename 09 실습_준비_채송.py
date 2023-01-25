####  09 모듈 실습 #####

### ============= 사용자정의 모듈(계산기 모듈 만들기)

## 먼저 calculator.py 계산기 모듈 만들기
# 더하기/빼기/곱하기/나누기 함수 정의


## 방법1)

'''
import calculator

num1 = float(input("첫번째 숫자를 입력하세요 : "))
num2 = float(input("두번째 숫자를 입력하세요 : "))

print("더하기 : %.f" %calculator.plus(num1, num2))
print("빼기 : %.f" %calculator.minus(num1, num2))
print("곱하기 : %.f" %calculator.multiply(num1, num2))
print("나누기 : %.2f" %calculator.divide(num1, num2))



## 방법2)

# from ~ import ~ 로 불러오기

from calculator import plus, minus, multiply, divide
 

num1 = float(input("첫번째 숫자를 입력하세요 : "))
num2 = float(input("두번째 숫자를 입력하세요 : "))


print("더하기 : %.f" %plus(num1,num2))
print("빼기 : %.f" %minus(num1,num2))
print("곱하기 : %.f" %multiply(num1,num2))
print("나누기 : %.2f" %divide(num1,num2))
'''

####  random module
'''
import random

# random()  출력해보기 

print(random.random())

# 10~100 사의의 임의의 값 출력하기  ==> randint()

print(random.randint(10,100))

# 100 미만의 랜덤 값 10개 리스트 만들기       ===> 18쪽 참고

ll = []

for i in range(10):
    ll.append(random.randint(1,100))


# 가위바위보 게임 만들기에서 컴퓨터가 내는 값 지정하기

option = ["가위", "바위", "보"]

while True :
    me = input("가위, 바위, 보 중 하나를 선택하세요. ")
    com = random.choice(option)  ## 세 옵션 중에 하나를 선택해서 지정하기

    print("computer: {}" .format(com))

    if me == com :
        print("비겼습니다.")

    else :
        if (me == "가위" and com == "보") or (me == "바위" and com == "가위") or (me == "보" and com == "바위"):
            print("이겼습니다.")
        else :
            print("졌습니다.")
    
'''

##### ============== 컴퓨터가 숨긴수 맞추기

'''
print("컴퓨터가 숨긴 수를 맞춰보세요(1~100)")

import random
import time 

computer = random.randint(1,100)

count = 1

t1 = time.time()

while True : 

    me = int(input("숫자를 입력하세요. "))
    
    
    if me > computer :
        print("틀렸습니다.")
        print("더 작은 수를 선택하세요.")
        count = count + 1
    
    if me < computer :
        print("틀렸습니다.")
        print("더 큰 수를 선택하세요.")
        count = count + 1

    if me == computer :
        t2 = time.time()
        print('빙고! %d번만에 맞췄네요. 컴퓨터가 숨긴 수는 %d입니다.' %(count, computer))
        print('숨긴 수를 맞출 때 까지 %.3f초 걸렸습니다.'%(t2 - t1))
        break
'''        


### 터틀그래픽 다중원그리기  31쪽

import random
import math
import turtle

'''
tt = turtle.Turtle("turtle")

tt.speed(10)

for i in range(12):
    tt.circle(100)
    tt.left(30)
    
### 터틀그래픽 다각형 함수 32쪽


def polygon(tt, size, angle):
    for i in range(angle):
        tt.forward(size)
        tt.left(360/angle)

polygon(tt, 100, 12)

'''

### ============== 다양한 색깔과 크기의 원을 만들어 보기 
'''
tt = turtle.Turtle("circle")

turtle.setup(width = 600, height = 600)

tt.speed(0)

for i in range(20) :
    tt.penup()
    tt.goto(random.randint(-300, 300), random.randint(-300, 300))
    tt.pendown()
    r = random.random()
    g = random.random()
    b = random.random()
    tt.begin_fill()
    tt.color(r,g,b)
    tt.circle(random.randint(1,100))
    tt.end_fill()
''' 
    
    






