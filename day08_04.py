import cv2
import mediapipe as mp

# 비디오를 읽어줘
cap = cv2.VideoCapture('person.jpg')                    # 0으로 입력하면 웹캠

mp_fd = mp.solutions.face_detection                     # 얼굴을 찾는다
mp_draw = mp.solutions.drawing_utils                    # 찾은얼굴에 박스를 쳐준다
# 50%의 얼굴이면 얼굴로 인식
fd = mp_fd.FaceDetection(0.5)                           # 정확도 조정

# 읽은 비디오를 여러개의 이미지로
success, img = cap.read()
# 크기 조정
img = cv2.resize(img, (680, 960))
# 색보정 (정확도)
from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# 얼굴을 찾아줘
result = fd.process(from_bgr_to_rgb)


# 얼굴 찾으면 
if result.detections:
    # 각 얼굴별로
    for id, detection in enumerate(result.detections):
        mp_draw.draw_detection(img, detection)          # 네모표시

# 보여주고 기다려
cv2.imshow('title', img)
cv2.waitKey(0)
