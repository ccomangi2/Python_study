# nums = [1, 2, 3, 4, 5]
# a = sum(nums)
# b = a/len(nums)
# print(b)

def 평균(src):
    result = src
    for i in range(len(src)):
        a = sum(src, 0.0)
        result = a/len(src)
    return result

리스트 = [1, 2, 3, 4, 5]
a = 평균(리스트)

print(a)
