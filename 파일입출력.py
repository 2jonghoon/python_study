# 파일명, "w" = write, encoding="utf8"
# score_file = open("score.txt", "w", encoding="utf8")

# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# "a" => 덮어쓰기 (append) / ★ file.write 시에는 줄바꿈이 없어서 줄바꿈을 따로 명시해줘야함!
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# "r" => 읽기 (read)
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# readline => 한줄별로 읽기 후 커서를 다음 줄로 이동
score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")

# while문으로 반복하여 처리
# while True:
#   line = score_file.readline()
#   if not line:
#     break
  
#   print(line, end="")


# list로 처리
lines = score_file.readlines() # readlines ==> list 형태로 저장
for line in lines:
  print(line, end="")

score_file.close()