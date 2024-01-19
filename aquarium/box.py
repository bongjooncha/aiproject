import cv2
import numpy as np

# 이미지 경로
image_path = r'c:\Users\OWNER\Desktop\coding_project\aiproject\aquarium\aqa_data\test.jpg'

# 이미지 불러오기
image = cv2.imread(image_path)

# 네모 박스의 좌표와 크기
box_coordinates = (start_x, start_y, end_x, end_y)  # 이 값은 실제로 계산되어야 합니다.

# 네모 박스 그리기
cv2.rectangle(image, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

# 이미지 출력
cv2.imshow('Detected Penguin', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
