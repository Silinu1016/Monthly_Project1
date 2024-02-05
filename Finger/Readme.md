학습 과정은 아래 링크에서 확인하실 수 있습니다.
1. Webcam으로 데이터 수집하기 : https://silinu-ai.tistory.com/9
2. 이미지 라벨링하기 : https://silinu-ai.tistory.com/10
3. Image preprocessing 및 train,val 나누기 : https://silinu-ai.tistory.com/11
4. Yolov8 모델로 커스텀 데이터 학습하기 및 예측하기 : https://silinu-ai.tistory.com/12
5. 학습된 Yolo 가중치 불러오기 및 실시간 웹캠에 적용하기 : https://silinu-ai.tistory.com/13


본 내용에서는 **YOLOv8** 모델을 커스터마이징하여 **손가락의 숫자를 실시간으로 인식하는 것**을 목표로 합니다.<br>
현재 사용한 Webcam은 다이소에서 5,000원에 파는 pc용 화상 카메라로 진행하였습니다.<br>
Jupyter notebook 환경에서 실행되며 Anaconda prompt 가상 환경에서 opencv, ultralytics, pyqt5, pyrcc5 라이브러리를 설치하였습니다. 설치하는 방법은 위 티스토리 블로그에 기재되어 있습니다. 
<br><br>
라벨링을 할 때는 https://github.com/tzutalin/labelImg.git 의 labelImg.py를 설치하여 실행하였습니다.<br>
총 353개의 데이터로 학습을 진행하였고 실시간으로 다음과 같이 예측되는 것을 확인할 수 있습니다.<br>
![croped_test_with_webcam](https://github.com/Silinu1016/YOLOv8_with_Custom_Data-/assets/97217295/3b201b30-0cf6-412f-88a0-f6cb1754b8b0)
