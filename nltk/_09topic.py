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
