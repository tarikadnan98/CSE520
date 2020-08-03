import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({'col1':np.random.randint(0,9,100),
                   'col2':np.random.randint(2,12,100),
                   'col3':np.random.randint(4,14,100)})
df.head()
df.boxplot()
plt.show()