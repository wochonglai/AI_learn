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
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)
dic = gc.Dictionary(lines_tokens)
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)  # 构造词袋----------
    bow.append(row)
n_topics = 2    # 主题个数
model = gm.LdaModel(bow, num_topics=n_topics,
                    id2word=dic)    # 可加参数 passes=25,提取严格程度
topics = model.print_topics(num_topics=n_topics,
                            num_words=4)    # num_words 每个主题提前主题词的个数
print(topics)
