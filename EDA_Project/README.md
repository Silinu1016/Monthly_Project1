# EDA Project 
## Description 
* 고객 특징에 따른 소비 유형 분석
  * 어떤 고객 유형이 어느 제품을 구매할 가능성이 가장 높은 지 분석하고 마케팅 하기
  * 분석된 값을 바탕으로 홈페이지를 제작하기
 
## Data
* Link
  * https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis
* 고객 유형
  * 출생 연도, 교육 수준, 결혼 여부, 소득, 자녀 여부, 최근 구매일, 불만 사항
* 제품 종류
  * 와인, 과일, 고기, 생선, 과자, 금

## Hypothesis
**가설 1.** 고객 가구의 자녀 수에 따라 과자 소비량이 비례할 것<br>
**가설 2.** 고객의 결혼 상태에 따라 육류, 생선 소비량이 다를 것<br>
**가설 3.** 고객의 연간 가구 소득에 따라 금 소비량이 비례할 것<br>
**가설 4.** 고객 가구의 자녀 수에 따른 불만 사항 수가 비례할 것<br>
  
## Exploratory Data Analysis(EDA)
### 가설 1 분석 결과
<img src="https://github.com/Silinu1016/Project/assets/97217295/77fd39c1-ef26-438f-b939-0126949800f3" width="405" height="350">

* 자녀 수가 많을 수록 식습관 지출이 반비례한다는 것을 알 수 있음
* 자녀 수가 많을 수록 금 소비가 비례한다는 것을 알 수 있음

**→ 가설이 맞지 않다는 것을 입증함**

### 가설 2 분석 결과
<img src="https://github.com/Silinu1016/Project/assets/97217295/eb66115b-a69d-451a-a3d4-f00b2b94d038" width="300" height="225"> 
<img src="https://github.com/Silinu1016/Project/assets/97217295/39c1c480-298e-48b4-bf27-1b4c5c41cf40" width="300" height="225">
<img src="https://github.com/Silinu1016/Project/assets/97217295/5a275b73-6884-4b8a-88e7-b58737ca3154" width="300" height="225">

* 결혼 상태와는 관계없이 비슷한 지출을 함을 확인할 수 있음
* 와인, 고기, 금 순으로 지출이 높다는 것을 알 수 있음
* 지출 횟수 관점에서 결혼한 사람, 동거, 독신, 이혼 순으로 소비량이 잦은 것을 나타냄
**→ 가설이 맞지 않다는 것을 입증함**

### 가설 3 분석 결과
<img src="https://github.com/Silinu1016/Project/assets/97217295/2b86b0b4-3c15-4f02-adc6-192f0f5fe12b" width="300" height="222"> <br>
<img src="https://github.com/Silinu1016/Project/assets/97217295/b47548f1-9610-42bf-8cf2-5ea408780289" width="439" height="222">
<img src="https://github.com/Silinu1016/Project/assets/97217295/7d38cf96-740c-454e-a3e6-659b4989787e" width="439" height="222">

* 저소득층일수록 구매하지 않는 양이 커지게 되지만, 소득이 0일 때는 예외 사항을 보임
* 소득이 높아질 수록 더욱 다양한 금액 투자가 이루어져 평균적인 금 구매 양이 높음을 확인할 수 있음

**→ 가설이 맞다는 것을 입증함**

### 가설 4 분석 결과
<img src="https://github.com/Silinu1016/Project/assets/97217295/c8d80d90-fe92-4e9a-973c-04f67d29b452" width="389" height="200"> 
<img src="https://github.com/Silinu1016/Project/assets/97217295/a9949ba9-f473-47bc-a6b9-a6c80d194a76" width="247" height="200">
<img src="https://github.com/Silinu1016/Project/assets/97217295/16941538-e555-4c08-a0cf-8404bbe76961" width="254" height="200">

* 자녀 수 혹은 자녀 존재 여부와 불만 비율은 비례하는 것을 확인할 수 있음
* 3 이상의 청소년 수 표본의 종류가 없어, 3 이상일 때의 불만 사항 비율이 증가할 지는 미지수임
* 청소년 존재 여부와 불만 비율은 관계가 없음을 확인할 수 있음

**→ 가설이 맞다는 것을 입증함**

## Homepage
### 실행 방법
1. 두 폴더(Cct_anal,EDA_Project) 및 두 파일(manage.py, db.sqlite3)을 다운받기
2. cd 명령어를 사용하여 다운 받은 위치로 들어가기
3. 아래 명령어를 사용하여 manage.py를 실행하기<br>
   ```python manage.py runserver```

### Page
* 홈
  ![image](https://github.com/Silinu1016/Project/assets/97217295/83c2b120-d839-40a8-a67f-75058921e0f4)

* 참여자
  * GitHub Link Click 누르면 GitHub로 이동함
  ![image](https://github.com/Silinu1016/Project/assets/97217295/2a3c5e50-af56-40cf-a288-975a2f776bc5)

* 데이터 다운
  * kaggle 위치로 바로 넘어감
    ![image](https://github.com/Silinu1016/Project/assets/97217295/b06ac97a-4de5-40f9-aefe-8d5be7ebadf4)

* 데이터 파악
  * 개요
    ![image](https://github.com/Silinu1016/Project/assets/97217295/7941fc23-bbd2-4ea3-accb-d84033f16328)

  * 중요 컬럼
    ![image](https://github.com/Silinu1016/Project/assets/97217295/b14c6eef-c89e-40e4-9585-4be00a4c4049)

  * 판단 및 가설
    ![image](https://github.com/Silinu1016/Project/assets/97217295/342ccbc0-581f-4b88-a652-f8f38110a2e5)

* 데이터 분석
  * 가설 1
    ![image](https://github.com/Silinu1016/Project/assets/97217295/ad6265ee-07db-4914-84a0-e05611336e1e)

  * 가설 2
    ![image](https://github.com/Silinu1016/Project/assets/97217295/4a8f8dca-719e-4a21-9359-488e7d01e96b)

  * 가설 3
    ![image](https://github.com/Silinu1016/Project/assets/97217295/9e8ad3e4-ca3c-40d8-90dc-fef9ff083119)

  * 가설 4
    ![image](https://github.com/Silinu1016/Project/assets/97217295/737d4722-3a8a-4fe4-a75b-1f65bbfd90f2)

  * 그래프 제작
    * 고객 유형과 소비 유형을 하나씩 선택하고 그래프 만들기 버튼을 누르면 그래프가 나옴
      ![그래프 제작](https://github.com/Silinu1016/Project/assets/97217295/cc9f48d0-03db-4009-b79a-a13643a3341d)

### 특수 효과
* 버튼에 마우스를 가져다 댔을 때<br>
  ![글씨 어두워지기](https://github.com/Silinu1016/Project/assets/97217295/fe590086-8b16-421b-a3cf-5046f8a28e9d)

* 그래프에 마우스를 가져다 댔을 때<br>
  ![사진 커지기](https://github.com/Silinu1016/Project/assets/97217295/613e129c-157f-43c3-8b5e-73378dc41463)


### Link
* "" -> 홈
* "participants/"-> 참가자
* "data_disc/purpose"-> 데이터 파악(개요)
* "data_disc/columns"-> 데이터 파악(중요 컬럼)
* "data_disc/hypothesis"-> 데이터 파악(판단 및 가설)
* "data_anal/theory1"-> 데이터 분석(가설1)
* "data_anal/theory2"-> 데이터 분석(가설2)
* "data_anal/theory3"-> 데이터 분석(가설3)
* "data_anal/theory4"-> 데이터 분석(가설4)
* "data_anal/Graph"-> 데이터 분석(그래프 제작)


