import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate,StratifiedKFold,GridSearchCV,RandomizedSearchCV
from scipy.stats import uniform,randint
# from myex01 import AA


wine = pd.read_csv('https://bit.ly/wine-date')

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
train_input,test_input,train_target,test_target = train_test_split(data,target,\
    test_size=0.2,random_state=42)

sub_input,val_input,sub_target,val_target = train_test_split(train_input, train_target,\
    test_size=0.2,random_state=42)

print(sub_input.shape,val_input.shape)

dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input,sub_target)

print(dt.score(sub_input,sub_target))
print(dt.score(val_input,val_target))

'''## 교차 검증'''

scores = cross_validate(dt,train_input,train_target)
print(scores)

print(np.mean(scores['test_score']))

scores = cross_validate(dt,train_input,train_target,cv = StratifiedKFold())
print(np.mean(scores['test_score']))

splitter = StratifiedKFold(n_splits=10,shuffle=True,random_state=42)
scores = cross_validate(dt,train_input,train_target,cv=splitter)
print(np.mean(scores['test_score']))

'''###하이퍼파라미터튜닝'''

# aa = AA()
# aa.doA()

params = {'min_impurity_decrease':[0.0001,0.0002,0.0003,0.0004,0.0005]}

gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)

gs.fit(train_input,train_target)

dt = gs.best_estimator_
print(dt.score(train_input,train_target))

print(gs.best_params_)
print(gs.cv_results_['mean_test_score'])

best_index = np.argmax(gs.cv_results_['mean_test_score'])
print(gs.cv_results_['params'][best_index])

params = {'min_impurity_decrease':np.arange(0.0001,0.001,0.0001),
        'max_depth':range(5,20,1),
        'min_samples_split':range(2,100,10)
        }

gs = GridSearchCV(DecisionTreeClassifier(random_state=42),params,n_jobs=-1)
gs.fit(train_input,train_target)

print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))

'''### 랜덤 서치'''
rgen = randint(0,10)
rgen.rvs(10)

np.unique(rgen.rvs(1000),return_counts=True)
ugen = uniform(0,1)

params = {'min_impurity_decrease':uniform(0.0001,0.001),
        'max_depth':randint(20,50),
        'min_samples_split':randint(2,5),
        'min_samples_leaf':randint(1,25)
        }

gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42),params,n_iter=100,n_jobs=-1,random_state=42)

gs.fit(train_input,train_target)
print(gs.best_params_)

print(np.max(gs.cv_results_['mean_test_score']))

dt = gs.best_estimator_
print(dt.score(test_input,test_target))


'''
키워드로 끝내는 핵심 포인트
검증 세트는 하이퍼 파라미터 튜닝을 위해 모델을 평가할때, 테스트 세트를 사용하지 않기 위해
훈련 세트에서 다시 떼어 낸 데이터 세트입니다.

교차 검증은 훈련 세트를 여러 폴드로 나눈 다음 한 폴드가 검증 세트의 역할을 하고 나머지 폴드에서는
모델을 훈련 합니다. 교차검증은 이런식으로 모든 폴드에 대해 검증 점수를 얻어 평균을 구하는 방법입니다.

그리드 서치는 하이퍼 파리미터 탐색을 자동화 해주는 도구 입니다. 탐색할 매개변수를 나열하면 교차 검증을 수행하여
가장 좋은 검증 점수의 매개변수 조합을 선택합니다. 마지막으로 이 매개변수 조합으로 최종 모델을 훈련합니다.

랜덤서치는 연속된 매개변수 값을 탐색할 때 유용합니다. 탐색할 값을 직접 나열하는 것이 아니고 탐색 값을
샘플링 할 수 있는 확률 분포 객체를 전달합니다. 지정된 횟수만큼 샘플링하여 교차 검증을 수행하기 때문에
시스템 자원이 허락하는 만큼 탐색량을 조절할 수 있습니다.
'''

'''
    핵심패키지와 함수
    scikit-learn
    cross_validateion() 교차 검증을 수행하는 함수 입니다.
    첫 번쨰 매개변수에 교차 검증을 수행할 모델 객체를 전달합니다. 두번째와 세번째 매개변수에 특성과 타깃
    데이터를 전달합니다.

    scoring 매개변수에 검증에 사용할 평가 지표를 지정할 수 있습니다. 기본적으로 분류 모델은 정확도를
    의미하는 accuracy 회귀 모델은 결정 계수를 의미하는 r2가 됩니다.

    cv매개변수에 교차 검증 폴드 수나 스플리터 객체를 지정할 수 있습니다. 기본값은 5입니다. 회귀일때는
    KFold 클래스를 사용하고 분류일떄는 StratifiedKFold 클래스를 사용하여 50폴드 교차검증을 수행합니다.

    n_jobs매개변수는 교차검증을 수행할 떄 사용할 cpu 코어 수를 지정합니다. 기본값은 1로 하나의 코어를
    사용합니다 -1으로 지정하면 시스템에 모든 코어를 사용합니다.

    return_train_score 매개변수를 True로 지정하면 훈련 세트의 점수도 반환 합니다. 기본값은 False입니다.

    GridSearchCV는 교차 검증으로 하이퍼파라미터 탐색을 수행합니다. 최상의 모델을 찾은 후
    훈련 세트 전체를 사용해 최종모델을 훈련합니다.

    첫번째 매개변수로 그리드 서치를 수행할 모델 객체를 전달합니다. 두번째 매개변수에는 탐색할
    모델의 매개변수와 값을 전달합니다.

    scoring,cv,n_jobs,return_train_score 매개변수는 cross_validate() 함수와 동일합니다.

    RandomizedSearchCV는 교차 검증으로 랜덤한 하이퍼 파라미터를 탐색을 수행합니다. 최상의 모델을 찾은후
    훈련 세트 전체를 사용해 최종모델을 훈련합니다.

    첫번쨰 매개변수로 그리드 서치를 수행할 모델객체를 전달합니다. 
    두번째 매개변수에는 탐색할 모델의 매개변수와 확률 분포 객체를 전달합니다.

    scoring,cv,n_jobs,return_train_score 매개변수는 cross_validate() 함수와 동일합니다.
'''