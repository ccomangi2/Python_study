#이때는 super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해줍니다. 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식입니다.
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()  # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'

james = Student()
print(james.school)
print(james.hello)
print(james.hello)