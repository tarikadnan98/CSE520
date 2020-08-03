import pandas as pd
import stemgraphic
import matplotlib.pyplot as plt
col_name = input("Type the feature name to plot stem-leaf: ")
input_scale = float(input("Input scale to plot stem-leaf: "))

data = pd.read_csv('F:/File/Car_data.csv')[col_name]
y = pd.Series(data)
fig, ax = stemgraphic.stem_graphic(data, scale=input_scale)
fig.set_figheight(10)
fig.set_figwidth(6)

plt.title('Stem-Leaf plot of feature:' + " " + col_name)
plt.show()
