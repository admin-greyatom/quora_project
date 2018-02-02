import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
pal = sns.color_palette()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_questions.build import q01_load_data_questions


plt.switch_backend('agg')
path = 'data/train.csv'

def q02_len_questions_1(path):
    length, mean_duplicate, duplicate_count, df_train = q01_load_data_questions(path)
    train_qs = pd.Series(df_train['question1'].tolist() + df_train['question2'].tolist()).astype(str)
    dist_train = train_qs.apply(len)
    plt.hist(dist_train,bins=200, range=[0, 200], color=pal[2], normed=True, label='train')
    plt.title('Normalised histogram of character count in questions', fontsize=15)
    plt.legend()
    plt.xlabel('Number of characters', fontsize=15)
    plt.ylabel('Probability', fontsize=15)
    plt.show()
    return train_qs

