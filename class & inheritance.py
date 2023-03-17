####  클래스

## 클래스 정의
## 생성자 정의
## 상속 개념

## 클래스 정의 및 안스턴스 생성 기본과정

# Student 클래스 만들기
'''
class Student:
    name = "Hong"
    age = 20

    def Info(self):
        print("이름 : %s" %self.name)
        print("나이 : %s" %self.age)



# 공통적인 속성과 기능은?

 
##       print("이름 : %s" %self.name)
##        print("나이 : %s" %self.age)


# 인스턴스 생성

stu1 = Student()
stu1.Info()
print(stu1.name)
stu2 = Student()
stu2.name = 'kkk'
print(stu2.name)
'''
## 생성자 함수를 사용하여 초기화  
'''
class Student :
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def Info(self):
        print("이름 : %s" %self.name)
        print("나이 : %s" %self.age)

stu1 = Student("Hong",20)
stu1.Info()

stu2 = Student("kim", 15)
stu2.Info()
# 속성과 메소드 접근하기

stu1.Info()
stu2.Info()
print(stu1.name, stu1.age)
print(stu2.name, stu2.age)

'''

# 접근자(getter)와  설정자(setter) 지정해보기 
'''
class Student :

    
    def __init__(self , val_name='', val_age=0):
        self.name = val_name
        self.age = val_age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def setName(self, name):
        self.name = name



stu1 = Student("Hong", 20)

print(stu1.name, stu1.age)
print(stu1.get_name(), stu1.get_age())
 
stu2 = Student("Hong", 20)

s1 = Student()
print(s1.get_name(), s1.get_age())
s1.setName('kim')
print(s1.get_name(), s1.get_age())

###  ==> 기본값으로 처리하자
'''


### 상속(Inheritance)
'''
class Student :
    
    def __init__(self , val_name='', val_age=0):
        self.name = val_name
        self.age = val_age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def setName(self, name):
        self.name = name

class Boys(Student) :

    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height 
    
##    def get_height(self, height):
##        self.height = height
##        return self.height

    def get_height(self, height):
        return height
    
    

b1 = Boys('hong', 10, 130)

print(b1.get_name(), b1.get_age(), b1.get_height(125))

# 자식 클래스 정의

'''

#원 클래스 정의 및 다양한 원 객체 만들기

## 1) 원 클래스를 만들어 5개의 크기, 색깔이 다른 원을 만든다

class Circle :

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color

## 2) 메인코드
        
import random

ll = ["빨강", "파랑", "노랑", "초록", "보라"]

for i in range(5):
    ci = Circle(random.randint(1,10), random.choice(ll))
    print("반지름이 %d, 면적이 %.1f이고 %s인 원" %(ci.radius, ci.radius**2*3.14, ci.color))

print()

#부모클래스 Circle과 자식클래스 Cylinder

## 1) 부모 클래스 Circle

class Circle:

    def __init__(self, radius):
        self.radius = radius 

    def getRadius(self):
        return self.radius

    def setRadius(self):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

class Cylinder(Circle):

    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def sarea(self):
        return (super().area()) * 2 + (super().perimeter() * self.height)

    def volume(self):
        return super().area() * self.height

cy = Cylinder(3,5)
print('원통 체적: %.2f' %cy.volume())
print('원통 표면적: %.2f' %cy.sarea())

