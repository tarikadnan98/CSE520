import pandas as pd
import matplotlib.pyplot as plt
col_name = input("Type the feature name to Histogram: ")

data = pd.read_csv('F:/File/Car_data.csv', quoting=3)[col_name]
plt.hist(data, bins=20)
plt.xlim([0, 40])
plt.ylabel('Frequency')
plt.xlabel('mpg')
plt.title('Histogram of feature:' + col_name)
plt.show()
