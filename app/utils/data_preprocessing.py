import pandas as pd

def preprocess_data(data):
    # Drop unnecessary columns
    data = data.drop(columns=['oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest'])
    
    # One-hot encode the 'type' feature
    data = pd.get_dummies(data, columns=['type'], drop_first=True)
    
    return data