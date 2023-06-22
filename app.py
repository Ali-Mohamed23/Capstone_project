from flask import Flask, request, jsonify
import pandas as pd
import pickle
import joblib
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the scaler
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Load the encoders dictionary
encoders = joblib.load('encoders.pkl')
le = LabelEncoder()

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.get_json()

    # Convert the data to dataframe
    input_df = pd.DataFrame.from_dict(input_data, orient='index').T

    # Preprocess the input data
    columns_to_encode = ['hotel', 'arrival_date_month', 'country', 'meal',
                            'market_segment', 'distribution_channel',
                            'reserved_room_type', 'assigned_room_type',
                            'deposit_type', 'customer_type']

    # Transform the new data using the loaded encoders
    for column in columns_to_encode:
        le = encoders[column]
        input_df[column] = le.transform(input_df[column])


    expected_feature_order = scaler.get_feature_names_out()
    input_df = input_df[expected_feature_order]
    
    # Perform data normalization
    input_scaled = scaler.transform(input_df)

    # Make the prediction
    prediction = model.predict(input_scaled)
    # Create a response dictionary
    response = {}

    # Check the prediction and add appropriate message to the response
    if prediction[0] == 1:
        response['message'] = "Receive 10% discount on booking, if deposit is made today"
    else:
        response['message'] = "Thank you for booking!"
    
    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)