#클래스 메서드는 다음과 같이 메서드 위에 @classmethod를 붙입니다.
#이때 클래스 메서드는 첫 번째 매개변수에 cls를 지정해야 합니다(cls는 class에서 따왔습니다).

# 사람 클래스 Person을 만들고 인스턴스가 몇 개 만들어졌는지 출력하는 메서드
class Person:
    count = 0  # 클래스 속성

    def __init__(self):
        Person.count += 1   # 인스턴스가 만들어질 때
                            # 클래스 속성 count에 1을 더함

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))  # cls로 클래스 속성에 접근

james = Person()
maria = Person()

Person.print_count()  # 2명 생성되었습니다.

