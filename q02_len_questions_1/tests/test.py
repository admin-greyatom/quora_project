import sys, os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_len_questions_1
from inspect import getargspec
import pandas

path = "data/train.csv"
df = q02_len_questions_1(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q02_len_questions_1).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_type(self):
        self.assertIsInstance(df, pd.Series, "The Expected return type do not match with the return type")

