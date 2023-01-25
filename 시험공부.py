'''
def in_to_cm(inch):
    cm = inch * 2.54
    return cm

num = int(input('인치를 입력하세요: '))

result = in_to_cm(num)

print('%d inch => %.2f cm' %(num, result))


ll =[1,2,3]

def f1(*arg):
    print(arg)

f1(*ll)

def dic_prn(**arg):
    print(arg.items())

dic_prn(이름 = '홍길동', 학과 = '컴퓨터학과', 학번 = '17')


def hello(name):
    print("안녕! %s!" %name)

hello('명수')
name = '정연'
hello(name)


def factorial(n):
    i = 1
    for j in range(1, n+1):
        i = i*j
    return i

print(factorial(5))
print(factorial(20))

import math

def circle(r):
    area = r**2*math.pi
    circum = 2*math.pi*r
    return area, circum

r = float(input("반지름을 입력하세요: "))

area, circum = circle(r)

print('원의 면적 : %.2f, 원주의 길이 : %.2f' %(area, circum))

def f_sum(n,m,step =1) :
    hap = 0
    for i in range(n, m,step):
        hap = hap + i
    return hap

print("0에서 100미만의 합: ", f_sum(0,100))
print(f_sum(100,200,step=3))
print(f_sum(100,200,5))

def f_sum(*arg):
    hap = 0
    for i in arg:
        hap = hap + i
    return hap

L1 = [10,20,30]
print(f_sum(1,2,3))
print(f_sum(1,2,3,4,5))
print(f_sum(*[10,20,30]))
print(f_sum(*L1))

def prn(**arg):
    for k in arg:
        print(k)

prn(x=1, y=2, z=3)


def count(arg, x = 0, y = 100):
    cnt = 0
    for i in L:
        if x <= i < y:
            cnt = cnt + 1
    return cnt

L = [95, 93, 87, 63, 95, 70, 60, 75, 88]

print(count(L,90))
print(count(L, 80, 90))



def CNT_LargerN(LL, n):
    cnt = 0
    for i in LL:
        if i > n:
            cnt = cnt +1
    return cnt 
    

L = [99,34,55,80,88,99,23,\
     100,78,99,22,87,80,91,100,87]

n = int(input("n 입력: "))

print(CNT_LargerN(L, n))

avg = sum(L)/ len(L)

print("평균값 {}보다 더 큰 수는 {}개입니다."\
      .format(avg, CNT_LargerN(L,avg)))'''







