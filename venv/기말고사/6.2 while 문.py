# 기본적인 while 문
x = 3
while x < 6:
    print(x)
    x += 1

echo = input()
while echo != "exit":
    print(echo)
    echo = input()

while True:
    if echo == "exit":
        break
    print(echo)
    echo = input()