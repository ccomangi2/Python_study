#딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 됩니다.
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] # 490
lux['armor'] # 18.72

# 딕셔너리 키에 값 할당
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037    # 키 'health'의 값을 2037로 변경
lux['mana'] = 1184      # 키 'mana'의 값을 1184로 변경
lux #{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}

# 키 추가하고 값 할당
lux['mana_regen'] = 3.28    # 키 'mana_regen'을 추가하고 값 3.28 할당
lux #{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}

# 딕셔너리에서 키가 있는지 확인하고 싶다면 in 연산자를 사용하면 됩니다.
# 이렇게 not in은 특정 키가 없으면 True, 있으면 False가 나옵니다.

