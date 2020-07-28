# 주사위 굴리는 프로그램
import random   #임의의 값을 얻기 위해 사용하는 random 모듈을 가져온다.

#처음 시작
n = random.randint(1,6) #1에서 6까지의 정수 중에 하나를 뽑는다.
print("결과 : ", n)
n = random.randint(1,6)
print("결과 : ", n)
n = random.randint(1,6)
print("결과 : ", n)


# 매개 변수가 없는 함수 정의하기
import random

# 함수 사용 --의미 파악이 쉬워지고 수정이 쉽다.
def rolling_dice():
    n = random.randint(1,6)
    print("6면 주사위 굴린 결과 : ", n)
rolling_dice()
rolling_dice()


# 혼자 해보기
def star():
    print("*****")
star()
star()
star()
