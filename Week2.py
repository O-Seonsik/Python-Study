# 문자열 안에 작은 따옴표 포함
"""
1. 문자열을 큰 따옴표(")로 감싼다.
2. Escape Character 를 사용한다
"""
num="python's favorite food is perl"
print(num)

say ='\'Python is very easy\'. he say'
print(say)

# 줄바꿈은 \n
print("Hello\nPython")
print("강한친구 대한육군\n강한친구 대한육군")

# 문자열 관련 함수
"""
len() = 길이를 반환, count() = 인자값과 동일하는 문자 개수 반환
upper() = 소문자 -> 대문자 변환
lower() = 대문자 -> 소문자 변환
"""
a="12345"
print(len(a))
a="1 2345"
print(len(a))
a="hobby"
print(a.count('b'))
a="apapalae"
print(a.count('a'))
str1=input()
print(str1.upper().count("A"))

#할당 연산자
cnt = 2
cnt **= 10;
print(cnt)

#조건문
"""
if-else
if-elif
조건문 사용시 들여쓰기 tab을 맞춰줘야한다 혹은 space 4개!
Python은 {} (Bracket)을 사용하지 않음
들여쓰기 안하면 오류가 발생해요!!!!!!!
"""
name = input("당신은 오선식? ")
if name == '오선식' :
    print("안녕하세요")
else :
    print("아니 당신은!?")

#논리 연산자
"""
and, or, not
"""
print(True or False)

#HW #2
score = int(input("점수를 입력하세요 : "))
if score >= 90:
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')