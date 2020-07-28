# 셋 생성
game = {"LOL", "Overwatch", "Tetris", 1942, 2048}
set("Funny")        #{'n', 'F', 'y', 'u'}
set([2048, "Tetris", "Cube"])   #{2048, 'Cube', 'Tetris'}
set((2560, 1440))               #{2560, 1440}
set({"google":"google.com", 18:"unesco.org"})   #{18, 'google'}
set(range(3))   #{0, 1, 2}

# set(문자열) : 문자열의 문자가 하나씩 셋의 요소로 들어간다.
# set(리스트) : 리스트의 각 요소가 하나씩 셋의 요소로 들어간다.
# set(튜플) : 튜플의 각 요소가 하나씩 셋의 요소로 들어간다.
# set(딕셔너리) : 딕셔너리의 키가 하나씩 셋의 요소로 들어간다.
# set(range()) : range() 함수의 각 요소가 하나씩 리스트의 요소로 들어간다.

# 셋에 추가
game.add("Fifa")    #{2048, 'LOL', 'Fifa', 1942, 'Overwatch', 'Tetris'}
game.update(("NBA", "MLB"))  #{2048, 'MLB', 'LOL', 'Fifa',  'NBA', 1942, 'Overwatch', 'Tetris'}

# 셋에서 제거
game.remove("LOL")      #{2048, 'MLB', 'Fifa',  'NBA', 1942, 'Overwatch', 'Tetris'}

# 셋 연산
s3 = {3, 6, 9, 12}      #교집합
s4 = {4, 8, 12, 16}
s3 & s4
s3.intersection(s4) 

s3 | s4                 #합집합
s3.union(s4)

s3 - s4                 #차집합
s3.union(s4)

s3 ^ s4                 #대칭 차집합
s3.symmetric_difference(s4)