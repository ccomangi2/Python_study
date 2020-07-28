# 매개 변수가 하나인 함수
import random
#함수 사용 --의미 파악이 쉬워지고 수정이 쉽다.
#인자 값 - 주사위 눈 수 조정. pip : 주사위 눈을 의미
def rolling_dice(pip):
    n = random.randint(1,pip)
    print(pip, "면 주사위 굴린 결과 : ", n)

rolling_dice(4)
rolling_dice(5)

# 매개 변수가 여러 개인 함수
import random
#인자 값 - 주사위 여러 번 굴리게 하자
def rolling_dice(pip, repeat):
    for r in range(1, repeat + 1):
        n = random.randint(1, pip)
        print(pip, "면 주사위 굴린 결과", r, " : ", n)

rolling_dice(6, 1)
rolling_dice(6, 2)


# 매개 변수에 가변 인수가 있는 함수
def p(*args):
    str = ""
    for a in args:
        str = str + a
    print(str)
p("★")