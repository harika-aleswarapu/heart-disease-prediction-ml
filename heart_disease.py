import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading dataset...")

# Load dataset(we'll add the csv next)
data=pd.read_csv("heart.csv")

print("\nFirst 5 rows:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nCheckimg for missing values:")
print(data.isnull().sum())
print("\nStatistical Summary:")
print(data.describe())

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading Dataset---")
data=mpd.read_csv("heart.csv")
