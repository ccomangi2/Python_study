#1
# def cute_word(str):
#     bus = "삐삐삐"
#     age = "삐삐"
#     return 0
# print(cute_word("저기 152번 버스 온다."))
# print(cute_word("저는 18살입니다. 내년엔 19살이에요. 십년 전에는 8살이었어요."))
#2
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def hbalance(self):
        print("balance : ", self.balance)

    def deposit(self,up):
        self.balance += up

    def withdraw(self, down):
        if self.balance > down:
            self.balance -= down
        else:
            print("잔고가 부족합니다.")

ba = BankAccount(1000)
ba.hbalance()
ba.deposit(2000)
ba.hbalance()
ba.withdraw(5000)
ba.hbalance()
ba.withdraw(1200)
ba.hbalance()

#3
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self):
        self.x - self.x
        self.y - self.x

p1 = Point(2, 3)
p2 = Point(-2, -2)

print(p1.x)
print(p2.y)

# print(p2.distance(p2))
# print(p1.distance(p1))

#4
class App:
    def __init__(self, name, category, money):
        self.name = name
        self.category = category
        self.money = money

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

kakaottok = App('카카오똑', 'SNS', 0)
kartrice = App('카트라이스', 'game', 1000)
facecook = App('페이스쿡', 'SNS', 100)
apps = [kakaottok, kartrice, facecook]
for app in apps:
    if app.get_category() == 'SNS':
        print(app.get_name())
        
#5
class Todo:
    def __init__(self, text, priority):
        self.text = text
        self.priority = priority
    
    def get_text(self):
        return self.text
        
    def get_priority(self):
        return self.priority
    
game = Todo('게임하기', 10)
sing = Todo('노래하기', 30)
dance = Todo('춤추기', 20)
todos = [game, sing, dance]
max_priority_todo = todos[0]
for todo in todos:
    if max_priority_todo < todo:
        max_priority_todo = todo
print(max_priority_todo.get_text())

