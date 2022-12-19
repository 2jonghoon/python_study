# 모듈은 확장자가 .py 이다.
# 같은 경로이거나 파이썬 프로젝트 안에 있어야 사용 할 수 있다.

# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)


# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 원하는 함수만 사용 할 수 있다.

# price(3)
# price_morning(4)

# from theater_module import price_soldier as soldier # 별칭을 지을 수 있다.

# soldier(5)