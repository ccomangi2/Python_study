# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

def 아이템삽입(src, index, object):
    result = src
    result[index:index] = [object]
    return result


movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
a = 아이템삽입(movie_rank, 1, "슈퍼맨")

print(a)
