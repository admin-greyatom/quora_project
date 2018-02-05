import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q01_load_data_questions.build import q01_load_data_questions
path = 'data/train.csv'

def q06_TF_IDF():

