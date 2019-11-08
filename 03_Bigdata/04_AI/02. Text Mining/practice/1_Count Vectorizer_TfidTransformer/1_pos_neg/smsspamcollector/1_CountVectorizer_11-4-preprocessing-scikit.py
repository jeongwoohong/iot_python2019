import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

spam_header = 'spam\t'
no_spam_header = 'ham\t'
documents = []
labels = []

with open('SMSSpamCollection', 'r', encoding='UTF-8') as file_handle:
    for line in file_handle:
        # 각 줄에서 레이블 부분만 떼어내고 나머지를 Documents에 넣는다.
        if line.startswith(spam_header):
            labels.append(1)
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            labels.append(0)
            documents.append(line[len(no_spam_header):])

# 희소행렬(Sparse Matrix)         => Compressed sparse Matrix
# | 1 0 0 0 2 0 |                   | 0 0 1 |
# | 0 0 0 3 0 0 |                   | 0 4 2 |
# | 0 0 0 4 5 0 |                   | 1 3 3 |
# | 6 0 0 0 0 0 |                   | 2 3 4 |
# | 0 0 0 0 0 7 |                   | 2 5 6 |
# | 0 8 0 0 0 0 |                   | 3 0 6 |
#                                   | 4 5 7 |
#                                   | 5 1 8 |

vectorizer = CountVectorizer() # 단어 횟수 피처를 만드는 클래스
term_counts = vectorizer.fit_transform(documents) # 문서에서 단어 횟수를 센다.
vocaburaray = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스
# 단어 빈도 (term frequency)가 생성
# TF : Term Frequency (문서상에서 발견된 단어) / (전체 문서상의 단어)
# IDF : Inverse Document Frequency
#       (주요 언어: is, of, that 같은 단어는 제외하고 빈도를 측정한다.)
tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)

# 처리된 파일을 저장합니다. 앞으로의 예제에서 사용될 예정입니다.
with open('processed.pickle', 'wb') as file_handle:
    pickle.dump((vocaburaray, features, labels), file_handle)