# 클래스 변수와 메소드 정의 형식
# class 클래스 이름:
#     [클래스 변수 정의...]
#     @classmethod
#     def 클래스 이름(cls, 추가 파라미터들...):
#         [클래스 메소드 정의...]

# 클래스 변수와 메소드 정의
class Car:
    count = 0

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        Car.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

print(Car.get_count())
c1 = Car("스포츠카", 100)
c2 = Car("트럭", 50)
print(Car.get_count())
