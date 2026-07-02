import pandas as pd
import pickle
from pathlib import Path

path = Path('model/house_price_model.pkl')
data = pd.read_csv('data/cleaned_house_data.csv')
print('columns', data.columns.tolist())
print('shape', data.shape)
with open(path, 'rb') as f:
    model = pickle.load(f)
print(type(model))
print('has_predict', hasattr(model, 'predict'))
if hasattr(model, 'feature_names_in_'):
    print('feature_names_in_', list(model.feature_names_in_))
