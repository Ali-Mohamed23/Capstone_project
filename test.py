import requests

# Endpoint URL
url = 'http://127.0.0.1:5000/predict'

# Input should be in the following format because model expects the features to be in the order it was trained on
'''
children                          0.0
deposit_type                      0.0
hotel                             1.0
adults                            2.0
distribution_channel              1.0
meal                              0.0
previous_cancellations            0.0
reserved_room_type                7.0
booking_changes                   0.0
stays_in_weekend_nights           0.0
customer_type                     2.0
assigned_room_type                7.0
arrival_date_year              2015.0
stays_in_week_nights              1.0
arrival_date_month                5.0
required_car_parking_spaces       0.0
total_of_special_requests         0.0
arrival_date_day_of_month         2.0
market_segment                    3.0
adr                             147.0
booking_lead_time              2015.0
arrival_date_week_number         27.0
lead_time                         0.0
country                         133.0
month                             7.0
'''

# Input data
data = {
    'children': 0,
    'deposit_type': 'No Deposit',
    'hotel': 'Resort Hotel',
    'adults': 2,
    'distribution_channel': 'TA/TO',
    'meal': 'BB',
    'previous_cancellations': 0,
    'reserved_room_type': 'A',
    'booking_changes': 0,
    'stays_in_weekend_nights': 2,
    'customer_type': 'Transient',
    'assigned_room_type': 'A',
    'arrival_date_year': 2015,
    'stays_in_week_nights': 5,
    'arrival_date_month': 'August',
    'required_car_parking_spaces': 0,
    'total_of_special_requests': 1,
    'arrival_date_day_of_month': 1,
    'market_segment': 'Online TA',
    'adr': 100,
    'booking_lead_time': 2015, 
    'arrival_date_week_number': 32,
    'lead_time': 50,
    'country': 'USA',
    'month': 7.0
}

data_canc = {
    'children': 0,
    'deposit_type': 'No Deposit',
    'hotel': 'Resort Hotel',
    'adults': 2,
    'distribution_channel': 'TA/TO',
    'meal': 'BB',
    'previous_cancellations': 0,
    'reserved_room_type': 'D',
    'booking_changes': 0,
    'stays_in_weekend_nights': 0,
    'customer_type': 'Transient',
    'assigned_room_type': 'D',
    'arrival_date_year': 2015,
    'stays_in_week_nights': 5,
    'arrival_date_month': 'July',
    'required_car_parking_spaces': 0,
    'total_of_special_requests': 0,
    'arrival_date_day_of_month': 4,
    'market_segment': 'Online TA',
    'adr': 113,
    'booking_lead_time': 1982, 
    'arrival_date_week_number': 27,
    'lead_time': 33,
    'country': 'PRT',
    'month': 7.0
}

try:
    # Send POST request
    response = requests.post(url, json=data_canc)
    # Print response
    print(response.json())
except:
    print('An Error occured!')