import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
# 붓꽃의 CSV 데이터 읽어 들이기 --- (※1)
csv = pd.read_csv('preprocessed_data.csv')
# 필요한 열 추출하기 --- (※2)
# csv_data = csv["SepalLength","SepalWidth","PetalLength","PetalWidth"]
csv_data = csv[["title_bout", "no_of_rounds", "B_current_lose_streak", "B_current_win_streak", "B_draw", "B_avg_BODY_att", "B_avg_BODY_landed", "B_avg_CLINCH_att", "B_avg_CLINCH_landed", "B_avg_DISTANCE_att", "B_avg_DISTANCE_landed", "B_avg_GROUND_att", "B_avg_GROUND_landed", "B_avg_HEAD_att", "B_avg_HEAD_landed", "B_avg_KD", "B_avg_LEG_att", "B_avg_LEG_landed", "B_avg_PASS", "B_avg_REV", "B_avg_SIG_STR_att", "B_avg_SIG_STR_landed", "B_avg_SIG_STR_pct", "B_avg_SUB_ATT", "B_avg_TD_att", "B_avg_TD_landed", "B_avg_TD_pct", "B_avg_TOTAL_STR_att", "B_avg_TOTAL_STR_landed", "B_longest_win_streak", "B_losses", "B_avg_opp_BODY_att", "B_avg_opp_BODY_landed", "B_avg_opp_CLINCH_att", "B_avg_opp_CLINCH_landed", "B_avg_opp_DISTANCE_att", "B_avg_opp_DISTANCE_landed", "B_avg_opp_GROUND_att", "B_avg_opp_GROUND_landed", "B_avg_opp_HEAD_att", "B_avg_opp_HEAD_landed", "B_avg_opp_KD", "B_avg_opp_LEG_att", "B_avg_opp_LEG_landed", "B_avg_opp_PASS", "B_avg_opp_REV", "B_avg_opp_SIG_STR_att", "B_avg_opp_SIG_STR_landed", "B_avg_opp_SIG_STR_pct", "B_avg_opp_SUB_ATT", "B_avg_opp_TD_att", "B_avg_opp_TD_landed", "B_avg_opp_TD_pct", "B_avg_opp_TOTAL_STR_att", "B_avg_opp_TOTAL_STR_landed", "B_total_rounds_fought", "B_total_time_fought(seconds)", "B_total_title_bouts", "B_win_by_Decision_Majority", "B_win_by_Decision_Split", "B_win_by_Decision_Unanimous", "B_win_by_KO/TKO", "B_win_by_Submission", "B_win_by_TKO_Doctor_Stoppage", "B_wins", "B_Height_cms", "B_Reach_cms", "B_Weight_lbs", "R_current_lose_streak", "R_current_win_streak", "R_draw", "R_avg_BODY_att", "R_avg_BODY_landed", "R_avg_CLINCH_att", "R_avg_CLINCH_landed", "R_avg_DISTANCE_att", "R_avg_DISTANCE_landed", "R_avg_GROUND_att", "R_avg_GROUND_landed", "R_avg_HEAD_att", "R_avg_HEAD_landed", "R_avg_KD", "R_avg_LEG_att", "R_avg_LEG_landed", "R_avg_PASS", "R_avg_REV", "R_avg_SIG_STR_att", "R_avg_SIG_STR_landed", "R_avg_SIG_STR_pct", "R_avg_SUB_ATT", "R_avg_TD_att", "R_avg_TD_landed", "R_avg_TD_pct", "R_avg_TOTAL_STR_att", "R_avg_TOTAL_STR_landed", "R_longest_win_streak", "R_losses", "R_avg_opp_BODY_att", "R_avg_opp_BODY_landed", "R_avg_opp_CLINCH_att", "R_avg_opp_CLINCH_landed", "R_avg_opp_DISTANCE_att", "R_avg_opp_DISTANCE_landed", "R_avg_opp_GROUND_att", "R_avg_opp_GROUND_landed", "R_avg_opp_HEAD_att", "R_avg_opp_HEAD_landed", "R_avg_opp_KD", "R_avg_opp_LEG_att", "R_avg_opp_LEG_landed", "R_avg_opp_PASS", "R_avg_opp_REV", "R_avg_opp_SIG_STR_att", "R_avg_opp_SIG_STR_landed", "R_avg_opp_SIG_STR_pct", "R_avg_opp_SUB_ATT", "R_avg_opp_TD_att", "R_avg_opp_TD_landed", "R_avg_opp_TD_pct", "R_avg_opp_TOTAL_STR_att", "R_avg_opp_TOTAL_STR_landed", "R_total_rounds_fought", "R_total_time_fought(seconds)", "R_total_title_bouts", "R_win_by_Decision_Majority", "R_win_by_Decision_Split", "R_win_by_Decision_Unanimous", "R_win_by_KO/TKO", "R_win_by_Submission", "R_win_by_TKO_Doctor_Stoppage", "R_wins", "R_Height_cms", "R_Reach_cms", "R_Weight_lbs", "B_age", "R_age", "weight_class_Bantamweight", "weight_class_Catch Weight", "weight_class_Featherweight", "weight_class_Flyweight", "weight_class_Heavyweight", "weight_class_Light Heavyweight", "weight_class_Lightweight", "weight_class_Middleweight", "weight_class_Open Weight", "weight_class_Welterweight", "weight_class_Women's Bantamweight", "weight_class_Women's Featherweight", "weight_class_Women's Flyweight", "weight_class_Women's Strawweight", "B_Stance_Open Stance", "B_Stance_Orthodox", "B_Stance_Sideways", "B_Stance_Southpaw", "B_Stance_Switch", "R_Stance_Open Stance", "R_Stance_Orthodox", "R_Stance_Southpaw", "R_Stance_Switch"]]
csv_label = csv["Winner"]
# 학습 전용 데이터와 테스트 전용 데이터로 나누기 --- (※3)
train_data, test_data, train_label, test_label = \
train_test_split(csv_data, csv_label)
# 데이터 학습시키고 예측하기 --- (※4)
clf = svm.SVC()
# 아래와 같은 방식은 머신러닝의 대표적인 지도학습 모델이라고 할 수 있다.
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)
ac_number = metrics.accuracy_score(test_label, pre, normalize=False)
print("전체 데이터 수: %d"%(len(csv_data)))
print("학습 전용 데이터 수: %d"%(len(train_data)))
print("테스트 데이터 수: %d"%(len(test_data)))
print(f'정답개수: {ac_number}')
print(f"정답률: {ac_score*100} %%")
