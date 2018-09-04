# -*- coding: utf-8 -*-
'''
词干提取:
去除词中的次要成分,只保留与含义最相关的./
从单词中抽取主要成分，未必是合法的词汇。
'''
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb


words = ['table', 'probably', 'wolves', 'playing', 'is',
         'dog', 'the', 'beaches', 'grounded', 'dreamt',
         'envision']
# 各种不同的词干提取器,SnowballStemmer使用最多,LancasterStemmer提取更严,保留最少
porter = pt.PorterStemmer()
lancaster = lc.LancasterStemmer()
snowball = sb.SnowballStemmer('english')
for word in words:
    pstem = porter.stem(word)
    lstem = lancaster.stem(word)
    sstem = snowball.stem(word)
    print('{:10} {:10} {:10} {:10}'.format(
        word, pstem, lstem, sstem))
