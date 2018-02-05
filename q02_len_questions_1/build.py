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

def q02_len_questions_1():
    

