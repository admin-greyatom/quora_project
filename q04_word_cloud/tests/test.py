import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q04_word_cloud
from inspect import getargspec
import pandas

path = "data/train.csv"
df = q04_word_cloud(path)


class TestRead_csv_data_to_df(TestCase):
    def test_args(self):
        arg = getargspec(q04_word_cloud).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))


