import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q01_load_data_questions
from inspect import getargspec
import pandas

path = "data/train.csv"
df = q01_load_data_questions(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q01_load_data_questions).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_length(self):
        self.assertEqual(df[:3],(363861, 36.93, 98967), "The Expected return values do not match with the value returned")


    def test_return_type(self):
        self.assertIsInstance(df[3],pd.DataFrame, "The Expected return type do not match with the return type")
