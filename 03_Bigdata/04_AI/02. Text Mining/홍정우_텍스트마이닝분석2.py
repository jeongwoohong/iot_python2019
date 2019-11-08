from gensim.models import word2vec

model = word2vec.Word2Vec.load("trump.model")

print('\nStep2] 단어 빈도가 높은 어휘를 대상으로 유의어 분석')
similar_words = model.most_similar(positive=["미국"])
for word_set in similar_words:
    print(f'{word_set[0]:<10}: {word_set[1]}')
