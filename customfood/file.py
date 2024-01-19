import os
import shutil
from tqdm import tqdm  # tqdm를 import

# 원본 이미지 폴더 경로
source_folder = 'E:/food/validation/images'

# 대상 이미지 폴더 경로
destination_folder = 'E:/food/validation/images'

# 원본 이미지 폴더의 모든 하위 폴더를 반복
for root, dirs, files in os.walk(source_folder):
    for file in tqdm(files, desc='Moving Files', unit='file'):  # tqdm을 사용하여 파일 이동 진행 상황 표시
        # 파일이 .jpg 또는 .jpeg로 끝나는 경우
        if file.lower().endswith(('.jpg', '.jpeg','.png')):
            # 파일의 전체 경로 구성
            file_path = os.path.join(root, file)
            
            # 대상 폴더에 동일한 이름의 파일이 이미 있는지 확인
            destination_path = os.path.join(destination_folder, file)
            if os.path.exists(destination_path):
                print(f'Skipped: {file_path} (Already exists in destination)')
            else:
                # 파일을 대상 폴더로 이동
                shutil.move(file_path, destination_folder)

# tqdm의 close 호출 (진행 상황 표시를 마무리)
tqdm.close()
