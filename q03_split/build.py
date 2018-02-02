import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q02_len_questions_1.build import q02_len_questions_1
path = 'data/train.csv'

def q03_split(path):
    "write your solution here"
    train_qs = q02_len_questions_1(path)
    dist_train = train_qs.apply(lambda x: len(x.split(' ')))

    plt.figure(figsize=(15, 10))
    plt.hist(dist_train, bins=50, range=[0, 50], normed=True, label='train')
    plt.title('Normalised histogram of word count in questions', fontsize=15)
    plt.legend()
    plt.xlabel('Number of words', fontsize=15)
    plt.ylabel('Probability', fontsize=15)
    plt.savefig('images/q03_split.jpg')
    plt.axis('off')
    plt.show()



