#### 07 딕셔너리  실습 ######

## 딕셔너리 생성 및 출력 
## 딕셔너리 접근 (값 변경)
## 딕셔너리 함수
## 딕셔너리  활용 


#### ============== 생성  및 출력
## 딕셔너리 기본 구조
 
stu = {'학과': '컴퓨터학부', '학번': 1000, '이름':'김아름'}

print(stu)
print(stu['이름'])
print(stu['학번'])
print('길이 : %d ' % len(stu))
print()


## dict 함수로 생성하기
'''
 
  
print("d1=", d1)

  

print("d2=", d2)

A=['a','b','c']
B=[11,22,33]

 

print("d3=",d3)
'''
 
## ==========  값 변경 및 삭제

## 학과 수정    
##stu['학과'] = '통계학과'
## 연락처 추가
##stu['연락처'] =  '010-1111-2222'
'''
print(stu)

del stu['학과']

print(stu)
# del stu
print(stu)
print()

'''

# =========== 딕셔너리 반복처리 (for 문으로 하나씩 순회하여 출력하기)
'''
#방법 1)

for s in stu :
    print(s, ':', stu[s])
print()

#방법 2)

for s in stu.keys() :
    print(s)
print()

#방법 3)

for x, y in stu.items() :
    print(x, y)
 
print()

#방법 4)

for v in stu.values() :
    print(v)
 
print()
'''
## ========= 딕셔너리 함수
'''


# key 리스트 만들기

print(stu.keys())
print(list(stu.keys()))
print(keylist)
print(stu.items())
print(stu.get('이름'))
'''
# 딕셔너리 추가 또는 수정 update()
'''
stu = {'학과': '컴퓨터학부', '학번': 1000, '이름':'김아름'}

# 방법1

stu['주소'] = '서울 은평구'

print(stu)

# 방법2 ==> update 함수 이용 : 변경 또는 추가

stu.update({'학과':'간호학과'})
stu.update({'연락처':'010-1111-1111'})
print(stu)
'''


### 딕셔너리 참조하여 문제 해결

name = '김최고'
s = {'국어': 95, '수학': 99, '영어': 94, '음악': 100,
     '사회': 84, '과학':88, '미술' : 95, '체육' : 99}
print(s)

# 수학 점수 수정 99로

s.update({'국어':100})

print(s)
print()

# 전체 평균은

#방법 1) 딕셔너리 s에서 

sum_s = 0
for k in s :
    sum_s = sum_s + s[k]
print(round(sum_s/len(s),2))


print()


#방법 2) s.keys()

sum_s = 0

for i in s.keys():
    sum_s = sum_s + s[k]

avg = sum_s / len(s)

print("%s의 평균 : %.2f" %(name,avg))

print()

#방법 3) s.values()

sum_s = 0
for i in s.values() :
    sum_s = sum_s + i
avg = sum_s / len(s)
print("%s의 평균 : %.2f" %(name,avg))

print()

#방법 4) s.items

sum_s = 0

for i in s :
    sum_s = sum_s + s[i]

avg = sum_s / len(s)

print("%s의 평균 : %.2f" %(name,avg))
print()

sum_s = 0

for k, v in s.items() :
    sum_s = sum_s + v

avg = sum_s/ len(s)

print("%s의 평균 : %.2f" %(name,avg))
print()
# 90점 이상인 과목은 몇개? 

cnt = 0

for i in s.values():
    if i >= 90 :
        cnt = cnt +1

print("90점 이상인 과목 갯수 : %d " %cnt )
print()

#최고점수?
large = max(s.values())
print("최고 점수인 과목은? ", end = '')
for i in s :
    if s[i] == large :
            print(i , end = '')
print()
print("과목 중 최고 점수는? : %d점" %max(s.values()))
print()

### 실험결과를 딕셔너리 자료로 저장하고,
###각 실험자의 평균데이터를 딕셔너리에 담아보자

s = {'홍' : [90, 80, 150], '김' : [33, 23, 89, 90],
     '정' : [79, 110, 99, 98, 23], '오' : [76, 88, 192, 90]}

result = {}

for i in s:
    avg = sum(s[i]) / len(s[i])
    avg = round(avg, 1)
    result.update({i:avg})
print("실행결과 :")
print(result)


    

