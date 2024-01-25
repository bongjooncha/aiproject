from ultralytics import YOLO
import wandb

if __name__ == '__main__':
    wandb.init(project="foodyolo")

    model = YOLO('yolov8n.pt')
    model.train(data='./data.yaml', epochs=5, batch=56, imgsz = 480)
    model.val()