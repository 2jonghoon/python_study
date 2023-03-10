'''
https://docs.python.org/3/py-modindex.html
해당 사이트에서 외장 함수 모듈을 찾을 수 있다.
'''

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)

# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리 표시

# folder = "sample_dir"

# folder 가 있으면
# if os.path.exists(folder):
#   print("이미 존재하는 폴더 입니다.")
#   os.rmdir(folder)
#   print(folder, "폴더를 삭제하였습니다.")
# else:
#   os.makedirs(folder)
#   print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # 현재 파일 리스트

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td)