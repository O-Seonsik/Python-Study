#반복문(while)
"""
반복문 사용 시 조건문과 마찬가지로 Indentation 지켜야한다.
강제로 while문 탈출 시 break사용
한 단계의 반복을 넘어갈 땐 continue 사
"""
i = 2
while i <= 100:
    if i%2 == 0:
        print(i, end=" ")
        #end="" 를 하면 print()에 포함된 줄바꿈이 사라짐.
        #end=" "를 하면 각 출력 사이에 공백(" ")이 생김
    i+=1

#1부터 10까지 합
i = 1
result = 0
while i <= 10:
    result += i
    i+=1

print("\n%s" %result)

#숫자 맞추기 게임2
num = 50
while True:
    result = int(input("답 입력: "))
    if num == result:
        print("정답")
        break
    else:
        print("다시 입력")


#리스트
"""
여러 개의 자료들을 모아서 하나의 묶음으로 저장(배열)
리스트에 노드 추가 list이름.append("value")
리스트는 0부터 시작
"""

#반복문(for)
"""
기존의 continue를 똑같이 사용 가능
range()함수, range(초기 값, 종료 값, 증가 값)
초기 값이 없으면 0으로, 증가 값이 지정되지 않으면 1로 자동으로 설정 
"""
for i in [1, 2, 3, 4, 5]:
    print(i)

for i in range(5):
    print("%d번 째"%(i+1))

#구구단 출력
dan=int(input("출력할 단: "))
for i in range(1, 10):
    print("%d x %d = %d"%(dan, i, dan*i))

#팩토리얼 계산
n=int(input("정수 입력: "))
result=1
for i in range(2, n+1):
    result *= i
print("%d의 팩토리얼 값은 %d"%(n, result))

#HW1
for i in range(2, 101):
    if i%2 == 0:
        print(i, end=" ")

#HW2
result = 0
for i in range(1, 11):
    result += i
print(result)

arr = [5, 6, 3, 6]

for i, j in enumerate(arr):
    print(i, j)