# 함수 2022.12.17

# 함수 정의 시 def 
# def open_account():
#   print("새로운 계좌가 생성되었습니다.")

# open_account()


# def deposit(balance, money):
#   total = balance + money
#   print("입금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(total))
#   return total

# def withdraw(balance, money):
#   if(balance >= money):
#     total = balance - money
#     print("출금이 완료 되었습니다. 잔액은 {0}원 입니다.".format(total))
#     return total
#   else:
#     print("출금이 완료 되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))  
#     return balance
  
# def widhraw_night(balance, money): 
#   comission = 100
#   total = balance - money - comission
#   return comission, total


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)

# comission, balance = widhraw_night(balance, 500)
# print("수수료 {0}원이며, 잔액은 {1}원 입니다.".format(comission, balance))

# 함수 기본값 설정 2022.12.17

# def profile(name, age, main_lang):
#   print("이름 : {0}\t나이 : {1}\t 주 언어 : {2}"\
#     .format(name, age, main_lang))
  

# 기본 키
# def profile(name, age = 17, main_lang = "파이썬"):
#   print("이름 : {0}\t나이 : {1}\t 주 언어 : {2}"\
#     .format(name, age, main_lang))
    
# profile("유재석")
# profile("김태호")

# 키워드 값
# def profile(name, age, main_lang):
#   print(name, age, main_lang)
  
# profile(name="유재석", main_lang="파이썬", age=25)
# profile(main_lang="자바", age=20, name="김태호")

# 가변인자
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#   print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#   print(lang1, lang2, lang3, lang4, lang5)
  
# def profile(name, age, *language): # 몇개의 인자값이 올지 모르기에 *변수 로 선언
#   print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#   for lang in language:
#     print(lang, end=" ")
#   print()
  
  
# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 23, "Kotlin", "Swift")

# 지역변수 : 함수 호출 내에 선언했다가 함수가 끝나면 사용 X
# 전역변수 : 함수 밖에서 선언하여 계속 사용 가능

# gun = 10

# def checkpoint(soldiers):
#   global gun # 전역 공간에 있는 gun 사용
#   gun = gun - soldiers
#   print("[함수 내] 남은 총 : {0}".format(gun))


# def checkpoint_ret(gun, soldiers):
#   gun = gun - soldiers
#   print("[함수 내] 남은 총 : {0}".format(gun))
#   return gun


# print("전체 총 : {0}".format(gun))
# #checkpoint(2)
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))