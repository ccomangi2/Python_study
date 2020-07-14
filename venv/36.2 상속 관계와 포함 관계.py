#하지만 학생 클래스가 아니라 사람 목록을 관리하는 클래스를 만든다면 어떻게 해야 할까요?
#다음과 같이 리스트 속성에 Person 인스턴스를 넣어서 관리하면 됩니다.
class Person:
    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []  # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):  # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)