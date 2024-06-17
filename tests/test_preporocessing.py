from json import load
from app.utils.data_preprocessing import PreprocPipeline
import pandas as pd
import numpy as np


#Testing if loading pipeline works

data = {
    'transaction_id': [1, 2, 3],
    'amount(usd)': [100.0, 200.0, 300.0],
    'lat': [34.05, 36.16, 40.71],
    'long': [-118.24, -115.15, -74.01],
    'merch_lat': [34.05, 36.16, 40.71],
    'merch_long': [-118.24, -115.15, -74.01],
    'age': [25, 35, 45],
    'merchant': ['A', 'B', 'A'],
    'job': ['engineer', 'doctor', 'teacher'],
    'hour_of_day': [12, 15, 18],
    'month': [1, 2, 3],
    'day_of_week': [1, 2, 3]
}

df = pd.DataFrame(data)

# Instantiate the pipeline
pipeline = PreprocPipeline()

# Fit the pipeline
pipeline.fit(df)

# Save the pipeline
pipeline.save_pipeline()

loaded_pipeline = PreprocPipeline.load_pipeline()

loaded_pipeline.transform(df)
