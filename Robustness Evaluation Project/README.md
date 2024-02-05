# Robustness Evaluation Project
## Description
* **Robustness Evaluation**
  * 적대적 공격(Adversarial attack) 기법 구현하기

## Data
* **Link**
  * https://github.com/ndb796/Small-ImageNet-Validation-Dataset-1000-Classes
* **Dataset**
  * 5,000 개
* **Classes**
  * 1,000개
  * Example(geyser, bittern, leafhopper, jack-o'-lantern)
    ![image](https://github.com/Silinu1016/Project/assets/97217295/39a87607-898f-4e76-9bac-b7f7fabc12da)

## Pre-trained Model
* Accuracy
![image](https://github.com/Silinu1016/Project/assets/97217295/e48e19f6-34bd-484b-ab68-c3f9498fe8fa)



## Model & Performance
### FGSM(Fast Gradient Sign Method)
  * **Architecture**
    * 각 픽셀마다 비용이 증가하는 방향으로 eps만큼 변경하는 공격 기법
    * 딥러닝 분류 모델이 작은 크기의 perturbation에도 매우 취약할 수 있음
    * [Explaining and Harnessing Adversarial Examples](https://arxiv.org/abs/1412.6572) <br> 
    ![image](https://github.com/Silinu1016/Project/assets/97217295/5ba94c0e-0f09-4ab2-9a00-454c63390f8a)


  * **Performance**
    * 정확도가 낮을 수록 공격력이 높은 것
    * **Accuracy by eps** <br>
      ![image](https://github.com/Silinu1016/Project/assets/97217295/a0a626de-1a5e-475f-8da9-b25ecf0cc7cf)

### PGD(Projected Gradient Descent)
  * **Architecture**
    * 적은 스텝(step = iters)만으로도 충분히 강력한 perturbation을 만들 수 있다는 장점이 있음
    * [Towards Deep Learning Models Resistant to Adversarial Attacks](https://arxiv.org/abs/1706.06083) <br> 
    ![image](https://github.com/Silinu1016/Project/assets/97217295/eeb83595-de17-4b6f-9d4c-04aed7c2ee50)

  * **Performance**
    * **Accuracy by eps** <br>
      ![image](https://github.com/Silinu1016/Project/assets/97217295/350851b0-2ded-4027-9828-5503df55251a)


### Custom Black-box Attack Model
  * **Architecture**
    * Ensemble Model 사용함
      * Model List
        * ResNet50, ResNet101, ResNet152, ResNext50_32x4d, DenseNet121, DenseNet169,
          DenseNet201, EfficientNet, ShuffleNet v2, Regnet, MobileNet
  * **Hyperparameter**
    * Eps: 16/255
    * Alpha: 8/255
    * Iteration: 5
    * Beta: 1.0(iteration 3부터 0.5로 진행함)

  * **Performance**
    * Accuracy: 2.88%
    * Average L0 distance: 143395.872
    * Average L2 distance: 22.3299
    * Average MSE: 0.0033
    * Average Linf distance: 0.0627

      
