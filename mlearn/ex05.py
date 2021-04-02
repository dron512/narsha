#결정트리

'''
    한빛 마켓에서는 신상품으로 캔 와인을 판매하려 합니다. 주류는 온라인 판매가 안돼서 온라인
    예약 후 오프라인 매장에서 구매를 유도할 계획입니다.

    아무래도 병이 아닌 캔이라 걱정인데 마켓팅 팀은 특수 캔으로 맛과 향이 유지되도록 제작했다며 젊은 층에
    인기가 있을거라 자신합니다. 그런데 입고된 와인을 보니 급하게 제작하는 바람에 레드와인과 화이트 
    와인 표시가 누락되었습니다. 김 팀장은 다시 혼공머신을 불렀습니다.

    캔에 인쇄된 알코올 도수, 당도, pH 값으로 와인 종류를 구별할 수 있는 방법이있을까
    글쎼요 해봐야죠 일단 훈련데이터를 얻으려면 수천개의 캔을 뜯어야 할지도 몰라요
    품질확인용으로 뜬은 캔이 있으니 걱정 말게 필요한 데이터는 충분할 거네
    알겠습니다. 작업해보고 진전이 있으면 다시 말씀드릴꼐요
    이사님꼐 직접 보고해야 하니 조금이라도 진전이 있으면 바로 말해줘
    
    김팀장의 당부를 듣고 혼공머신은 일단 알코올 도수, 당도, pH 값에 로지스틱 회귀 모델을 적용할 계획을
    세웁니다.

    로지스틱 회귀로 와인 분류하기
    혼공머신은 의외로 문제를 쉽게 풀수 있을것 같았습니다. 품질관리 팀에서 6497개의 와인 샘플 데이터를 보냈습니다.
    이 데이터 셋을 불러와 보죠. 4장에서처럼 판다스를 사용해 인터넷에서 직접 불러오겠습니다.
'''

import pandas as pd
wine = pd.read_csv('https://bit.ly/wine-date')

# print(wine.head())

'''
    처음 3개의 열은 각각 알코올 도수,당도,pH값을 나타냅니다. 네번쨰 열은 타깃값으로 0이면 레드와인, 1이면 화이트
    와인이라고 하네요 레드 와인과 화이트와인을 구분하는 이진 분류 문제이고, 화이트 와인 양성 클래스입니다.
    즉 전체 와인 데이터에서 화이트 와인을 골라내는 문제군요.

    로지스틱 회귀 모델을 바로 훈련하기 전에 판다스 데이터프레임의 유용한 메서드 2개를 먼저 알아보겠습니다.
    먼저 info()메서드입니다. 이 메서드는 데이터프레임의 각 열의 데이터 타입과 누락된 데이터가
    있는지 확인하는데 유용합니다.
'''

# print(wine.info())

'''
    출력결과를 보면 총 6497개의 샘플이 있고 4개의 열은 모두 실솟값입니다. Non-NUll Count가 모두 6497이므로
    누락된 값은 없는것 같습니다.
'''

'''
    누락된 값이 있다면 그 데이터를 버리거나 평균값으로 채운 후 사용할 수 있습니다. 어떤 방식이 최선인지는 미리
    알기 어렵습니다. 두 가지 모두 시도해보세요. 여기에서도 항상 훈련 세트의 통계 값으로 테스트 변환하다는 것을
    잊지 마세요. 즉 훈련 세트의 평균값으로 테스트 세트의 누락된 값을 채워야 합니다.

    다음은 알아볼 메서드는 describe()입니다. 이 메서드는 열에 대한 간략한 통계를 출력해 줍니다.
    최소, 최대, 평균값등을 볼수 있습니다.
'''

print(wine.describe())

'''
    평균 표준편차 최소 최대 값을 볼 수 있습니다. 
    시분위수는 데이터를 순서대로 4등분 한 값입니다. 예를 들어 2사분위수(중간값)는 데이터를 일렬로 늘어놓을떄
    정중앙의 값입니다. 만약 데이터 개수가 짝수개라 중앙값을 선택할 수 없다면 가운데 2개 값의 평균을 사용합니다.

    여기서 알 수 있는 것이 알코올 도수와 당도 pH 값의 스케일이 다르다는 것입니다. 이전에 했던 것처럼 사이킷런의
    StandardScaler 클래스를 사용해 특성을 표준해해야겠군요. 그 전에 먼저 판다스 데이터 프레임을
    넘파이 배열로 바꾸고 훈련 세트와 테스트 세트로 나누겠습니다.
'''

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

'''
    wine 데이터프레임에서 처음 3개의 열을 넘파이 배열로 바꿔서 data 배열에 저장하고 마지막 class 열을 넘파이
    배열로 바꿔서 target 배열에 저장했습니다. 이제 훈련세트와 테스트 세트로 나누어보죠
'''

from sklearn.model_selection import train_test_split
train_input,test_input,train_target,test_target = train_test_split(data,target,test_size=0,2,random_state=42)

