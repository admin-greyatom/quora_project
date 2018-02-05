import os
import sys
import xgboost as xgb
from sklearn.model_selection import train_test_split
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q06_TF_IDF.build import q06_TF_IDF
from sklearn.metrics import roc_auc_score

path  = 'data/train.csv'
path1 = 'data/test.csv'


def q07_XGBoost():
 
