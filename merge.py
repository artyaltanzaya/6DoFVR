import pandas as pd
import numpy as np

path = r'.\dataset'

df0 = pd.read_csv(path + r'\dataset_myplace1_with_constraints_no6.csv',  encoding = 'utf8')
df1 = pd.read_csv(path+ r'\dataset_myplace2_with_constraints_no6.csv',  encoding = 'utf8')
df2 = pd.read_csv(path+ r'\dataset_myplace3_with_constraints_no6.csv',  encoding = 'utf8')

df = np.concatenate((df0, df1, df2), axis = 0)
df = pd.DataFrame(df)