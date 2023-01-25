
##08 사용자정의함수 실습 ######
##
## 함수 정의 및 호출 방법
## 다양한 유형의 함수 정의하기
##
## 함수 정의
##
## ==== 반환 값이 있는 함수 / 반환 값이 없는 함수
##
## 1) 이름 출력하는 함수  ==> 반환 값이 없는 함수
'''

 함수정의
a = ''
def hello(a):
    print("안녕! {}!".format(a))

    
 메인

hello('명수')
name='정연'
hello(name)
'''

## 2) factorial(n) 정의 후 호출하여 출력해보기
'''
 함수정의

def factorial(n):
    pak = 1
    for i in range(n):
        pak = pak * (i+1)
    return pak
   

 factorial() 함수 호출하여 결과 만들기 
print("5! =", factorial(5))
print("10! =", factorial(10))
print("20! =", factorial(20))

'''   

## ==== 반환 값이 여러 개인 함수   ==> 강의노트 25쪽 참고
## 25쪽 해보기
'''
함수정의
def f_calc(x,y):
    res1 = x+y
    res2 = x-y
    res3 = x*y
    res4 = x/y
    return res1, res2, res3, res4

메인코드
res1, res2, res3, res4 = f_calc(100,200)
print("100과 200의 사칙연산 결과는 %d, %d, %d, %.1f" %(res1, res2, res3, res4))
'''
## 3)반지름을 매개변수로 받아 원의 둘레와 면적을 계산하여 반환하는 함수
'''
def circle(a) :
    b = a**2*3.14
    c = 2*a*3.14
    return b, c

 메인코드
r = float(input('반지름을 입력하세요: '))
area, circum = circle(r)

print('원의 면적 : %.2f, 원주의 길이 :%.2f' % (area , circum))
'''


## ==== 기본값이 있는 함수 => 강의노트 21쪽 참고
## 4) 임의의 구간에 대해 step 간격으로 합을 구하는 함수  

'''
def f_sum(n1,n2,step=1):
    hap = 0
    for i in range(n1, n2, step):
        hap = hap + i 
    return hap  

print("0에서 100미만의 합:", f_sum(0, 100))
print("100+103+106+ … + 199의 합:", f_sum(100, 200, step=3))
print("100+105+110+ … + 199의 합:", f_sum(100, 200, 5))

'''
## 5) 가변 매개변수, 키워드 매개변수 가 있는 함수  => 강의노트 23쪽 참고
'''
 전달된 자료들의 합을 구하는 함수
def f_sum(*a):
    hap = 0
    for i in a:
        hap = hap + i 
    return hap

 딕셔너리 정보를 출력하는 함수
def prn(**arg) :
    for k in arg :
        print(k, arg[k]) 

L1 = [10,20,30]

print("합계: %d " % f_sum(1,2,3))
print("합계: %d " % f_sum(1,2,3,4,5))
print("합계: %d " % f_sum( *[ 10, 20, 30]))    ### 리스트인경우 앞에 *을 붙임 (튜플로변환)
print("합계: %d " % f_sum( *L1 ))

 prn() 함수호출하여 딕셔너리 출력해보기
 호출시 키워드 인수로 지정  또는 딕셔너리 형태로 인수지정

prn(x=1, y=2, z=3)
'''
##
##  6) 구간에 대한 빈도수 계산하기


def count (arg, x=0, y=100) :
    cnt = 0
    for i in arg :
        if x <= i < y:
            cnt = cnt + 1
    return cnt

L = [95, 93, 87, 63, 95, 70, 60, 75, 88]

print("90 이상 100 미만 : %d명 " % count(L, 90))
print("80 이상 90 미만 : %d명 " % count(L, 80, 90))
print("70 이상 80 미만 : %d명 " % count(L, 70, 80))
print("70 미만 : %d명 " % count(L, y=70))


##  7) 온도 변환 함수 구하기

#함수 정의
'''
def temp(x,y) :
    if x == 'c' or x =='C':
        z = (9/5 * y) + 32
    if x == 'f' or x == 'F':
        z = (y - 32) * 5/9
    return z

#메인 코드

x = input('섭씨온도를 화씨온도로 바꾸려면 C 또는 c를\n화씨온도를 섭씨온도로 바꾸려면 F 또는 f를 입력하세요 : ')

if x == 'c' or x == 'C' :
    y = int(input('섭씨온도를 입력하세요: '))
    print('섭씨 %d℃는 화씨 %.2f℉입니다.'%(y, temp(x,y)))

elif x == 'f' or x == 'F' :
    y = int(input('화씨온도를 입력하세요: '))
    print('화씨 %d℉는 섭씨 %.2f℃입니다.'%(y, temp(x,y)))

else :
    print("잘못된 입력입니다.")
'''

#  8) 임의의 값보다 큰 수를 세는 함수

def CNT_LargerN(LL, n):
    cnt = 0
    for i in LL :
        if n < i :
            cnt = cnt +1
    return cnt 

LL = [99, 34, 55, 80, 88, 99, 23, 100, 78, 99, 22, 87, 80, 91, 100, 87]

avg = sum(LL) / len(LL)

print("{}에서\nn보다 더 큰수가 몇개 있는지 확인합니다. ".format(LL))
print()
n = int(input("n 입력 : "))
print()
print("{}에서\n{}보다 더 큰 수는 {} 개입니다.".format(LL, n, CNT_LargerN(LL,n)))
print("평균값 {}보다 더 큰 수는 {} 개입니다.".format(avg, CNT_LargerN(LL, avg)))
