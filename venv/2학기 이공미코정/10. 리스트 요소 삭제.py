# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

def 특정아이템모두삭제(src, object):
    return [val for val in src if val != object]


movie_rank = ['럭키', '스플릿', '럭키', '배트맨']
a = 특정아이템모두삭제(movie_rank, "럭키")

print(a)
