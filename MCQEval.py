import numpy as np
import pandas as pd
import math
import csv 
from csv import reader, writer
import glob, os
from io import StringIO
import io

data = pd.read_csv('Test_Form.csv')
colms = ['Timestamp', 'Email_ID']
data.drop(colms, inplace=True, axis=1)
data = data.dropna(axis=0, how='all')

Names=data.Register_Number
data1 = data
data1.to_csv('First.csv', index=False)
#print(data1)

Q1 = "Capital of India"
Q2 = "This equation states that"
Q3 = "Data mining states that"
Q4 = "Capital of Chennai"

x1 = (data1["Capital_of_India"]=="Delhi") 
x2 = (data1["This_equation_states_that"]=="Laplace") 
x3 = (data1["Data_mining_states_that"]=="All the above") 
x4 = (data1["Capital_of_Chennai"]=="Trichy") 

res = np.array([x1,x2,x3,x4])
conv = res.astype(int)
#print(data1.to_string(index=False))
#print('',conv)

Res = pd.DataFrame(conv, columns=Names, 
                          index=[Q1, Q2, Q3, Q4])

Res.to_csv('ResltN.csv')

with open('ResltN.csv', 'r') as f, open('RESULT_NEW.csv', 'w') as fw: 
    writer(fw, delimiter=',').writerows(zip(*reader(f, delimiter=',')))

Tot = Res.sum(axis=0)
tot = Tot.values
cvv = pd.read_csv('RESULT_NEW.csv', index_col=[0])
cvv['Total'] = tot 
cvv.to_csv('NewResultNew.csv', index=True)
