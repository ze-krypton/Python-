import pandas as pd
import numpy as np

data = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5, np.nan, 7, 8, 9, 10]
})
data.fillna(data.mean(), inplace=True)
print(data)