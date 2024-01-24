from ultralytics import YOLO
import wandb

if __name__ == '__main__':
    wandb.init(project="foodyolo")

    model = YOLO('yolov8n.pt')
    model.train(data='./data.yaml', epochs=5, batch=48, save_dir='./', lr0=0.01)
    model.val()