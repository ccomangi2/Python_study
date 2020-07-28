# 기본 if 문
x = int(input())
if x % 2 == 0:
    print("짝수")
else:
    print("홀수")

# print() 함수 : 화면에 문자열로 출력한다.
# input() 함수 : 사용자의 입력을 기다리고, 문자열로 입력받는다.

# if ~ elif ~ else 문
x = int(input())
if x % 4 == 0:
    print("4의 배수")
elif x % 3 == 0:
    print("3의 배수")
elif x % 2 == 0:
    print("2의 배수")