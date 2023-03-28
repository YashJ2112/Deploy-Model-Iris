## Iris Classifier Web App

This is a web application that uses a pre-trained machine learning model to classify Iris flowers based on their sepal length, sepal width, petal length, and petal width. The web app is built using the Flask web framework in Python.

## Installation

- Clone the repository
- Install the required dependencies by running `pip install -r requirements.txt`
- Run the application by executing `python app.py` in the command line
- Open your web browser and navigate to http://localhost:5000

## Usage

- Open the application in your web browser
- Enter values for the four input features (Sepal Length, Sepal Width, Petal Length, Petal Width) of an Iris flower you want to classify
- Click the "Predict" button
- The predicted class of the Iris flower will be displayed below the "Prediction" heading

## Files

- `app.py`: Flask web application that serves the classification model
- `model.py`: Python script that trains the Random Forest classification model and saves it as a pickle file
- `template/predict.html`: HTML template for the web form used to collect input data
- `template/home.html`: HTML template for the home page of the web application
- `model/iris.csv`: CSV file containing the Iris dataset used to train the classification model
- `model/iris.pkl`: Pickle file containing the trained Random Forest classification model

## Dependencies

- Flask==2.0.1
- scikit-learn==0.24.2
- pandas==1.3.4

### Credits

This project is based on the Iris dataset from the UCI Machine Learning Repository. The machine learning model is implemented using scikit-learn, and the web app is built using Flask.
