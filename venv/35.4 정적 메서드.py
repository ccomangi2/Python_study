# 정적 메서드는 매개변수에 self를 지정하지 않습니다.
# @staticmethod처럼 앞에 @이 붙은 것을 데코레이터라고 하며 메서드(함수)에 추가 기능을 구현할 때 사용합니다.
# 데코레이터는 'Unit 42 데코레이터 사용하기'에서 자세히 설명하겠습니다.

# 덧셈과 곱셈을 하는 클래스를 만들어보겠습니다.
class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 20)  # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)  # 클래스에서 바로 메서드 호출