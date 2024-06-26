# -*- coding: utf-8 -*-
"""SVR(gridSearch).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dxPoq-v-LU01FPp12IfvjvoBi-K5jZQK
"""

import pandas as pd

df = pd.read_csv('Salary_Data.xls')

df.head()

import numpy as np

# Memisahkan atribut dan label
x = df['YearsExperience']
y = df['Salary']

# Mengubah bentuk atribut
x = np.array(x)
x = x.reshape(-1,1)

from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR

# Membangun model dengan parameter C, gamma, dan kernel
model = SVR()
parameters = {
    'kernel' : ['rbf'],
    'C' : [1000,10000,100000],
    'gamma' : [0.5, 0.05, 0.005]
}
grid_search = GridSearchCV(model, parameters)

# Melatih model dengan fungsi fit
grid_search.fit(x,y)

# Menampilkan parameter terbaik dari objek grid_search
print(grid_search.best_params_)

# Membuat model SVM baru dengan parameter terbaik hasil grid search
model_baru = SVR(C=100000, gamma=0.005, kernel='rbf')
model_baru.fit(x,y)

import matplotlib.pyplot as plt

plt.scatter(x,y)
plt.plot(x, model_baru.predict(x))

