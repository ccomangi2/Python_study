# 딕셔너리 생성
d = {}      #빈 딕셔너리
urls = {"google":"google.com", 18:"unesco.org"}

# 딕셔너리에 요소 추가
urls["x"] = 2560        #키 x가 딕셔너리에 없으면 , 추가한다. ({'google':'google.com', 18:'unesco.org,', 'x':2560})

# 딕셔너리에 요소 수정
urls["x"] = 2560        #키 x가 딕셔너리에 있으면, 수정한다. ({'google':'google.com', 18:'unesco.org,', 'x':1920})

# 딕셔너리에서 요소 제거
del urls["x"]           #키 x 제거
urls.pop(18)            #키 18만 뺌
urls.clear()            #전부 다 제거

# 딕셔너리에서 요소 검색
urls = {"google":"google.com", 18:"unesco.org"}
urls["google"]                  #키 'google'의 값을 가져온다.
urls.get("google")              #키 'google'의 값을 가져온다.
"google" in urls                #키 'google'이 있는지 확인한다.
"google.com" in urls            #키 'google.com'이 있는지 확인한다.
"google.com" in urls.values()

# 키 in 딕셔너리 : 딕셔너리에 키가 있는지 확인한다.
# 값 in 딕셔너리.values() : 딕셔너리에 값이 있는지 확인한다.

# 기타 딕셔너리 관련 함수
len(urls)       #2
urls.keys()     #dict_keys(['google',18])
urls.values()   #dict_values(['google.com', 'unesco.org')]
urls.items()    #dict_items([('google', 'google.com'), (18, 'unesco.org')])

# 딕셔너리.keys() : 딕셔너리의 키들을 dict_keys 객체로 리턴한다.
# 딕셔너리.values() : 딕셔너리의 값들을 dict_vlaues 객체로 리턴한다.
# 딕셔너리.items() : 딕셔너리의 키와 값의 쌍을 묶어 dict_items 객체로 리턴한다.