#다음과 같이 Person 클래스에 hello 속성이 있고, Person 클래스를 상속받아 Student 클래스를 만듭니다.
#그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해봅니다.
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)  # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함