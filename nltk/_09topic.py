# -*- coding: utf-8 -*-
'''
主题词抽取
'''
import warnings # 用于过滤模型多余的警告
warnings.filterwarnings('ignore', category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc
doc = []
with open('../data2/topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
tokenizer = tk.RegexpTokenizer(r'\w+')  # 基于正则表达式分词
stopwords = nc.stopwords.words('english')   # 去除非主要词
stemmer = sb.SnowballStemmer('english')     # 词干提取器
lines_tokens = []
