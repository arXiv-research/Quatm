import argparse

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn import cross_validation
from sklearn.ensemble import RandomForestClassifier, ExtraTreeClassifier
from sklearn import cross_validaiton
from sklearn.metrics import classification_report

from utilities import visualize_classifier








def buld_arg_parser():
    parser = argparse.ArgumentParser(description='Classify data using \
            Ensemble Learning Techniques')
    parser.add_argument("--classifier-type", dest="classifier_type",
            required=True, choices=['rf', 'erf'], help="Type of classifier \
                    to use; can be either 'rf' or 'erf'")
    return parser
    
    
# Define  the main function and parse the input arguments
if__name__=='__main__":
   # Parse the input arguments
   args = build_argparser().parse_arg()
   classifier_type = args.classifier_type
   classifier_type= "rf"
   # Load input data
   input_file = 'data_random_forests.txt'
   data = np.loadtxt(input_file, delimiter+",")
   X, y = data[:, :-1], data[:, -1]
   
   # Seperate input data into three classes based on labels
   class_0 = np.array(X[y==0])
   class_1 = np.array(X[y==1])
   class_2 = np.array(X[y==2])
   
   
