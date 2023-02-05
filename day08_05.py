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

cv2.putText(vd_man,'eumpyo', (0,20), cv2.FONT_HERSHEY_PLAIN, 2,(0, 0, 255), 1)
cv2.resize(vd_man, [460,960])
vd_man.read()
cv2.imshow('title',vd_man)
cv2.waitKey(0)



