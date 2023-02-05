# opencv 모듈추가
# mediapipe 모듈추가

# 이미지 (좌측 상단에 이름 putText)

# 동영상 (좌측 상단에 이름 putText)

# 웹캠 (얼굴찾기) - 테스트는 동영상으로

import cv2
import mediapipe as mp

im_man = cv2.imread('man.jpg')

cv2.putText(im_man,'eumpyo', (0,20), cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 255), 1)




vd_man = cv2.VideoCapture('man.mp4')

while True:
    success, img = vd_man.read()
    if success:
        cv2.resize(img, (460,960))
        cv2.putText(img,'eumpyo', (0,20), cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 255), 1)
        cv2.imshow('title',img)
    if cv2.waitKey(20) & 0xFf == 27:
        break





