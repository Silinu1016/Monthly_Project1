# Elevator Detection
## Description
  * Jetson TX2의 내장 카메라를 사용하여 엘리베이터 문 상태가 열려있으면 인사하는 시스템임
  * 이 코드는 엘리베이터 문이 열렸는지 닫혔는지 판단하는 부분임  


## Data
* **Collection**[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/0.%20Change_file_names.py)[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/1.%20Image%20gathering.py)
  * 엘리베이터가 보이는 위치에 노트북 카메라로 1초마다 한 번씩 촬영하여 저장함
  * 엘리베이터가 열리면 Open, 닫히면 Close로 분류함
  * Open 사진이 Close 사진에 비해 압도적으로 적음
  * 따라서 Open 사진 763장 기준으로 Close 사진도 763장을 가져옴
    ![image](https://github.com/Silinu1016/Project/assets/97217295/66d63cc3-5e46-4f04-a26f-e4134af0eda4)

* **Dataset**
  * 1,526 개
  
* **Classes**
  * Open, Close

* **Pre-processing**[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/2.%20Image%20Resize%20and%20change%20color.py)
  * 이미지 라벨링
    * python labelImg.py 사용함
    * 같은 곳을 촬영했기 때문에 모든 이미지 라벨 값을 같도록 조정함[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/2.5.%20Make%20Labeling.py)
    * 크기에 따라, 처리된 이미지에 따라 이미지 라벨링 값을 재정의함[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/3.%20Image%20Resizing%20Label.py) [[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/4.%20Convert%20Annotation%20with%20change%20color.py)
    
  * 크기
    * 원본, 엘리베이터 작게 확대한 이미지, 엘리베이터 크게 확대한 이미지
  * 처리
    * Resize, 흑백, 색반전, 모자이크
    * 아래 그림은 크기 조정된 이미지, 흑백, 색반전, 모자이크 순임
  ![image](https://github.com/Silinu1016/Project/assets/97217295/2d7fc411-5d75-46e4-ae99-f31203afcc73)
  * 이미지 학습 순서를 임의로 변환함[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/4.5.%20Mix%20order.py)

## Model[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/5.%20Training%20and%20save%20the%20weights.py)
* **Train Model**
  * YOLOv3-Tiny Fine-Tuning

* **Hyperparameter**
  * Epoch: 100
  * Learning rate: 0.001
  * Batch size: 64


## Performance
* **Architecture**
  * Close를 인식할 때는 가만히 있음
  * Open을 인식했을 때는 로봇이 엘리베이터 앞까지 가서 사람에게 인사하는 화면을 띄운 후 제자리로 돌아옴
* **Image Test**[[Link]](https://github.com/Silinu1016/Project/blob/main/Elevator%20Detection/6.%20Image%20test.py)
  * 35개의 이미지 데이터(Open: 21개, Close: 14개)
    * 휴대폰으로 찍은 사진, 노트북으로 찍은 사진을 섞음
  * 엘리베이터의 상태를 정확하게 인식한 이미지는 33개로 94% 이상의 정확도를 보임
    ![image](https://github.com/Silinu1016/Project/assets/97217295/a91b5a8c-11b0-4df9-aab0-3840c5bf3496)
* **TX2 Test**
  * 실시간으로 촬영(2[frame/s])하였을 때, 95% 이상의 정확도를 보임
    ![image](https://github.com/Silinu1016/Project/assets/97217295/3eec4693-1684-4b8b-8b56-d06613e399b6)

