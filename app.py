from flask import Flask, render_template, request, jsonify
from model import predict_stock_price

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the main HTML page (templates/index.html)
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract stock symbol or parameters from POST request (JSON or form data)
    data = request.get_json()
    symbol = data.get('symbol')

    # Run your Python prediction function
    predicted_prices = predict_stock_price(symbol)

    # Return prediction results as JSON
    return jsonify(predicted=predicted_prices)

if __name__ == '__main__':
    app.run(debug=True)
