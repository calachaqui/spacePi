#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gps_points.csv')

print(df.head())

BBox = (df.longitude.min(), df.longitude.max(),
         df.latitude.min(), df.latitude.max())

print(BBox)

#https://towardsdatascience.com/easy-steps-to-plot-geographic-data-on-a-map-python-11217859a2db
