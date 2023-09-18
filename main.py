from fastapi import FastAPI
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
app = FastAPI()
# Load dataset and train a simple model
X, y = load_iris(return_X_y=True)
clf = LogisticRegression().fit(X, y)

@app.get('/')
def hello_word(): 
    return {'message': 'Hello world'}


@app.get("/predict/")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return {"prediction": int(prediction[0])}