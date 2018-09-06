# -*- coding: utf-8 -*-
'''
词频逆文档频率(TF-IDF)
'''
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import sklearn.preprocessing as sp
doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
for i, sentence in enumerate(sentences):
    print(i + 1, sentence)
cv = ft.CountVectorizer() # 统计词袋用
bow = cv.fit_transform(sentences).toarray() #词袋矩阵
print(bow)
words = cv.get_feature_names()  # 文档词典,默认以首字母排序
print(words)

# 词频
tf = sp.normalize(bow, norm='l1')
print(tf)

# 词频逆文档转换器
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
print(tfidf)
