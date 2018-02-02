import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q02_len_questions
from inspect import getargspec
import pandas

path = "data/train.csv"
df = q02_len_questions(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q02_len_questions).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))


