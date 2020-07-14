#다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.
class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

#해설
#x = Knight(health=542.4, mana=210.3, armor=38)와 같이 클래스에 값을 넣어서 인스턴스를 생성하고,
# print(x.health, x.mana, x.armor)와 같이 인스턴스 속성을 출력하고 있습니다.
# 따라서 class로 Knight 클래스를 만들고 __init__ 메서드에 매개변수로 self, health, mana, armor를 지정합니다.
# 이때 반드시 첫 번째 매개변수는 self라야 합니다. 함수 안에서는 self.health = health처럼 모든 매개변수를 그대로 속성으로 만들어줍니다.

#그다음에 x.slash()와 같이 인스턴스로 메서드를 호출하고 있으므로 Knight 클래스 안에 slash 메서드를 만들고 print로 '베기'를 출력하도록 만들면 됩니다.