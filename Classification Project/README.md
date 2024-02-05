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
* **Logistic Regression**
  * 아래 코드처럼 Logistic Regression을 불러와서 학습함
    * ```
      from sklearn.linear_model import LogisticRegression
      model = LogisticRegression(multi_class="multinomial",solver="lbfgs", max_iter=iter)
      model.fit(X_train, y_train)
      ```
  * **Performance**
    * 초반에는 증가하다가 일정 epoch 기준으로 수렴하거나 감소함
    * 왜냐하면 학습 데이터 셋에 맞춰 **Overfitting**하기 때문임
    * 따라서 적절한 Epoch를 주는 것이 중요함
    ![image](https://github.com/Silinu1016/Project/assets/97217295/e9e6eaef-f54d-41e0-8de6-41b3e730b276)

* **Increase performance by 55% or more**
  * 기존 이미지, Shift(기존 이미지), Flip(기존 이미지)로 학습하기
  * 아래 처럼 Hyperparameter를 설정함
    * ```
      model = LogisticRegression(multi_class="multinomial",solver="lbfgs", max_iter=35)
      ```
  * **Performance**
    * 학습 데이터셋 정확도: 57.9%
    * 검증 데이터셋 정확도: 55.6%
* **Test accuracy by K**
  * 평가지표
    * Sum Absolute Error(SAE), Root Sum Square Error(RSSE), Cosine Similarity
    ![image](https://github.com/Silinu1016/Project/assets/97217295/11205e42-cad7-459d-b06e-e4c9e35cc754)

