
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
df.reindex()

df.iloc[0,0] = np.nan

df.dropna(subset=['A'], inplace=True)

pd.to_numeric(df, errors='coerce')
