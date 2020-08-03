import csv
import numpy as np
import pandas
import matplotlib.pyplot as plt
import glob

files = glob.glob('F:/File/*.csv')
fig = plt.figure(figsize=(4, 6))

for file in files:
    df = pandas.read_csv(file)

    # LABELS = ["real", "user", "sys"]

    plt.title('Time Taken by Classifier')
    plt.xlabel('Time_Types')
    plt.ylabel('Time_Value in (sec)')
    df.boxplot(column=['wt'])
    plt.show()
