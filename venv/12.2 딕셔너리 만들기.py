#딕셔너리는 { }(중괄호) 안에 키: 값 형식으로 저장하며 각 키와 값은 ,(콤마)로 구분해줍니다.

#딕셔너리 = {키1: 값1, 키2: 값2}
#그럼 키와 값이 4개씩 들어있는 딕셔너리를 만들어보겠습니다.
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

#키 이름이 중복된다면?
lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']    # 키가 중복되면 가장 뒤에 있는 값만 사용함 #490은 저장되지 않음
