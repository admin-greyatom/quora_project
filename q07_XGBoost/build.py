import os
import sys
import xgboost as xgb
from sklearn.model_selection import train_test_split
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from q06_TF_IDF.build import q06_TF_IDF
from sklearn.metrics import roc_auc_score

path  = 'data/train.csv'
path1 = 'data/test.csv'


def q07_XGBoost(path):
    "write your solution here"
    X, y = q06_TF_IDF(path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    params = {}
    params['objective'] = 'binary:logistic'
    params['eval_metric'] = 'logloss'
    params['eta'] = 0.02
    params['max_depth'] = 4

    d_train = xgb.DMatrix(X_train, label=y_train)
    d_valid = xgb.DMatrix(X_test, label=y_test)

    watchlist = [(d_train, 'train'), (d_valid, 'valid')]

    bst = xgb.train(params, d_train, 400, watchlist, early_stopping_rounds=50)
    test_X, test_y = q06_TF_IDF(path1)
    d_test = xgb.DMatrix(test_X, label=test_y)
    p_test = bst.predict(d_test)
    score =roc_auc_score(test_y, p_test)
    return score

