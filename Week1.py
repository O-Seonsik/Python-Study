# -*- coding: utf-8 -*-
# 변수 (variable)
num = 123
text = "test"
print(num, text)

# 연산자 (operator)
"""
기본적인 내용은 똑같으나
제곱 = **
몫 = //
"""
print(8/3.0)    # 나눈 값을 소수점 포함해서 모두 출력
print(8//3.0)   # 몫만 출력
print(2**3)     # 2^3 을 출력

print(type(num), type(text))     # 자료형 출력

# 입력 (input())
"""
input은 항상 입력을 문자열로 받아온다
그러므로 string이 아닌 경우는 자료형의 변환이 필요
int(), float(), str()
"""
print("type(num) = ", type(num))
num=input("입력하세요 : ")
print("type(num) = ", type(num))
num=int(input("입력하세요 : "))  # string에서 int로 형 변
print(type(num))

# 문자열 연산하기
"""
1.'+'는 여러 문자열을 합치는데 사용, 하지만 문자열 이외의 값에 시도하면 오류 발생
str()을 활용해서 해결 가능
2.'*'는 문자열 곱하기
문자열을 연속해서 만듦
3.문자열의 길이는 내장함수 len()을 활요하면 가능
띄어쓰기도 문자열에 포함
"""
print("이름: " + "오선식")
print("학번: " + str(201620866))
print("=" *10)
print("start python")
print("=" *10)
a = "Life is too short"
print(len(a))

# 문자열 인덱싱
"""
1. 0부터 시작
2. 음수를 인덱스로 사용 가능
음수 인덱스는 -1부터 시작
즉 제일 마지막 인덱스는 -1로 표현 가능
"""
print(a[-1], a[0])

# 문자열 슬라이싱
"""
':'을 기준으로 좌측이 시작 우측이 마지막 인덱스 번호이다
좌측 인덱스부터 포함하여 우측 인덱스 -1까지 인덱스에
해당하는 문자를 순차적으로 포함하는 문자열을 만든다.
"""
print(a[0:4], a[5:6])

# 문자열 포멧팅
print("I like %d apples." %3)
print("I eat %s apples."%'three')
print("I eat %d %s."%(3, "apples"))  #2개 이상일 경우에는 괄호로 표기

# Format() 포멧팅
"""
형식: "문자열{}".format()
-()소괄호를 이용해 값을 대입
-{}중괄호 안에 변수명이나 숫자를 지정하여 순서를 지정 가능
"""
print("I eat {0} apples.".format(5))
print("I eat {0} apples.".format('five'))
print("{1} {0} {2}".format(0, 1, 2))
print("{aaa} {bbb}".format(aaa='a', bbb='b'))
