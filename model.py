import pandas as pd
import pickle
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# iris = datasets.load_iris()
# X, y = iris.data, iris.target

# clf = svm.SVC()
# clf.fit(X, y)  

# # save
# with open('model/model.pkl','wb') as f:
#     pickle.dump(clf,f)

# Load the Iris dataset from a CSV file
data = pd.read_csv('model/iris.csv')

# Split the data into features (X) and labels (y)
X = data.drop('species', axis=1)
y = data['species']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a machine learning model on the training data
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save the trained model to a pickle file
with open('model/iris.pkl', 'wb') as f:
    pickle.dump(clf, f)
