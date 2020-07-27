h = "  Happy Programming!"
len(h) # 글자 수 세기
h.count("p") # h 문자열에서 인자 'p'의 개수 세기
h.upper() # 모두 대문자로 변환하기
h.lower() # 모두 소문자로 변환하기
h.strip() # 왼쪽, 오른쪽 모두 공백 없애기
h.replace("Happy", "Funny") # 문자열 대체하기
h.find("ap") # h문자열에서 인자 'ap' 왼쪽부터 찾기
h.rfind("a") # h문자열에서 인자 'a'를 오른쪽부터 찾기
h.find("z00") # 찾지 못하면 -1 리턴
"a" in h # h 문자열에 a가 있는지 확인
"amp" in h # h 문자열에 amp가 있는지 확인

x = "01::23::ab::&&"
y = x.split("::") ## x 문자열을 '::'로 나누어 리스트 만들기
", ".join(y) # y 리스트를 ', '로 이어서 문자열 만들기