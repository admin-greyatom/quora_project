import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q05_semantic_analysis
from inspect import getargspec
import pandas

path = "data/train.csv"
df = q05_semantic_analysis(path)


class Test_word_cloud(TestCase):
    def test_args(self):
        arg = getargspec(q05_semantic_analysis).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_length(self):
        self.assertEqual(df, (0.9988, 0.0012, 0.0631, 0.9981, 0.9995, 0.1181),
                         "The Expected return values do not match with the value returned")
