import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_questions.build import q01_load_data_questions
path = 'data/train.csv'

def q06_TF_IDF(path):
    "write your solution here"
    length, mean_duplicate, duplicate_count, df_train = q01_load_data_questions(path)
    tfidf = TfidfVectorizer(analyzer='word',
                            stop_words='english',
                            lowercase=True,
                            max_features=300,
                            norm='l1')
    BagOfWords = pd.concat([df_train.question1, df_train.question2], axis=0)
    tfidf.fit(BagOfWords.values.astype('str'))
    train_q1_tfidf = tfidf.transform(df_train.question1.astype(str))
    train_q2_tfidf = tfidf.transform(df_train.question2.astype(str))
    X = abs(train_q1_tfidf - train_q2_tfidf)
    y = df_train['is_duplicate']
    return X, y
