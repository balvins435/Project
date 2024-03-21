import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Load the pre-trained machine learning model
try:
    with open('prediction.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    print("Model type:", type(model))  # Check the type of the loaded model
except FileNotFoundError:
    print("Model file not found. Please ensure the correct path.")

# Define a function for preprocessing input features
def preprocess_input_features(input_features):
    try:
        # Convert input features to numpy array
        input_features = np.array(input_features)

        # Check if input_features is 1D or 2D array
        if input_features.ndim == 1:
            input_features = input_features.reshape(1, -1)

        # Perform data type conversion if necessary
        input_features = input_features.astype(float)

        # Perform feature scaling using StandardScaler
        scaler = StandardScaler()
        input_features_scaled = scaler.fit_transform(input_features)

        return input_features_scaled
    except Exception as e:
        print("Error occurred during preprocessing:", e)
        return None

def predict_yield(Acre, Residue_length, Urea, Cult_land, Harv_hand_rent):
    try:
        # Preprocess the input features
        input_features_scaled = preprocess_input_features([[Acre, Residue_length, Urea, Cult_land, Harv_hand_rent]])

        if input_features_scaled is not None:
            # Make the prediction
            print("Input features shape:", input_features_scaled.shape)  # For debugging
            prediction = model.predict(input_features_scaled)
            return prediction[0]
        else:
            return None
    except Exception as e:
        print("Error occurred during prediction:", e)
        return None
