import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# with open('model/model.pkl', 'rb') as f:
#     model = pickle.load(f)
    
with open('model/iris.pkl', 'rb') as f:
    model = pickle.load(f)
    
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Get the input data from the form
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        # Make predictions on the input data
        input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction = model.predict(input_data)[0]
        # Render the template with the prediction
        return render_template('predict.html', prediction=prediction)
    # Render the template without a prediction
    return render_template('predict.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the input data from the request
#     data = request.get_json(force=True)
#     # Make predictions on the input data
#     predictions = model.predict(data['input'])
#     # Return the predictions as a JSON object
#     return jsonify(predictions=predictions.tolist())

if __name__ == '__main__':
    app.run(port=5000, debug=True)