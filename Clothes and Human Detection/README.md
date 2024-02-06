# Photo Review Quality Evaluation
## Description
  * 사진 리뷰와 해당 상품과의 관련성 판단함
  * 해당 상품과 사진 리뷰와 관련 있을 때, 단순 상품 사진, 착용 사진으로 판단함
    * 옷만 나온 사진은 단순 상품 사진으로 판단함
    * 사람이 직접 옷을 착용한 사진은 착용 사진으로 판단함

## Architecture
![image](https://github.com/Silinu1016/Project/assets/97217295/ccb3200d-20ef-4e1b-9891-45cba713579c)
1. 사진 리뷰를 YOLOv8모델에 넣어 의류 종류와 사람을 인식함
2. 의류 종류와 사람을 인식하지 못한 경우나 사람만 인식한 경우 관련 없음으로 분류함
3. 의류 종류나 의류 종류와 사람을 둘 다 인식했다면 인식한 의류 종류의 bbox 부분만 Crop함
4. Crop된 이미지의 크기만큼 해당 상품 이미지 크기를 조절함
5. Crop된 이미지를 Embedding 한 값과, 크기 조절된 해당 상품 이미지를 Embedding 한 값끼리 Cosine similarity를 비교함
6. Cosine similarity가 0.55 이상이라면 단순 상품 사진 혹은 착용 사진으로 분류되며, 그렇지 않은 경우 관련 없음으로 분류함


## Data
* **Dataset**
  * **Crawling**
    * 무신사 홈페이지 내에서 상품 및 리뷰 이미지를 크롤링 함
    * 의류 종류 별로 상품을 50~150개의 리스트로 만들어서 저장함
  * **Kaggle fashion dataset**
    * Crawling Data 중 원피스 데이터가 적어, 이를 보충하기 위함
    * 라벨 값으로 원피스가 있는 데이터만 수집함
    * 아래 링크에서 다운 받을 수 있음
      * https://www.kaggle.com/datasets/nguyngiabol/colorful-fashion-dataset-for-object-detection?resource=download
  * **Kaggle scene dataset**
    * 옷과 사람이 없는 사진을 입력으로 넣었을 때 모델이 인식하지 않는 것을 테스트하기 위함
    * 아래 링크에서 다운 받을 수 있음
      * https://www.kaggle.com/datasets/nitishabharathi/scene-classification
  
* **Classes**
  * Top, Outer, Pants, Onepiece, Skirt, Human

* **Pre-processing**
  * 이미지 라벨링
    * python ImgLabel.py 사용함
  * 크기
    * (256, 256) 사이즈로 크기 조정함
  * 처리
    * 색반전, 모자이크, 흑백
    * 아래 그림은 기존 이미지, 색반전, 모자이크, 흑백 순임
      ![image](https://github.com/Silinu1016/Project/assets/97217295/ab4c0184-4aae-4431-a9ce-be2c622ff1c6)


## Model
* **Train Model**
  * YOLOv8s Fine-Tuning
  * YOLOv8m Fine-Tuning
  * YOLOv8l Fine-Tuning

* **Hyperparameter**
  * Epoch: 200(Early Stopping 가능함)
  * Patience: 30
  * Image size: 256


## Performance
* **Image Test**
