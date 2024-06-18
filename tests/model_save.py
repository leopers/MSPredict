from sklearn.tree import DecisionTreeRegressor
from app.utils.model import Model

# Create Model 
model = Model(DecisionTreeRegressor())

model.set_name('Decision Tree Regressor')

#save model
model.save_model('tests/test_model.pkl')

# Load model
loaded_model = model.load_model('tests/files/test_model.pkl')
loaded_model_name = loaded_model.get_name()

print(loaded_model_name)