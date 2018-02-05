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
def q04_word_cloud():
    
