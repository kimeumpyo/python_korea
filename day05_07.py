# import가 안되는 이유 : 설치가 안된 라이브러리(모듈) 또는 오타
# 외부 모듈 설치 : pip install

# pip install python-opencv     (아나콘다 파이썬)
# pip install opencv-python     (아나콘다 파이썬)           안될시 exit() 입력을 해본다.
import cv2

# img = cv2.imread('img1.png')            # 이미지를 읽어줘
# cv2.imshow('title', img)                # 보여줘     

# cv2.waitKey(0)                          # 무한대기

def 이미지(파일명):

    img = cv2.imread(파일명)            
    cv2.imshow('title', img)             
    cv2.waitKey(0)

# 이미지('../img/cat.jpg')  # 뒤로가기(../) 후 img파일에 있는 cat.jpg 를 찾는다 
이미지('img/cat.jpg')
이미지('img/flower.jpg')                         
