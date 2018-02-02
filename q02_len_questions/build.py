import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_questions.build import q01_load_data_questions
plt.switch_backend('agg')

path = 'data/train.csv'


def q02_len_questions(path):
    "write your solution here"
    length, mean_duplicate, duplicate_count, df_train = q01_load_data_questions(path)
    qids = pd.Series(df_train['qid1'].tolist() + df_train['qid2'].tolist())
    plt.figure(figsize=(12, 5))
    plt.hist(qids.value_counts(), bins=50)
    plt.yscale('log', nonposy='clip')
    plt.title('Log-Histogram of question appearance counts')
    plt.xlabel('Number of occurences of question')
    plt.ylabel('Number of questions')
    plt.show()



