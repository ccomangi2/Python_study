# 리스트와 튜플의 요소 개수 구하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
len(a) # 10
b = (1, 2, 3, 4, 5)
len(b) # 5

# range의 숫자 생성 구하기
len(range(0, 10, 2)) # 5

# 문자열 길이 구하기
hello = 'Hello, world!'
len(hello) # 13

# UTF-8 문자열의 바이트 수 구하기 - utf-8 한글 글자 하나의 바이트는 3
hello = '안녕하세요'
len(hello.encode('utf-8')) # 15
