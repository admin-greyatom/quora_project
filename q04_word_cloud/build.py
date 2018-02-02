import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from wordcloud import WordCloud
import sys
import os
import matplotlib.pyplot as plt
plt.switch_backend('agg')
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q02_len_questions_1.build import q02_len_questions_1

path = 'data/train.csv'
def q04_word_cloud(path):
    "write your solution here"
    train_qs = q02_len_questions_1(path)
    cloud = WordCloud(width=1440, height=1080).generate(" ".join(train_qs.astype(str)))
    plt.figure(figsize=(20, 15))
    plt.imshow(cloud)
    plt.axis('off')
