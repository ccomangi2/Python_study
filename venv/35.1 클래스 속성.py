#이제 간단하게 사람 클래스에 클래스 속성으로 가방 속성을 넣고 사용해보겠습니다.
#다음과 같이 Person 클래스에 바로 bag 속성을 넣고, put_bag 메서드를 만듭니다.
# 그리고 인스턴스 두 개를 만든 뒤 각각 put_bag 메서드를 사용합니다.
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff) #클래스 이름으로 클래스 속성에 접근


james = Person()
james.put_bag('책')

maria = Person()
maria.put_bag('열쇠')

print(james.bag)
print(maria.bag)

#가방에 물건을 넣는 간단한 동작을 만들었습니다.
#그런데 결과가 좀 이상하죠? james와 maria 인스턴스를 만들고 각자 put_bag 메서드로 물건을 넣었는데,
# james.bag과 maria.bag을 출력해보면 넣었던 물건이 합쳐져서 나옵니다. 즉, 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유합니다.