# 논리 연산자를 이용한 여러 조건의 제어문
x = int(input())
if x > 10 and x % 2 == 0:
    print("10초과 짝수")
    
# 중첩 제어문
x = int(input())
if x > 10:
    if x % 2 == 0:
        print("10 초과 짝수")
    else:
        print("10 초과 홀수")
else:
    print("10 이하")