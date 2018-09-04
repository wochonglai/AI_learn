# -*- coding: utf-8 -*-
'''词型还原'''
import nltk.stem as ns
words = ['table', 'probably', 'wolves', 'playing', 'is',
         'dog', 'the', 'beaches', 'grounded', 'dreamt',
         'envision']
# 词形还原器
lmm = ns.WordNetLemmatizer()
for word in words:
    n = lmm.lemmatize(word, pos='n')  # 名词
    v = lmm.lemmatize(word, pos='v')  # 动词
    print('{:10} {:10} {:10}'.format(word, n, v))
