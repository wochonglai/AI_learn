# -*- coding: utf-8 -*-
import nltk.tokenize as tk  #分词包


doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)
# 基于句子分词
tokens = tk.sent_tokenize(doc)
for i, token in enumerate(tokens):
    print(i + 1, token)
print(1,'+'*19)
# 基于单词的拆分
tokens = tk.word_tokenize(doc)
for i, token in enumerate(tokens):
    print(i + 1, token)
print(2,'+'*19)

# 单词标点分词器对象,会以所有标点拆分
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print(i + 1, token)
