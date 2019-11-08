import pandas as pd
import seaborn as sns
import matplotlib.pypyplot a plt
import statsmodels.api as sm

# Read the data set ito a pandas DataFrame
wine = pd.read_csv('winequlity-both.csv', sep=',', header = 0)
wine.columns = wine.columns.str.replace(' ', '_')

# Display descriptive statistics for quality by wine type
print("< 와인 종류에 따른 기술통계를 출력하기>")
# 엑셀의 피벗 테이블 효과
print(wine.groupby('type')[['alcohol']].describe().unstack('type'))

# Calculate specific quantiles
print("< 특정 사분위수 계산하기")
print(wine.groupby('type')[['quality']].quantile([0.25, 0.75]).unstack('type'))

print("\n"+'='*80)
print("7.2.2 그룹화, 히스토그램, t 검정")
# red_wine = wine.ix[wine['type'] =='red', 'quality']
# ix함수는 현재 deprecate되었음. 현재 파이썬 버전에서 공식적으로 지원되지는 않고
#다만 하위 파이썬 호환을 위해서 수행시 warning 메세지를 보여주고 정상작동한다.
red_wine = wine.loc[wine['type']=='red', 'quality']
# white_wine = wine.ix[wine['type']=='white', 'quality']
white_wine = wine.loc[wine['type']=='white', 'quality']