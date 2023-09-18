# SimpleDocker_ML_App

Learning how to deploy ML app with FastAPI and Docker. 

First, create a simple FastAPI application to serve a machine learning model. For the simplicity, the programm use LogisticRegression to predict which type of the iris (based on the well-known Iris dataset). 

```Python

    # main.py
    from fastapi import FastAPI
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression
    app = FastAPI()
    # Load dataset and train a simple model
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression().fit(X, y)
    @app.get("/predict/")
    def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
        prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        return {"prediction": int(prediction[0])}

```

Then, create a Dockerfile for the program. Each instruction creates a new layer in the Docker image, and they’re executed in sequence to build the final image. 

```Docker

    # Use an official Python runtime as a base image
    FROM python:3.8-slim
    # Set the working directory
    WORKDIR /app
    # Install dependencies
    COPY requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    # Copy the current directory contents into the container at /app
    COPY . .
    # Expose port 8000 for FastAPI
    EXPOSE 8000
    # Run main.py when the container launches
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```

To run the Dockerfile, navigate the cmd to the directory that is currently dealt with. 

```CMD
docker build -t simpledocker_ml_app .
docker run -p 8000:8000 simpledocker_ml_app
```

Visit http://localhost:8000/predict/?sepal_length=5.1&sepal_width=3.5&petal_length=1.4&petal_width=0.2 in your browser. You should see a prediction output.