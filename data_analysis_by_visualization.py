# -*- coding: utf-8 -*-
"""DATA ANALYSIS BY VISUALIZATION

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iYf88u5jZ97V1VJiTPoTXzNOp9CE89mK
"""

from google.colab import files
data_to_load = files.upload()

import pandas as pd
import plotly.graph_objects as go
import csv 

df = pd.read_csv("data1.csv")

student_df = df.loc[df['student_id']  == "TRL_987" ]
print(student_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
    x = student_df.groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
    y = [ "Level 1", "Level 2", "Level 3", "Level 4" ],
    orientation = 'h'
))
fig.show()