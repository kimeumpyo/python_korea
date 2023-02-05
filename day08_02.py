import cv2

# pip install python-opencv     cv가 비활성시 터미널에 2개를 입력해준다
# pip install opencv-python

def ShowImage(img_path):
    # 이미지 읽어줘
    img = cv2.imread(img_path)
    # 이미지 보여줘
    cv2.imshow('title', img)
    # 무한대기
    cv2.waitKey(0)

def ShowVideo(video_path):
    # 동영상 읽어줘
    vc = cv2.VideoCapture(video_path)
    # 무한반복 (동영상 == 빠르게 여러 이미지를 출력0)
    while True:
        # 읽기성공여부, 동영상을 자른이미지
        success, img = vc.read()
        # 동영상을 정공적으로 읽었으면
        if success:
            cv2.imshow('title', img)
        if cv2.waitKey(20) & 0xFf == 27:
            # 동영상 waitKey 20~25
            # Esc키를 눌러 종료
            break

def ShowCam():
    # 캠 읽어줘
    vc = cv2.VideoCapture(0)
    # 화면 조정
    vc.set(3, 640)      # 3 : 가로
    vc.set(4, 480)      # 4 : 세로
    # 무한반복 (동영상 == 빠르게 여러 이미지를 출력)
    while True:
        # 읽기성공여부, 자른이미지
        success, img = vc.read()
        # 동영상을 정공적으로 읽었으면
        if success:
            cv2.imshow('title', img)
        if cv2.waitKey(1) & 0xFf == 27:              # 27 : Esc
            # 캠 : wahiKey 1
            # Esc 를 눌러 종료
            break

# ShowImage('person.jpg') 
# ShowVideo('person.mp4')
ShowCam()