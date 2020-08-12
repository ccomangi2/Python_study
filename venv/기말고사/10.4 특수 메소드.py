# 객체 삭제와 __del__ 메소드
class DeletaleClass:
    def __del__(self):
        print("delete")

d = DeletaleClass()
del d

# 사용자 재정의 메소드
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Person 설명, 이름은 " + self.name + " 키는 " + str(self.height)

    def __len__(self):
        return self.height

    def __getitem__(self, key):
        if key == "name":
            return self.name
        if key == "age":
            return self.age
        return None

p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])
p = Person("철수", 19, 170)
print(p)
print(len(p))
print(p['age'])
print(p['unknown'])