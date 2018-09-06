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
