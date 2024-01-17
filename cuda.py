import torch

# CUDA 사용 가능 여부 확인
cuda_available = torch.cuda.is_available()

if cuda_available:
    # 현재 사용 가능한 CUDA 디바이스 수 확인
    num_cuda_devices = torch.cuda.device_count()
    print(f"CUDA를 사용할 수 있습니다. 현재 {num_cuda_devices}개의 CUDA 디바이스가 이용 가능합니다.")
else:
    print("CUDA를 사용할 수 없습니다.")