from flask import Flask, request, jsonify, render_template
from yieldprediction import predict_yield
import pickle

app = Flask(__name__, template_folder="Templates")

# Load the trained model
model = pickle.load(open('prediction.pkl', 'rb'))

@app.route('/')
def another_page():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def predict():
    # prediction = None  # Initialize prediction variable
    if request.method == 'POST':
        # Get input data from request
        Acre = request.form.get('Acre', type=float)
        Residue_length = request.form.get('Residue_length', type=float)
        Urea = request.form.get('Urea', type=float)
        Cult_land = request.form.get('Cult_land', type=float)
        Harv_hand_rent = request.form.get('Harv_hand_rent', type=float)
        
        # Check if any key is missing
        if None in [Acre, Residue_length, Urea, Cult_land, Harv_hand_rent]:
            return jsonify({'error': 'Missing input data'}), 400
        
        # Perform prediction using input data
        prediction = predict_yield(Acre, Residue_length, Urea, Cult_land, Harv_hand_rent)
        
        if prediction is None:
            return jsonify({'error': 'Failed to make prediction'}), 500
        
        print("Received POST request. Input data:")
        print("Acre:", Acre)
        print("Residue_length:", Residue_length)
        print("Urea:", Urea)
        print("Cult_land:", Cult_land)
        print("Harv_hand_rent:", Harv_hand_rent)

        return jsonify({'prediction': prediction.tolist()})
    
    # For GET requests, render the HTML template
    return render_template('index.html', prediction_text=None)

if __name__ == '__main__': 
    app.run(debug=True)
