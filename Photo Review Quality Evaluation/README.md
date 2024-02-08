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
5. Crop된 이미지와 크기 조절된 해당 상품 이미지를 각각 ResNet 모델로 Embedding 함
6. Crop된 이미지를 Embedding 한 값과, 크기 조절된 해당 상품 이미지를 Embedding 한 값을 Cosine similarity를 비교함
7. Cosine similarity가 0.55 이상이라면 단순 상품 사진 혹은 착용 사진으로 분류되며, 그렇지 않은 경우 관련 없음으로 분류함
   * 3~6번은 프로그래머스 최종 프로젝트 종료 후에 개별적으로 진행함

## Data
* **Dataset**
  * **Collection**[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/1.%20image%20%ED%95%A9%EC%B9%98%EA%B8%B0.ipynb) [[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/2.%20Make%20data%20with%20crawling%20data.ipynb)
    * 한 의류 플랫폼 내에서 상품 및 리뷰 이미지를 수집함
    * 의류 종류 별로 상품을 50~150개의 리스트로 만들어서 저장함
      * 의류 종류: {"상의", "아우터", "바지", "원피스", "스커트"}
      * 상의, 아우터, 바지는 150개의 상품을 가져옴
      * 원피스는 50개의 상품을 가져옴
      * 스커트는 100개의 상품을 가져옴
     * 각 상품 별 단순 상품 사진 최대 10장, 착용 사진 최대 10장의 사진 리뷰를 가져옴
  * **Kaggle fashion dataset**[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/3.%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A6%9D%EA%B0%95%ED%95%98%EA%B8%B0%20with%20fashion%20dataset.ipynb)
    * 위 수집 데이터 중 원피스 데이터가 적어, 이를 보충하기 위함
    * 라벨 값으로 원피스가 있는 데이터만 수집함
    * 아래 링크에서 다운 받을 수 있음
      * https://www.kaggle.com/datasets/nguyngiabol/colorful-fashion-dataset-for-object-detection?resource=download
  * **Kaggle scene dataset**
    * 옷과 사람이 없는 사진을 입력으로 넣었을 때 모델이 인식하지 않는 것을 테스트하기 위함
    * 아래 링크에서 다운 받을 수 있음
      * https://www.kaggle.com/datasets/nitishabharathi/scene-classification
  
* **Classes**
  * Top, Outer, Pants, Onepiece, Skirt, Human

* **Train Dataset**
  * Collection 데이터 중 총 9,789장 활용함
    * Top, Outer, Pants의 상품을 140개씩 가져옴
    * Onepiece의 상품을 45개 가져옴
    * Skirt의 상품을 95개 가져옴
  * Kaggle fashion dataset 원피스 이미지를 678장 활용함

* **Test Dataset**
  * Collection 데이터 중 총 800장 활용함
    * Top, Outer, Pants의 상품을 10개씩 가져옴
      * 각각 200장의 사진 리뷰를 가져옴
    * Onepiece, Skirt의 상품을 5개씩 가져옴
      * 각각 100장의 사진 리뷰를 가져옴
   * Kaggle scene dataset 1,000장 활용함
     * Else로 구분하여 인식 하지 않는 것을 테스트함

* **Train Dataset Pre-processing**
  * 이미지 라벨링
    * python labelImg.py 사용함
  * 크기
    * (256, 256) 사이즈로 크기 조정함
  * 처리[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/4.%20%EB%8D%B0%EC%9D%B4%ED%84%B0%20%EC%A6%9D%EA%B0%95%ED%95%98%EA%B8%B0%20with%20blur%20and%20gray.ipynb)
    * 색반전, 모자이크, 흑백 처리를 하여 학습 이미지 수를 늘림
    * 아래 그림은 기존 이미지, 색반전, 모자이크, 흑백 순임
      ![image](https://github.com/Silinu1016/Project/assets/97217295/ab4c0184-4aae-4431-a9ce-be2c622ff1c6)
  * 학습 데이터 셋
    * 가장 성능이 좋은 데이터 셋을 선정하기 위해 4가지 데이터 셋을 준비함 <br>
      <img src="https://github.com/Silinu1016/Project/assets/97217295/a138cc49-2356-42c8-958b-a1a9192bbae5" width="400" height="200">

## Model
* **Train Model**
  * YOLOv8s Fine-Tuning
  * YOLOv8m Fine-Tuning
  * YOLOv8l Fine-Tuning

* **Hyperparameter**
  * Epoch: 200(Early Stopping 가능함)
  * Patience: 30
  * Image size: 256


## Performance[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/5.%20Yolo%20%ED%95%99%EC%8A%B5%20with%20crawling%20data.ipynb)
* **의류 종류와 사람을 인식했을 때의 성능(1~2단계만 거침)**
  * **Accuracy by each training dataset**
    * C data로 했을 때 가장 성능이 좋음 <br> 
      <img src="https://github.com/Silinu1016/Project/assets/97217295/924daa27-240e-4f0b-9888-2a580e907674" width="400" height="200">
  * **Accuracy and prediction time by each model**
    * YOLOv8m Fine-Tuning 모델이 가장 성능이 우수하며 시간 또한 빠른 것을 알 수 있음
      ![image](https://github.com/Silinu1016/Project/assets/97217295/58f0e414-a11b-4793-8fa2-bd2e9d6eeb58)
  * **Accuracy by confidence score threshold**
    * Confidence score threshold 값을 0.45로 조정하여 의류 종류 인식 성능을 유지하며, 풍경 사진을 옷으로 인식하지 않도록 실험함 <br> 
      <img src="https://github.com/Silinu1016/Project/assets/97217295/a82ecead-1a0e-4f74-8a69-a20ba1bcae2e" width="400" height="280">
  * **Category of clothes and human detection accuracy with YOLOv8m, C data and conf=0.45**
    ![image](https://github.com/Silinu1016/Project/assets/97217295/5feb44be-8d62-4221-8216-12fb060a51ab)
* **Cosine similarity로 비교한 후의 성능(3~6단계를 거침)[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/6.%20Cosine%20Similarity%20%EB%B9%84%EA%B5%90%20%EB%B0%8F%20%ED%8C%90%EB%8B%A8.ipynb)** <br>
    <img src="https://github.com/Silinu1016/Project/assets/97217295/3826c0c7-354f-4990-9c93-6311d341ac2c" width="420" height="240">
  * 이전과 비교했을 때, 상의, 아우터의 경우 2%, 바지의 경우 4%가 떨어짐
  * 왜냐하면 옷이 일치하더라도 상품의 색과 리뷰 사진의 의류 색이 다르면 유사도가 낮아지기 때문임
    * 색상을 여러 개로 옵션으로 둔 상품에는 여러 색상의 리뷰 사진이 올라오지만, 현재는 한 색상의 대표 사진만 가져와서 비교함
  * 현재는 하나의 상품의 색만 가져와서 비교했지만, 플랫폼쪽에서 색상이 같은 옷과 비교할 수 있도록 설계한다면 성능이 더 올라갈 것으로 보임
  * Else의 경우 90.2%에서 97.1%까지 총 6.9%의 성능을 끌어올림

## ONNX[[Link]](https://github.com/Silinu1016/Project/blob/main/Photo%20Review%20Quality%20Evaluation/7.%20Yolo%20model%20export%20and%20test%20with%20ONNX.ipynb)
* 안드로이드에 모델을 탑재하기 위해 ONNX로 변환함

## Link
* **발표 영상**
  * https://www.youtube.com/watch?v=I_bnnTaOqTg
* **Blog**
  * https://silinu-ai.tistory.com/45
  * https://silinu-ai.tistory.com/46
