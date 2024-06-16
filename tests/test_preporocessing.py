from app.utils.data_preprocessing import PreprocPipeline
import pandas as pd
import numpy as np


data = pd.read_csv('data/processed/processed_train.csv')

df = data.copy()

preprocessor = PreprocPipeline()

X = df.copy()
X = preprocessor.select_features(X)

# save the new dataframe
X.to_csv('data/test/processed_train_selected.csv', index=False)