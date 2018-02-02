import pandas as pd
import numpy as np


path = 'data/train.csv'
def q01_load_data_questions(path):
    "write your solution here"
    df_train = pd.read_csv(path)
    length = len(df_train)
    mean_duplicate = round(df_train['is_duplicate'].mean()*100, 2)
    qids = pd.Series(df_train['qid1'].tolist() + df_train['qid2'].tolist())
    duplicate_count = np.sum(qids.value_counts() > 1)
    return length,mean_duplicate,duplicate_count,df_train

