import pickle

# 파일을 열어서 변수에 저장 후 출력 할 수 있다.
# with open("profile.pickle", "rb") as profile_file:
#   print(pickle.load(profile_file))
  

# with open("study.txt", "w", encoding="utf8") as study_file:
#   study_file.write("파이썬을 열심히 공부하고 있어요")
  
with open("study.txt", "r", encoding="utf8") as study_file:
  print(study_file.read())
