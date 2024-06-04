import pandas as pd
class PreprocPipeline:
    '''
    Custom transformer for data preprocessing
    '''
    def __init__(self):
        self.drop_columns = ['oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'isFlaggedFraud']

    def preprocess_data(self, data):
        '''
        Preprocess the input data
        '''
        # Drop unnecessary columns
        data = data.drop(columns=self.drop_columns)
        
        # One-hot encode the 'type' feature
        data = pd.get_dummies(data, columns=['type'], drop_first=True)
        
        return data
