from ultralytics import YOLO
import wandb


wandb.init(project="foodyolo")

model = YOLO('yolov8n.pt')
model.train(data='./data.yaml', epochs=100, patience=30, batch=64, save_dir='C:/Users/OWNER/Desktop/coding_project/aiproject/customfood/')
model.val()