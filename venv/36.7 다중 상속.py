# 사람 클래스와 대학교 클래스를 만든 뒤 다중 상속으로 대학생 클래스
class Person:
    def greeting(self):
        print('안녕하세요.')

class University:
    def manage_credit(self):
        print('학점 관리')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting()  # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()  # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()  # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드

# 다이아몬드 상속

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')

class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')

class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')

class D(B, C):
    pass

x = D()
x.greeting()  # 안녕하세요. B입니다.