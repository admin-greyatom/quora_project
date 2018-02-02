import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_XGBoost
from inspect import getargspec

path = 'data/train.csv'
score = q07_XGBoost(path)

class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q07_XGBoost).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_shape(self):
        self.assertGreaterEqual(score, 0.59,
                         "The Expected return values do not match with the value returned")
