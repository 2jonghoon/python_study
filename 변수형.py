# 파이썬 기본
# 숫자형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# 문자열
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# boolean형
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5>10))

'''
animal = "고양이" #string
name = "해피" # string
age = 4 # int
hobby = "낮잠" # string
is_adult = age >= 3 # boolean
'''
# 숫자형, boolean형은 str로 감싸줘야 문자열이다

# '+' 대신 ','로 사용 할 수 있다.
# ',' 는 띄어쓰기가 무조건 포함 이다.

'''
print("우리집 " + animal +"의 이름은 " +  name + "에요")
hobby = "공놀이"

#print(name + "는 " + str(age) + "살 입니다. " + hobby + "을 아주 좋아해요")
print(name, "는 " , age, "살 입니다. " ,hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult))
'''
# #는 한줄 주석
# ''' ''' 여러줄 주석


# 연산자
# print(1+1) # 2
# print(3-2) # 1
# print(5*2) # 10
# print(6/3) # 2

# print(abs(-5))
# print(pow(4,2)) # 4^2 = 4*4 = 16

# 수학 함수 2022.12.17
# from math import * # math 라이브러리를 쓰겠다.

# print(floor(4.19)) # 내림 
# print(ceil(3.14)) # 올림
# print(sqrt(16)) # 제곱근

# 랜덤 함수 2022.12.17

# from random import * # 랜덤함수의 모든 라이브러리를 쓰겠다.

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성
# print(int(random() * 10 + 1)) # 1 ~ 10 이하의 임의의 값 생성

# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성
# print(int(random() * 45 + 1)) # 1 ~ 45 이하의 임의의 값 생성

# 로또 숫자 출력
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성
# print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성
# print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성

# 문자열 처리 함수 2022.12.17

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "900225-1083039"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0:2 문자열의 0번째부터 2번째 앞 까지 출력
# print("월 : " + jumin[2:4]) # 2:4 문자열의 2번째부터 4번째 앞 까지 출력 
# print("일 : " + jumin[4:6]) # 4:6 문자열의 4번째부터 6번째 앞 까지 출력

# print("생년월일 : " + jumin[:6]) # :으로 시작하면 //  처음부터 6번째 앞 까지 출력
# print("주민번호 뒤 7자리 " + jumin[7:])  # 7: 7번째 부터 끝까지 출력
# print("주민번호 뒤 7자리 (뒤에서부터) : " + jumin[-7:]) # 마이너스(-) 는 뒤에서 부터 출력 함 // 맨 뒤에서부터 7번째까지 출력

# python = "Python is Amazing"
# print(python.lower()) # 모든 문자 소문자
# print(python.upper()) # 모든 문자 대문자
# print(python[0].isupper()) # 해당 문자가 대문자인지 확인 (boolean형)
# print(len(python)) # 문자열의 길이 구하기
# print(python.replace("Python", "Java"))

# index = python.index("n") # 문자열의 index 값 구함 (대,소문자 인식)
# 대문자로 변환 먼저 한 후에 index 구해야함
# python.upper()
# index2 = python.index("o")
# print(index)
# index = python.index("n", index + 1) # index 위치 + 1 에서 문자열을 찾음
# print(index)

# print(python.find("Java")) # 해당 하는 문자가 없으면 -1 로 반환
# print(python.index("Java")) # 해당 하는 문자가 없으면 오류
# print("hi")

# print(python.count("n")) # 해당 하는 문자를 카운트함

# 문자열 포맷 2022.12.17
# 방법 1
# print("나는 %d살 입니다." % 20) # %d 위치에 % 뒤에 있는 값을 넣는다. %d = 정수형
# print("나는 %s을 좋아해요." % "파이썬") # %s = 문자열
# print("Apple 은 %c로 시작해요." % "A") # %c = 문자(한글자)

#print("나는 %s살 입니다." % 20) # %s 는
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 괄호를 통해 순서대로 포맷 처리

# 방법 2
# print("나는 {}살 입니다.".format(20)) # format(값) 값을 {} 안에 넣는다.
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간")) 
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) 

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간")) # 변수처럼 사용 할 수 있다.

# 방법 4 (python v3.6 이상)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") # f로 시작하면 변수로 설정한 값을 사용 할 수 있다.

# 탈출 문자 2022.12.17
# print("백문이 불여일견 \n백견이 불여일타") # \n : 줄바꿈

# 저는 "이종훈" 입니다.
# print('저는 "이종훈"입니다')
# print("저는 \"이종훈\"입니다.") # \" 
# print("저는 \'이종훈\'입니다.") # \'

# \\ : 문장 내에서 하나의 \ 로 변경
# print("D:\sourceTree\python")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # 커서를 맨 앞으로 이동해서 \r뒤에 있는 길이 만큼 치환

# print("Redd\bApple") # \b : 백스페이스 (한글자 삭제) \b앞에 있는 글자 삭제

# print("Red\tApple") # \t 탭


# 리스트 [] 2022.12.17
# 리스트는 객체의 집합 / 배열과 같은 의미

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는지?
# print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") # append = 리스트 맨 뒤에 추가
# print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워
# subway.insert(1, "정형돈") # insert(index, object)
# print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# 정렬
# num_list = [5,2,4,3,1]
# print(num_list)
# num_list.sort()
# print(num_list)

# 순서 뒤집기
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5,2,4,3,1]
# mix_list = ["이종훈", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# 사전 2022.12.17 (딕셔너리) / {Key : Value}
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[100])

# print(cabinet.get(5, "사용 가능")) # get(값, none 이면 다른 값으로 변경)

# print(3 in cabinet) # 3 = 키 값 딕셔너리
# print(4 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 딕셔너리에 추가 하기 딕셔너리변수[키] = 값 일 시 해당 키에 값을 대입 시킴
# cabinet["C-20"] = "조세호"
# cabinet["A-3"] = "김종국"
# print(cabinet)

# 딕셔너리에서 키 빼기 del 사용
# del cabinet["A-3"]
# print(cabinet)

# Key만 출력
# print(cabinet.keys())

# Value만 출력
# print(cabinet.values())

# Key, Value 쌍으로 출력
# print(cabinet.items())

# 딕셔너리 내용 지우기
# cabinet.clear()
# print(cabinet)


# 튜플 2022.12.17 MAP과 같은 의미 / 변경되지 않는 값을 가질때 사용 / 추가 불가
# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# add 불가
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 세트 = 집합 2022.12.17
# 집합 => 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# 교집합 (java + pyhton 을 모두 할 수 있는 사람)
# print(java & python) # & = 교집합
# print(java.intersection(python))

# 합집합 (java도 할 수 있고, python도 할 수 있는 사람) (순서가 없음)
# print(java | python)
# print(java.union(python))

# 차집합 (java는 할 수 있지만 pyhton은 할 수 없는 사람)
# print(java - python)
# print(java.difference(python))

# pyhton 을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# java를 까먹은 사람
# java.remove("김태호")
# print(java)

# 자료 구조의 변경 2022.12.17
# 커피숍
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) 

# menu = list(menu)
# print(menu, type(menu)) 

# menu = tuple(menu)
# print(menu, type(menu)) 

# menu = set(menu)
# print(menu, type(menu)) 