# sep는 ,를 대체해준다.
# end는 문장의 끝에 추가 해준다.
# print("Python", "Java", sep=" vs ")  
# print("Python", "Java", "Javascript", "?",sep=",",end="?")  

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력
# print("Python", "Java", file=sys.stderr) # 표준 에러

# ljust() 는 괄호안에 있는 숫자만큼 채운 후 왼쪽 정렬 
# rjust 는 오른쪽 으로 정렬

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#   # print(subject, score)
#   print(subject.ljust(8), str(score).rjust(4), sep=":") 

# 은행 대기순번표
# 001, 002, 003, ...

# zfill() 괄호안에 있는 길이 만큼 비어있으면 0을 채움
# for num in range(1, 21):
#   print("대기번호 : " + str(num).zfill(3))

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다.")