# -*- coding: utf-8 -*-
'''
性别识别
'''
import random
import numpy as np
import nltk.corpus as nc
import nltk.classify as cf
male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')
models, acs = [], []
for n_letters in range(1, 6):
    data = []
    for male_name in male_names:
        feature = {
            'feature': male_name[-n_letters:].lower()}  # 截取名字的后几个字母
        data.append((feature, 'male'))
    for female_name in female_names:
        feature = {
            'feature': female_name[-n_letters:].lower()}
        data.append((feature, 'female'))
    random.seed(7)
