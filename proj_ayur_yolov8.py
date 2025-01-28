# -*- coding: utf-8 -*-
"""proj_Ayur_YoloV8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M-1nMq7MM3dUwmUdA1Eja0ry8RrCZmcC
"""

!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="zHgBM1jmPuOc14x2S7zo")
project = rf.workspace("project-ayur").project("ayur-leave-yolo-new")
version = project.version(2)
dataset = version.download("yolov8")

pip install ultralytics

import os
import shutil
import random
from tqdm.notebook import tqdm

from google.colab import drive
drive.mount('/content/drive')

import ultralytics
ultralytics.checks()

!yolo task=detect mode=train model=yolov8x.pt data=/content/Ayur-leave-yolo-new-2/data.yaml epochs=10 batch=16 project=/content/drive/MyDrive/ayurproj/training_result name=ayur_proj save=True

!yolo task=detect mode=train model=/content/drive/MyDrive/ayurproj/training_result/ayur_proj5/weights/best.pt data=/content/drive/MyDrive/ayurproj/data.yaml epochs=50 batch=16 project=/content/drive/MyDrive/ayurproj/training_result name=ayur_proj save=True

!yolo task=detect mode=train \
model=/content/drive/MyDrive/ayurproj/training_result/ayur_proj_improved4/weights/best.pt \
data=/content/Ayur-leave-yolo-new-2/data.yaml \
epochs=30 \
batch=28 \
imgsz=640 \
lr0=0.0002 \
lrf=0.25 \
optimizer=SGD \
momentum=0.927 \
weight_decay=0.0005 \
patience=5 \
label_smoothing=0.20 \
augment=True \
mosaic=1.0 \
mixup=0.2 \
project=/content/drive/MyDrive/ayurproj/training_result \
name=ayur_proj_improved \
save=True

!yolo task=detect mode=predict model=/content/drive/MyDrive/ayurproj/training_result/ayur_proj_improved4/weights/best.pt conf=0.2 source=/content/Ayur-leave-yolo-new-2/valid/images save=true

