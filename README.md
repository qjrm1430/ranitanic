# This is Ranitanic README

## 경진 대회
https://www.kaggle.com/competitions/skn-03-ml/overview

## 최종 스코어

### public score
![image](https://github.com/user-attachments/assets/20ab0813-4588-46e4-8a84-8a11b26b1b18)

### private score
![image](https://github.com/user-attachments/assets/7508125d-cd20-4607-9705-b1a307237662)


## 개선 필요점

1. HPO 과정 수정
   - HPO에서 GridSearch보단 RandomSearch의 소요시간 및 기대값이 더 좋다.
   - 순서는 RandomSearch가 BayesianSearch(Optuna)보다 선행되어져야 한다.
   - 현재 순서 : BayesianSearch(Optuna) -> Gridsearch
   - 수정되어야 할 순서 : RandomSearch -> BayesianSearch(Optuna)

2. 전처리 과정중 필요한 임계값 찾기
   - 현재 임계값이 필요한 전처리 과정은 피처 선택 및 피처 삭제 과정이다.
   - 이 때 베이스 모델들의 학습에 필요한 최적의 임계값을 전체적으로 균형을 맞추려고 하니 찾는 시간도 오래걸리고 기대치도 낮다.
   - 이를 개선할 방법이 필요하다.
  
  
