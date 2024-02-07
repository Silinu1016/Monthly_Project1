# Finger Detection
## Description
  * 손가락의 숫자를 실시간으로 인식하는 것을 목표로 함
  * YOLOv8 모델을 커스터마이징한 데이터로 학습해보기 위함

## Data
* **Collection**[[Link]](https://github.com/Silinu1016/Project/blob/main/Finger%20Detection/1.%20webcam%EC%9C%BC%EB%A1%9C%20%EC%9E%90%EB%A3%8C%20%EC%88%98%EC%A7%91.ipynb)
  * 손이 보이는 위치에 웹캠으로 1[ms]마다 한 번씩 촬영하여 저장함
    
* **Dataset**
  * 334 개
  
* **Classes**
  * Finger_0, Finger_1, Finger_2, Finger_3, Finger_4, Finger_5

* **Pre-processing**
  * 이미지 라벨링[[Link]](https://github.com/Silinu1016/Project/blob/main/Finger%20Detection/2.%20image%20labeling.ipynb)
    * python labelImg.py 사용함
  * 크기[[Link]](https://github.com/Silinu1016/Project/blob/main/Finger%20Detection/3.%20Image%20preprocessing%20%EB%B0%8F%20train%2C%20val%20%EB%82%98%EB%88%84%EA%B8%B0.ipynb)
    * (416, 416) 크기로 조정함


## Model[[Link]](https://github.com/Silinu1016/Project/blob/main/Finger%20Detection/4.%20Custom%20Data%20Training%20and%20Predict.ipynb)
* **Train Model**
  * YOLOv8 Fine-Tuning

* **Hyperparameter**
  * Epoch: 200(Early Stopping 가능함)
  * Patience: 30
  * Image size: 416


## Performance[[Link]](https://github.com/Silinu1016/Project/blob/main/Finger%20Detection/5.%20Load%20weights%20and%20test%20with%20webcam.ipynb)
* **Image Test**
  * 22개의 이미지 데이터
    * 휴대폰으로 촬영한 사진임
  * YOLOv8n - 8개, YOLOv8s - 10개, YOLOv8m - 12개, YOLOv8l - 12개의 정답을 맞춤
    * 데이터를 가공하여 증강을 한다면 더 잘 맞출 수 있을 것이라 예상함
    * 모든 모델이 속도 측면에서 20ms 이내로 빠른 시간 내에 예측하는 것을 확인함
    
* **WebCam Test**
  * 실시간으로 촬영(100[frame/s])하였을 때, 80% 이상의 정확도를 보임 <br>
    ![croped_test_with_webcam](https://github.com/Silinu1016/Project/assets/97217295/396c6204-fc12-47dc-aff0-068c1346e179)

## Blog Link
1. Webcam으로 데이터 수집하기 : https://silinu-ai.tistory.com/9
2. 이미지 라벨링하기 : https://silinu-ai.tistory.com/10
3. Image preprocessing 및 train,val 나누기 : https://silinu-ai.tistory.com/11
4. Yolov8 모델로 커스텀 데이터 학습하기 및 예측하기 : https://silinu-ai.tistory.com/12
5. 학습된 Yolo 가중치 불러오기 및 실시간 웹캠에 적용하기 : https://silinu-ai.tistory.com/13
