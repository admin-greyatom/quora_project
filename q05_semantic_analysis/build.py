import pandas as pd
import numpy as np
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q02_len_questions_1.build import q02_len_questions_1
path = 'data/train.csv'


def q05_semantic_analysis(path):
    "write your solution here"
    train_qs = q02_len_questions_1(path)
    qmarks = round(np.mean(train_qs.apply(lambda x: '?' in x)),4)
    math = round(np.mean(train_qs.apply(lambda x: '[math]' in x)),4)
    fullstop = round(np.mean(train_qs.apply(lambda x: '.' in x)),4)
    capital_first = round(np.mean(train_qs.apply(lambda x: x[0].isupper())),4)
    capitals = round(np.mean(train_qs.apply(lambda x: max([y.isupper() for y in x]))),4)
    numbers = round(np.mean(train_qs.apply(lambda x: max([y.isdigit() for y in x]))),4)
    return  qmarks, math, fullstop, capital_first, capitals, numbers

print q05_semantic_analysis(path)