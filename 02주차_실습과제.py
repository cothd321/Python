#변수 a에 10, 변수 b에 20을 저장하고 a+b, a*b 확인하기

a=10; b=20
print("a={}, b={}일 때".format(a,b), "a+b={}, a*b={}".format((a+b),(a*b)))
print("a={}, b={}일 때 a+b={}, a*b={}".format(a,b,(a+b),(a*b)))
print("a=%d, b=%d일 때 a+b=%d, a*b=%d" %(a,b,(a+b),(a*b)))


#삼각형의 면적을 구하는 프로그램을 작성하자

h=10
w=20

print(h*w/2)


#키가 171인 사람의 표준체중 구하기

h=171

print("표준체중=(키-100)*0.9")
print("키={}".format(h))
print("표준체중=",(h-100)*0.9,sep='')


#간단한 계산기 프로그램

print("a,b를 입력 받아 a+b, a-b, a*b, a/b를 구합니다")

a=int(input("a 입력: "))
b=int(input("b 입력: "))

print("%d + %d = %d" %(a, b, a+b))
print("%d - %d = %d" %(a, b, a-b))
print("{} * {} = {}" .format(a, b, (a*b)))

