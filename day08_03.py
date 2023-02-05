import cv2
import mediapipe as mp              # 영상모듈
# pip install mediapipe

# 만약에 OS권한문제로 설치가 안될경우
'''
# 0. python이 실행 중인지 확인한다 (만약 실행중이라면 중지버튼을 눌러 중단시킨다) 
# 1. 시작 - anaconda입력 -  anaconda Prompt 관리자권한 실행 
# 2. python -m pip install --upgrade pip를 입력해서 pip를 업그레이드 시켜줌

'''

'''
만약에 웹캠이면 VideoCapture에 0을 넣고, 맨 밑 waitKey에 1을 넣는다
'''

# 동영상 읽어줘
cap = cv2.VideoCapture('person.mp4')                    # 0으로 입력하면 웹캠
mp_fd = mp.solutions.face_detection                     # 얼굴을 찾는다
mp_draw = mp.solutions.drawing_utils                    # 찾은얼굴에 박스를 쳐준다
fd = mp_fd.FaceDetection(0.5)                           # 정확도 조정 기본값 0.5 (50%)
# 무한반복 (동영상 == 빠르게 여러 이미지를 출력0)
while True:
    # 읽기성공여부, 동영상을 자른이미지
    success, img = cap.read()
    # 동영상을 정공적으로 읽었으면  보여주기 전에 얼굴을 찾는다
    if success:
        # 얼굴찾기 정확도 향상을위해 색을 반전시켜준다 BGR --> RGB
        from_bgr_to_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      
        face = fd.process(from_bgr_to_rgb)                          # 얼굴찾기

        if face.detections:
            # 얼굴을 찾았다! ==> 사람 얼굴을 찾은다음 하고 싶은 동작
            # 함수 사용하기
            for id, detection in enumerate(face.detections):        # 각각의 순번을 매기며 튜플로 읽어준다
                # mp_draw.draw_detection(img, detection)              # mediapipe 찾은 얼굴을 사각형 표시
                fd_box = detection.location_data.relative_bounding_box
                box = int(fd_box.xmin * img.shape[1]), int(fd_box.ymin * img.shape[0]),\
                     int(fd_box.width * img.shape[1]), int(fd_box.height * img.shape[0])  # \ 넣어주면서 코드를 아래로 내릴수있다.
                cv2.rectangle(img, box, (0,0,255), 1)                  #    (붉은색 0,0,255), 두께 2
                cv2.putText(img, f'{round(detection.score[0]*100, 1)}%', \
                    (box[0],box[1]), cv2.FONT_ITALIC, 0.7, (0,0,255), 2)

        cv2.imshow('title', img) 
    if cv2.waitKey(20) & 0xFf == 27:
        # 동영상 waitKey 20~25
        # Esc키를 눌러 종료
        break
    