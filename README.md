# STFPM_AnomalyDetection
​	A improved code of "Student-Teacher Feature Pyramid Matching for Anomaly Detection" for training, testing and predicting.

​	Original Reference Code(By PyTorch): https://github.com/gdwang08/STFPM

​	Unofficial Code (By PyTorch-Lightning): https://github.com/hcw-00/STPM_anomaly_detection

​	Paper Link: https://arxiv.org/abs/2103.04257v3

# Change

​	This code is modified from hcw-00's ***STPM_anomaly_detection***, which is based on PyTorch-Lightning.

1. It can generate "**grayscale** defect detection image" (ground-truth mask), which means the image is represented by only black and white. (By LuZikang)
2. Add an **prediction** module. (By YangBin)
3. It has changed from ResNet-18 to ResNet-152. You can change back or try to use ResNet-152 as Teacher & ResNet-18 as Student.

```
├ ─ test # models saved
│   ├ ─ bottle
│   └ ─ ......
├── train.py # model training
├── detecting.py # model predicting
├── tensorboard_run.py # training result visualization
├── requirements.txt
└── README.md
```



# Dataset

​	Download Link: https://www.mvtec.com/company/research/datasets/mvtec-ad/downloads 

​	Paper Link: https://ieeexplore.ieee.org/document/8954181

# Hardware

​	It is merely for the reference of the following training result. Always not expected to get the same result data by given the same models.

|  Component    |   Description  |  Note  |
| :---------:  |  :-----: |  ------- |
| CPU          | Intel(R) Xeon(R) Gold 6138 CPU @ 2.00GHz   2.00 GHz |  |
| GPU          | None in this training | Better GPU, better training. |
| RAM          | 64.0 GB |  |

# Training

```bash
# torch==1.12.1 torchvision=0.13.1 opencv-python==4.5.2.52
pip install -r requirements.txt
```

```bash
python train.py --phase=train --dataset_path=...\mvtec_anomaly_detection --category=bottle --project_path=...\test
```

| Main Parameters | Note                                                         |
| --------------- | ------------------------------------------------------------ |
| --num_epochs    | epoch number for training                                    |
| --lr            | optimizer parameter, learning rate                           |
| --momentum      | optimizer parameter                                          |
| --weight_decay  | optimizer parameter                                          |
| --batch_size    | Set less than 4 if ensure better performance                 |
| --project_path  | the path of models saved<br />Once a model are finished in training, It can't be re-training |

# Testing

```bash
python train.py --phase=test --dataset_path=...\mvtec_anomaly_detection --category=bottle --project_path=...\test --output_path=...\output
```

# Predicting

```bash
python train.py --phase=predict --predict_path=...\mvtec_anomaly_detection --category=bottle --project_path=...\test
```

or

revise **detecting.py** and run it.

# Results

100 epochs training for each category actually.

|  Category    |   AUC-ROC(image)  |   AUC-ROC (pixel)  |
| :---------:  |  :-----: |  :-----: | 
| carpet       | 0.9662921348314606 | 0.9903472118834364 | 
| grid         | 0.9866332497911445 | 0.9871335697600007 | 
| leather      | 1.0 | 0.9945778707141713 | 
| tile         | 0.9949494949494949 | 0.9744931114416499 | 
| wood         | 0.9947 | 0.9642 | 
| bottle       | 1.0 | 0.9818796255452386 | 
| cable        | 0.8862443778110944 | 0.9194169093988306 | 
| capsule      | 0.8954926206621461 | 0.9461320936660839 | 
| hazelnut     | 0.9714285714285714 | 0.9881636024343283 |
| meta_nut     | 0.8357771260997068 | 0.8974234615548793 |
| pill         | 0.9318057828696126 | 0.9582640814865969 |
| screw        | 0.8159458905513425 | 0.983182165681811 |
| toothbrush   | 0.9333333333333333 | 0.9861350877979583 | 
| transistor   | 0.8533333333333334 | 0.8226574097914439 | 
| zipper       | 0.9726890756302521 | 0.9622075550349201 | 
| <b>average</b>      | <b>0.93590</b> | <b>0.95708</b> | 


# Citation
@inproceedings{wang2021student_teacher,
    title={Student-Teacher Feature Pyramid Matching for Anomaly Detection},
    author={Wang, Guodong and Han, Shumin and Ding, Errui and Huang, Di},
    booktitle={The British Machine Vision Conference (BMVC)},
    year={2021}
}