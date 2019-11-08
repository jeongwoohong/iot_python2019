#- 과제 수행 목표 : 한글 text를 대상으로 한 텍스트마이닝 적용
#- 데이터 출처 및 해석 : https://kr.usembassy.gov/ko/013018-president-donald-j-trumps-state-union-address-ko/ 도날드 트럼프 국정연설
#- 텍스트 데이터 의미 : 국정연설 내용중 중요성을 띈 의미 해석
#- 예측 항목 : 유의어 예측
#- 어휘 분류 기준 : 미국
#- 판별 기준 : word2vec
#- 유의어 : 미국
#- 구현 프로그램 : konply Okt(python)
#- 분석 결과:
# 우리 (95)
# 그 (76)
# 미국 (75)
# 것 (70)
# 국민 (44)
# 이 (44)
# 수 (41)
# 저 (29)
# 계층        : 0.9992249011993408
# 법률        : 0.9991717338562012
# 도발        : 0.9991074800491333
# 것         : 0.9990739822387695
# 가정        : 0.9990377426147461
# 재건        : 0.9990273714065552
# 국민        : 0.999026358127594
# 보호        : 0.9990026354789734
# 이민        : 0.9989940524101257
# 확인        : 0.9989255666732788

import codecs
from konlpy.tag import Twitter
from konlpy.tag import Okt
from gensim.models import word2vec # word2vec: 문장 내부의 단어를 벡터로 변환하는 도구
fp = codecs.open("trump_sppech.txt", "r", encoding="utf-8")
text = fp.read()
okt = Okt()
results = []
lines = text.split("\r\n")
for line in lines:
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip()
    results.append(rl)
    print(rl)
wakati_file = 'trump.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data,
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save("trump.model")
print("\n\n================ 분석 완료 ================")

model = word2vec.Word2Vec.load("trump.model")

print('\nStep2] 단어 빈도가 높은 어휘를 대상으로 유의어 분석')
similar_words = model.most_similar(positive=["미국"])
for word_set in similar_words:
    print(f'{word_set[0]:<10}: {word_set[1]}')
