# 1부터 100까지 숫자 출력
for i in range(1, 101):    # 1부터 100까지 100번 반복
    print(i)

# 3의 배수와 5의 배수일 때 숫자 대신 'Fizz', 'Buzz'를 출력
for i in range(1, 101):    # 1부터 100까지 100번 반복
    if i % 3 == 0:         # 3의 배수일 때
        print('Fizz')      # Fizz 출력
    elif i % 5 == 0:       # 5의 배수일 때
        print('Buzz')      # Buzz 출력
    else:
        print(i)           # 아무것도 해당되지 않을 때 숫자 출력

#  3과 5의 공배수를 출력
for i in range(1, 101):              # 1부터 100까지 100번 반복
    if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
        print('FizzBuzz')            # FizzBuzz 출력
    elif i % 3 == 0:                 # 3의 배수일 때
        print('Fizz')                # Fizz 출력
    elif i % 5 == 0:                 # 5의 배수일 때
        print('Buzz')                # Buzz 출력
    else:
        print(i)                     # 아무것도 해당되지 않을 때 숫자 출력

# 논리 연산자 and를 사용하지 않고 3과 5의 공배수를 검사
for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)             # 아무것도 해당되지 않을 때 숫자 출력

# 코드 매우 단축
for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리