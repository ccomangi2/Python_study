a = [0, 0, 0, 0, 0]
b = a

a is b # True


b = a.copy()

a is b # False
