# 반복문 for

# for waiting_no in range(1,6):    
#   print("대기번호 : {}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#   print("{0}, 커피가 준비 되었습니다.".format(customer))

# 반복문 while
# customer = "토르"
# index = 5
# while index >= 1:
#   print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#   index -= 1 # 한번씩 줄여 나감 java의 -- 감소 와 같은 의미
#   if index == 0:
#     print("커피는 폐기처분 되었습니다.")

# customer = "아이언맨"
# index = 1
# while True:
#   print("{0}, 커피가 준비 되었습니다. 호출 {1}회".format(customer, index))
#   index += 1

# customer = "토르"
# person = "Unknown"
# while person != customer :
#   print("{0}, 커피가 준비 되었습니다.".format(customer))
#   person = input("이름이 어떻게 되세요? ")

# 반복문 continue 와 break

# absend = [2, 5] 
# no_book = [7]
# for student in range(1, 11):
#   if student in absend:
#     continue
    
#   elif student in no_book:
#     print("오늘 수업 여기까지. {0}는 교무실로 오세요.".format(student))
#     break  
#   print("{0}, 책을 읽어봐요".format(student))

# 한 줄 for문

# students = [1,2,3,4,5]
# students = [i+100 for i in students]

# print(students)

# 길이로 반환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)