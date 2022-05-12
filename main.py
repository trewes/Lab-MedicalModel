"""
Logistic regression model evaluated homomorphically using Zama's concrete-ml



"""


#some imports
import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression as SklearnLogisticRegression
from sklearn.model_selection import train_test_split

from concrete.ml.sklearn import LogisticRegression as ConcreteLogisticRegression



print("Hello")