# Generative Adversarial Networks Project
## Description
* **Generate images with mask and without mask**
  * 마스크를 착용한 이미지와 마스크를 착용하지 않은 얼굴 이미지를 생성하는 모델 만들기

## Data
* **Link**
  * https://www.kaggle.com/datasets/pranavsingaraju/facemask-detection-dataset-20000-images
* **Dataset**
  * 20,000 장
* **Train Dataset**
  * 18,000 장(마스크 착용 이미지-9,000장, 마스크 미착용-9,000장)
* **Test Dataset**
  * 2,000 장(마스크 착용 이미지-1,000장, 마스크 미착용-1,000장)

## Model & Performance
### GAN
  * **Architecture**
    * [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
    * [Conditional Generative Adversarial Nets](https://arxiv.org/abs/1411.1784)
    ![image](https://github.com/Silinu1016/Project/assets/97217295/65c04676-60b1-46f4-8564-5d04f95b8e67)


  * **Performance**
    * Fréchet Inception Distance(FID) 계산 방법
      * 생성된 이미지들과 실제 이미지들을 ImageNet에 넣어 특징(feature)을 추출함
      * 생성된 이미지 특징 분포 G와 실제 이미지 특징 분포 X를 가우시안 분포라고 가정함
      * 두 분포가 얼마나 다른지 계산하기 위해 FID(X, G)를 계산함
      * [FID score for PyTorch](https://github.com/hukkelas/pytorch-frechet-inception-distance) 라이브러리로 계산 가능
      * 아래 코드로 계산 가능함
         ```
          !python ./pytorch-frechet-inception-distance/fid.py --path1 {학습 시 저장된 생성 이미지 폴더 위치} --path2 {test 이미지 폴더 위치} --batch-size {배치 사이즈}
          ```
      ||Without Mask|With Mask|
      |:---:|:---:|:---:|
      |FID|247.69|320.88|
      |Image|<img src="https://github.com/Silinu1016/Project/assets/97217295/5798f2d5-77c2-4316-a6a9-2dc97b69234c" width="200" height="200">|<img src="https://github.com/Silinu1016/Project/assets/97217295/b6c0341b-06bb-4b68-a442-9bb2776a9302" width="200" height="200">|

### DCGAN
  * **Architecture**
    * [Deep Convolutional Generative Adversarial Networks](https://arxiv.org/abs/1511.06434)
    ![image](https://github.com/Silinu1016/Project/assets/97217295/13f59a13-bb51-4351-8750-288ddbb4f277)



  * **Performance**
      ||Without Mask|With Mask|
      |:---:|:---:|:---:|
      |FID|171.67|114.97|
      |Image|<img src="https://github.com/Silinu1016/Project/assets/97217295/63814e12-47b2-41f0-9d39-4e02d0754172" width="200" height="200">|<img src="https://github.com/Silinu1016/Project/assets/97217295/05564e02-6c85-44e7-827d-15a044b6517d" width="200" height="200">|

### Custom GAN
  * **Architecture**
    * DCGAN + ConvTranspose2d 모델 사용
      
  * **Hyperparameter**
    * Epoch : 135
    * Learning rate : 0.0002(25epoch마다 절반씩 감소함)
    * Batch size : 64

  * **Performance**
    * 총 Without Mask 점수와 With Mask 점수를 합하여 267.02점을 달성함
      ||Without Mask|With Mask|
      |:---:|:---:|:---:|
      |FID|166.59|100.43|
      |Image|<img src="https://github.com/Silinu1016/Project/assets/97217295/2485d369-3682-4009-8b9b-655a3da066b9" width="200" height="200">|<img src="https://github.com/Silinu1016/Project/assets/97217295/20a81021-6569-42ef-8b84-7e83ea8e95c1" width="200" height="200">|
