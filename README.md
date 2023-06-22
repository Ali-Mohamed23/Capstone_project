# Capstone_project

# Hotel Cancellation Project
### This project aims to analyze hotel booking data and build a model to predict hotel cancellations. The dataset used in this project contains information about bookings, including customer details, booking dates, and various hotel-related features.


To run this project, please follow these steps:

- Clone this repository to your local machine.
- First run the notebook Revenue_Time_series.ipynb as this will create the dataframe hotel_revenue.csv which will be used 
- Next run the Hotel_Cancellation_model.ipynb this will create the model.pkl, encoders, scaler that will all be used for flask api. 
- The model.pkl file is not located in this repository as the file size is too big.

Run the Flask application by executing python app.py.

- Access the API at http://127.0.0.1:5000/predict and send POST requests with appropriate data to get cancellation predictions.

# Project/Goals
- Identify strategies to maximize hotel revenue by understanding booking patterns, cancellations, and factors affecting occupancy rates and average daily rates (ADR).
- Train a time-series model to forecast revenue and cancellations.
- Build a classification model that predicts whether a booking will be cancelled
- Utilize acquired machine learning and data analytics tools and techniques to address real-world business challenges


# Exploratory Data Analysis

In this project, I performed an exploratory data analysis on the hotel bookings dataset to gain insights and understand the patterns and characteristics of the data. The following key findings were obtained:

Missing Values: I checked for missing values in the dataset and handled them appropriately by dropping unnecessary columns with a large number of missing values and removing rows with missing values in other columns.


Outlier Handling: I identified and handled outliers in the dataset, specifically focusing on the "adr" (average daily rate) column. Outliers were removed based on predefined upper and lower thresholds.

Lead Time and Cancellations: I observed that the average lead time for canceled bookings was higher than that for non-canceled bookings, indicating that longer lead times might be associated with higher cancellation rates.

Repeated Guests and Special Requests: Bookings made by repeated guests had a higher average number of total special requests, suggesting that guest loyalty might contribute to more personalized and demanding requests.

Meal Types and ADR: Certain meal types exhibited higher average daily rates (adr) compared to others, indicating potential price differentials based on meal plan options.

Market Segments and Lead Time: The distribution of lead time varied across different market segments, suggesting varying booking patterns and planning behavior among different customer segments.

Distribution Channels and Previous Cancellations: Bookings made through specific distribution channels had a higher average number of previous cancellations, suggesting potential differences in booking practices and cancellation rates based on the chosen channel.

Booking Changes and Previous Bookings: The number of booking changes was found to be positively correlated with the number of previous bookings not canceled, indicating a potential relationship between booking modifications and customer satisfaction.

Room Types and ADR: Certain room types exhibited higher average daily rates (adr) compared to others, suggesting variations in pricing based on room category.

Hotel Types and ADR: The average adr differed between different hotel types, indicating potential pricing differences between resort hotels and city hotels.

Reservation Status and Cancellations: The analysis revealed that around 27% of the bookings in the dataset were canceled, while 72% were not canceled.

Booking Patterns by Month and Hotel: We examined the reservation status and average daily rates (adr) in different months and across different hotel types, providing insights into seasonal trends and hotel-specific patterns.

Cancellations by Country: Identified the top 10 countries with the highest number of reservation cancellations, providing insights into the geographical distribution of cancellations.

Booking Patterns by Market Segment: We analyzed the market segments generating more bookings and calculated the cancellation rates by market segment, providing insights into the popularity and cancellation tendencies of different market segments.

The exploratory data analysis provided valuable insights into the dataset, which can be further utilized for modeling and decision-making purposes in the hotel industry.


# Process

## Data Preprocessing:

- Label encodes categorical columns using LabelEncoder.
- Balances the imbalanced dataset using random oversampling.
- Normalizes the numeric columns using MinMaxScaler.
- Splits the data into training and test sets using train_test_split.

## Feature Engineering:

- Uses a Random Forest Classifier to determine the importance of features.
- Selects the top 25 important features.
- Created feature for Vacancy 
- Created feature for Revenue

## Model Building and Evaluation:

Builds and evaluates different classification models:
- Decision Tree Classifier
- Random Forest Classifier
- Gaussian Naive Bayes
- Logistic Regression
- K-Nearest Neighbors (KNN)

## Saves the best fitted Random Forest Classifier model using pickle.

## Forecasting using tableau 

## Time-series model to forecast cancellation revenue created


## Builds an API using flask 
- Built a dashboard for the API so that input values can be entered and response generated

# Results: 

My random forest classifier was performing very well:

Random Forest Classifier : 
 --------------------------------------------------
Accuracy score: 96.29

ROC AUC score: 96.29

Classification Reoprt:
               precision    recall  f1-score   support

           0       0.97      0.96      0.96     11367
           1       0.96      0.97      0.96     11213

    accuracy                           0.96     22580
   macro avg       0.96      0.96      0.96     22580
weighted avg       0.96      0.96      0.96     22580


# Future Goals

1) Improve the dashboard for the API

2) Deploy on AWS

3) Create more forecasts

