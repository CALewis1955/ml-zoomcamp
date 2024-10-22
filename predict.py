import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

def load_model(dv_path, model_path):
    with open(dv_path, 'rb') as f_dv:
        dv = pickle.load(f_dv)
    with open(model_path, 'rb') as f_model:
        model = pickle.load(f_model)
    
    return dv, model

dv, model = load_model('dv.bin', 'model1.bin')

features = {"job": "management", "duration": 400, "poutcome": "success"}

prediction = predict(dv, model, features)[0] 
prediction
