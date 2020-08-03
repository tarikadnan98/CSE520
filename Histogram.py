import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('F:/File/Car_data.csv', quoting=3)['mpg']
plt.hist(data, bins=20)
plt.xlim([0, 40])
plt.ylabel('Frequency')
plt.xlabel('mpg')
plt.title('Histogram of mpg')
plt.show()
