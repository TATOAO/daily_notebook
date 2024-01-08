import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))

sns.pairplot(df)
