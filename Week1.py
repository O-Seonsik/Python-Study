# -*- coding: utf-8 -*-
#변수 (variable)
num = 123
str = "test"
print(num, str)

#연산자 (operator)
"""
기본적인 내용은 똑같으나
제곱 = **
몫 = //
"""
print(8/3.0)    # 나눈 값을 소수점 포함해서 모두 출력
print(8//3.0)   # 몫만 출력
print(2**3)     # 2^3 을 출력

print(type(num), type(str))     # 자료형 출력

#입력 (input())
inputTest=input("값을 입력하시오: ")
print(type(inputTest))