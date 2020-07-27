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

# format : 문자열 형식을 미리 정하고, 인자를 주어 문자열을 완성
s = "name: {} number: {}, soccer: {}"
s.format("Ronaldo", 7, True)

"name: {name}, number: {num}".format(name = "Jordan", num = 23)

# 정수를 표현하는 여러 가지 방법
"{:d}".format(515)  #정수를 넣는다.
"{:5d}".format(515) #최소 5칸을 차지하고 정수를 넣는다.
"{:+5d}".format(515) #양수면 +를 표시한다.
"{:=+5d}".format(515)   #+를 맨 앞에 표시한다.
"{:05d}".format(515)    #빈칸은 0으로 채운다.
"{:+05d}".format(515)   #양수면 0 앞에 +를 표시한다.

# 실수를 표현하는 여러 가지 방법
"{:f}".format(11.17)    #실수를 넣는다.
"{:12}".format(11.17)   #최소 12칸을 차지하고 실수를 넣는다.
"{:12.1f}".format(11.17)    #소수점 1자리까지 반올림해서 나타낸다.