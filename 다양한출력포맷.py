# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보

# ''>10 => ''를 10자리만큼 빈자리를 채움
# print("{0: >10}".format(500))

# 양수일 땐 +로 표시, 음수일 땐 -로 표시
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<10}".format(500))

# 3자리 마다 콤마(,)를 찍어주기
# print("{0:,}".format(100000000))

# 3자리 마다 콤마(,)를 찍어주기, +- 부호도 붙이기
# print("{0:+,}".format(100000000))
# print("{0:+,}".format(-100000000))

# 3자리 마다 콤마(,)를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈 자리는 ^ 로 채우기

# :^<+30,   ==> ^ 빈자리를 ^ 채우기 / < 왼쪽정렬 / + +부호를 나타내기 / 30 30자리만큼 공간 확보 / , 3자리 만큼 , 해줌
# print("{0:^<+30,}".format(1000000000)) 

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시 ( 소수점 3번째 자리에서 반올림 하여 두번째 자리까지만 출력)
print("{0:.2f}".format(5/3))