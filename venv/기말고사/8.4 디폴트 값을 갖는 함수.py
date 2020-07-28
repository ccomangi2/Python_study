# 기본 인자 값을 가지는 함수
def hello(msg="안녕하세요"):
    print(msg + "!")

hello("오랜만이에요")
hello("이영희")
hello()

# 기본 인자 값이 가변 객체인 함수
def fn(a, b=[]):
    b.append(a)
    print(b)

fn(3)
fn(5)
fn(10)


# 디폴트 값을 갖는 함수의 호출
def hello(name, msg="안녕하세요", feeling="♡"):
    print(name + "님, " + msg, feeling)

hello("아무개")
hello("김철수", "오랜만이에요")
