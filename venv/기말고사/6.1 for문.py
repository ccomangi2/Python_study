# 기본적인 for문
# range() 함수의 각 결과가 변수로 대입되어 반복한다.
for x in range(3, 9, 2):
    print(x)

# 문자열의 각 문자가 하나씩 변수로 대입되어 반복한다.
for ch in "LOVE":
    print(ch)

# 리스트의 각 요소가 하나씩 변수로 대입되어 반복한다.
for item in ["힙합", "발라드"]:
    print(item + "즐겨듣는다.")

# 튜플의 각 요소가 하나씩 변수로 대입되어 반복한다.
for item in (2560, 1440):
    print(item)

# 딕셔너리의 키가 하나씩 변수로 대입되어 반복한다.
pl = {"C":1972, "Java":1995, "Python":1991}
for key in pl:
    print(key, ":", pl[key])

# 셋의 각 요소가 하나씩 변수로 대입되어 반복한다.
for item in {"HTML5", "CSS3", "JavaScript"}:
    print(item + "를 할 수 있다.")


# 중첩 반복문
for i in range(1, 9+1):
    print("2 X {} = {}".format(i, 2*i)) #구구단 2단

for dan in range(2, 5+1):
    for i in range(1, 9+1):
        print("{} X {} = {}".format(dan, i, dan*i))
    print('---------------')

# break, continue 문
for i in range(1, 9+1):
    if i == 7:
        break
    print("2 X {} = {}".format(i, 2*i))

for i in range(1, 9+1):
    if i % 2 == 0:
        continue
    print("2 X {} = {}".format(i, 2*i))