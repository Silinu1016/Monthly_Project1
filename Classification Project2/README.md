# Classification Project
## Description
* **Scene Classification**
  * 다양한 자연 경치 이미지를 카테고리 별로 학습하기
  * 한 장의 이미지 입력 시 하나의 카테고리를 출력으로 내보냄

## Data
* **Link**
  * https://www.kaggle.com/nitishabharathi/scene-classification
* **Dataset**
  * 24,335 개
* **Train Dataset**
  * 17,034 개
* **Classes**
  * Buildings, Forests, Glacier, Mountains, Sea, Street
    ![image](https://github.com/Silinu1016/Project/assets/97217295/8767b9e8-510c-426a-91ad-73fd59f440d2)

## Model & Performance
### LeNet
  * **Architecture**
    ![image](https://github.com/Silinu1016/Project/assets/97217295/5778e037-20a2-4cb5-a4cb-83bc45ce7ad6)

  * **Performance**
    * 0.007 이상의 Learning rate의 경우 손실 값이 NaN이 나옴
    * **Accuracy by Learning rate in epoch 30** <br>
      ![image](https://github.com/Silinu1016/Project/assets/97217295/46ea6be3-0c43-4ec1-84b2-767512877ecf)
      
    * **Loss with learning rate 0.002** <br>
        <img src="https://github.com/Silinu1016/Project/assets/97217295/8028a437-12a6-4efc-90ec-eec5ca42c3dd" width="450" height="300">
        
    * **Confusion Matrix & Accuracy** <br>
        <img src="https://github.com/Silinu1016/Project/assets/97217295/86d348fd-234c-41d6-8874-93a802b02efa" width="300" height="222">   
        <img src="https://github.com/Silinu1016/Project/assets/97217295/fd82055f-82f4-434a-9de7-8eb7d4716e74" width="180" height="222">

### CustomLeNet
  * **Architecture**
    ![image](https://github.com/Silinu1016/Project/assets/97217295/e8f8803f-19e5-47be-98ca-9827a48b55ca)


  * **Performance**
    * **Accuracy by Learning rate in epoch 30** <br>
      ![image](https://github.com/Silinu1016/Project/assets/97217295/b27f3680-49ce-44c5-8365-2efe42d93f45)

    * **Loss with learning rate 0.0009** <br>
        <img src="https://github.com/Silinu1016/Project/assets/97217295/5645c798-d16b-4bf7-9f6b-c3ff20155b2c" width="450" height="300">

    * **Confusion Matrix & Accuracy**
      * LeNet보다 전체 평균 정확도가 0.0399 감소함 <br> 
        <img src="https://github.com/Silinu1016/Project/assets/97217295/10c861d8-3850-4ef3-a3df-7ee0380cd088" width="300" height="222">   
        <img src="https://github.com/Silinu1016/Project/assets/97217295/3c0583cd-be68-46b5-978d-a4a02724af9b" width="180" height="222">

### AlexNet
  * **Architecture**
    ![image](https://github.com/Silinu1016/Project/assets/97217295/80e1e209-95e8-477e-a8e6-6de660373a95)
    ![image](https://github.com/Silinu1016/Project/assets/97217295/2078068a-9c77-4583-bc50-0cbbb48ebdbc)

  * **Performance**
    * **Confusion Matrix & Accuracy** <br>
      <img src="https://github.com/Silinu1016/Project/assets/97217295/fede2ae1-0997-4e81-9971-f4d083024b7e" width="300" height="222">   
      <img src="https://github.com/Silinu1016/Project/assets/97217295/c579a101-edba-4b44-8755-feff75beccc4" width="180" height="222">

### LightResNet
  * **Architecture**
    * [ResNet(2016 CVPR)](https://arxiv.org/abs/1512.03385) 논문에서 제안된 가벼운 ResNet을 구현함
    * 이 프로젝트에서는 epoch 30, learning rate 0.002로 고정 후, layer 수를 각각 20, 32, 56, 110으로 학습함

  * **Performance**
    * **Accuracy**
      * Layer가 깊어짐에 따라 성능이 좋지 않음
      * 왜냐하면 Layer가 깊어질 수록 파라미터 수가 많아지기 때문에 Epoch 수를 늘려 학습을 더 진행해야 함
      <img src="https://github.com/Silinu1016/Project/assets/97217295/e6b37a88-74d2-4533-833c-daae8f5912a1" width="450" height="300">

### ResNet18
  * **Architecture**
    * 이 프로젝트에서는 ResNet18 모델의 성능을 올리기 위해 Mixup, Transfer Learning 기법을 사용함 

  * Performance
    * **Accuracy**
      * Transfer Learning 기법을 같이 적용하였을 때 기존 ResNet보다 7.2% 증가함
      <img src="https://github.com/Silinu1016/Project/assets/97217295/bb6e505c-a232-4058-a3e4-5a380c12edc3" width="450" height="300">

### ResNet50, ResNet101, ResNet152
  * **Architecture**
    * 이 프로젝트에서는 ResNet18 모델의 성능을 올리기 위해 Mixup, Transfer Learning 기법을 둘 다 적용함
   
  * **Hyperparameter**
    * Epoch : 50
    * Learning rate : 0.001
    * Optimizer : SGD
    * Scheduler : MultiStepLR <br>
      <img src="https://github.com/Silinu1016/Project/assets/97217295/50ecfe0e-c276-42e2-8dd5-14916eab6916" width="225" height="100">

  * **Performance**
    * **Accuracy**
      * 최종적으로 ResNet101 모델을 사용하여 94.3%를 달성함
      <img src="https://github.com/Silinu1016/Project/assets/97217295/c2e2089c-d3c0-4864-81ba-6c3f25ebb4a9" width="450" height="300">
