"""
split()
split()은 매개변수를 주지 않으면 " "(공백)을 기준으로 문자열을 나눈다
split()을 이용해서 한줄로 여러 입력을 받을 수 있다.
"""
# a, b=input().split()
# a=int(a)
# b=int(b)
# A
# print(a+b)
# B
# print(a-b)
# C
# print('%.10f' % (a/b))

"""
list = 배열
.append() 추가
del 삭제
"""
# list1=[]
# list2=[1,2,3,4]
#
# list2[0]=43
# print(list2)
#
# list2.append(5)
# print(list2)
#
# list1.append(5)
# print(list1)
#
# del list2[0]
# print(list2)
#
# list2.sort()
# print(list2)

"""
map은 하나의 자료형
순회가능한 데이터를 다른 형태로 한번에 형변환 시킬 수 있게 해
list로 형변환 시켜서 사용할 수 있음
"""
# list1=[]
# list1.append(1)
# list1.append(2)
# list1.append(3)
#
# print("list1:", list)
# print("원소 타입: ", type(list1[0]))
# print("list1 타입", type(list1))
#
# print("map함수", type(map(str, list1)))
#
# list2=list(map(str,list1))
# print("원소 타입: ", type(list2[0]))
# print("list2 타입", type(list2))

# D
# input()
# numList = list(map(int, input().split()))
# print(min(numList), max(numList))

# E
# numList=[]
# for i in range (0, 9):
#     numList.append(int(input()))
# print(max(numList))
# print(numList.index(max(numList))+1)

#F
# N = int(input())
# for i in range(0, N):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()

#G
# N = int(input())
# for i in range(0, N):
#     for j in range(1, N-i):
#         print(" ", end="")
#     for j in range(0, i+1):
#         print("*", end="")
#     print()