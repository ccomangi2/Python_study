# f1 = open("tmp/write.txt", 'w', encoding="utf-8")
#
# # 파일을 이용하여 쓰는 코드
# f1.write("안녕하세요.\n")
# f1.write("반갑습니다.")
#
# f1.close()

# 'a' = append
# f2 = open("tmp/append.txt", mode='a', encoding="utf-8")
# f2.write("append\n")
# f2.close()

with open("tmp/with.txt", 'w', newline='', encoding='utf-8') as f:
    f.write("with 구문 사용하기\n")
    f.write("2번째 줄\n")
    f.write("3번째 줄")

with open('tmp/with.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)

with open('tmp/with.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("줄 수 :", len(lines))
    for idx, line in enumerate(lines):
        print("[" + str(idx) + "]", line, end="")
    print()
