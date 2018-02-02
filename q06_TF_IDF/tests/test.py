import sys, os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q06_TF_IDF
from inspect import getargspec


path = "data/train.csv"
df = q06_TF_IDF(path)


class Test_TF_IDF(TestCase):
    def test_args(self):
        arg = getargspec(q06_TF_IDF).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))

    def test_return_shape(self):
        self.assertEqual(df[0].shape, (363861, 300),
                         "The Expected return values do not match with the value returned")
