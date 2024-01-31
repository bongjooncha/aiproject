from ultralytics import YOLO
import wandb

if __name__ == '__main__':
    wandb.init(project="foodyolo")
    wandb.run.name='2nd try'

    model = YOLO('yolov8n.pt')
    model.train(data='./data.yaml', epochs=100, batch=32, imgsz = 800, save_dir="./runs/detect")
    # model.val()