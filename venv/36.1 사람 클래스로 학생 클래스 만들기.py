# 사람 클래스를 만들고 사람 클래스를 상속받아 학생 클래스 만들기
class Person:
    def greeting(self):
        print('안녕하세요.')


class Student(Person):
    def study(self):
        print('공부하기')


james = Student()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Student에 추가한 study 메서드

# 상속 관계 확인 하는 함수 issubclass