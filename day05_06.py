# 외부 함수를 사용하는 법 : import
# 모듈 : 부품

# import 모듈명
# import 모듈명 as 별명
# from 모듈명 import 함수명


# import 모듈명
# import matplotlib.pyplot 

# lst = [10,20,10,30,40,90,60,10,40,30]
# matplotlib.pyplot.hist(lst)             # 막대그래프로 그려줘
# matplotlib.pyplot.show()                # 보여줘


# import 모듈명 as 별명
# 모듈명을 plt로 사용
import matplotlib.pyplot as plt
# 모듈 중에 font_manager와 rc 부분만 가져옴
from matplotlib import  font_manager, rc
# 외부 폰트를 가져와 한들을 표시가능.
font = font_manager.FontProperties(fname='gulim.ttc').get_name()
rc('font',family=font)

lst = [10,20,10,30,40,90,60,10,40,30]
plt.title('분포도')         # 제목을 표시
plt.xlabel('점수')          # x축 제목
plt.ylabel('갯수')          # y축 제목
plt.hist(lst)             # 막대그래프로 그려줘
plt.show()                # 보여줘

