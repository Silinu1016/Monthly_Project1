# Elevator Detection
## Description
  * Jetson TX2의 내장 카메라를 사용하여 엘리베이터 문 상태가 열려있으면 인사하는 시스템임
  * 이 코드는 엘리베이터 문이 열렸는지 닫혔는지 판단하는 부분임  


## Data
* **Collection**
  * 엘리베이터가 보이는 위치에 노트북 카메라로 1초마다 한 번씩 촬영하여 저장함
  * 엘리베이터가 열리면 Open, 닫히면 Close로 분류함
  * Open 사진이 Close 사진에 비해 압도적으로 적음
  * 따라서 Open 사진 763장 기준으로 Close 사진도 763장을 가져옴
    ![image](https://github.com/Silinu1016/Project/assets/97217295/66d63cc3-5e46-4f04-a26f-e4134af0eda4)

* **Dataset**
  * 1,526 개
  
* **Classes**
  * Open, Close

* **Pre-processing**
  * 이미지 라벨링
    * python labelImg.py 사용함
  * 크기
    * 원본, 엘리베이터 작게 확대한 이미지, 엘리베이터 크게 확대한 이미지
    * 크기에 따라 이미지 라벨링 값을 재정의 함
  * 처리
    * 흑백, 색반전, 모자이크
    * 아래 그림은 기존 이미지, 흑백, 색반전, 모자이크 순임
  ![image](https://github.com/Silinu1016/Project/assets/97217295/2d7fc411-5d75-46e4-ae99-f31203afcc73)


## Model
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
* **Image Test**
  * 35개의 이미지 데이터(Open: 21개, Close: 14개)
    * 휴대폰으로 찍은 사진, 노트북으로 찍은 사진을 섞음
  * 엘리베이터의 상태를 정확하게 인식한 이미지는 33개로 94% 이상의 정확도를 보임
    ![image](https://github.com/Silinu1016/Project/assets/97217295/a91b5a8c-11b0-4df9-aab0-3840c5bf3496)
* **TX2 Test**
  * 실시간으로 촬영(2[frame/s])하였을 때, 95% 이상의 정확도를 보임
    ![image](https://github.com/Silinu1016/Project/assets/97217295/3eec4693-1684-4b8b-8b56-d06613e399b6)

