#import travel.thailand # 모듈이나 패키지만 import 가능하며 class 나 함수는 불가하다.
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from 에서는 모듈 or 패키지 or class or 함수가 사용 가능하다.
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__

from travel import * # travel 이라는 패키지에 있는 모든걸 쓰겠다는 뜻인데 범위를 설정 해줘야 한다.
trip_to = thailand.ThailandPackage()
trip_to.detail()

# 모듈, 패키지 위치

import inspect # inspect.getFile( 클래스 또는 함수 또는 패키지 ) 파일 위치 찾기 
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))

