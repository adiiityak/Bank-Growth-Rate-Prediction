import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
import matplotlib 
import warnings
from sklearn.preprocessing import StandardScaler
# from sklearn.exceptions import InconsistentVersionWarning
# warnings.simplefilter("error", InconsistentVersionWarning)



# Load the model
model = pickle.load(open('Bank_Growth_Rate_Prediction.pkl', 'rb'))


def bank_groth_rate_prediction(input_data):
    input_data_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshaped)
    return prediction

def main():
    st.title('Bank Growth Rate Prediction Web App')
    
   
    st.sidebar.title('Predict Bank Growth Rate')
    st.sidebar.write("Enter data to predict if a member will leave the bank or not:")
    age = st.sidebar.text_input('Enter age')
    creditscore = st.sidebar.text_input('Enter credit score')
    tenure = st.sidebar.text_input('Enter tenure')
    balance = st.sidebar.text_input('Enter balance')
    numOfProducts = st.sidebar.text_input('Enter num of products')
    hasCrCard = st.sidebar.text_input('Do Member have credit card? (1 or 0)')
    isActiveMember = st.sidebar.text_input('Member is Active? (1 or 0)')
    estimatedSalary = st.sidebar.text_input('Enter estimated salary')
    geography_Germany = st.sidebar.text_input('From germany? (1 or 0)')
    geography_Spain = st.sidebar.text_input('From Spain (1 or 0)')
    gender_Male = st.sidebar.text_input('Is the person male? (1 or 0)')
    
    
    if st.sidebar.button('Predict'):
        prediction = bank_groth_rate_prediction([creditscore, age, tenure, balance, numOfProducts, hasCrCard, isActiveMember, estimatedSalary, geography_Germany, geography_Spain, gender_Male])
        if prediction == 0:
            st.sidebar.success("The member will not leave the bank")
        else:
            st.sidebar.success("The member will leave the bank")
    
    
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        
        st.write("Uploaded Data:")
        st.write(df)
        
        
        predictions = []
        for index, row in df.iterrows():
            input_data = row.drop('Exited').tolist()  # Exclude 'Exited' column from input
            prediction = bank_groth_rate_prediction(input_data)
            predictions.append(prediction)
        
        
        df['Prediction'] = predictions
        
       
        leave_count = (df['Prediction'] == 1).sum()
        stay_count = len(df) - leave_count
        
        
        stay_percentage = (stay_count / len(df)) * 100
        
        
        st.write(f"Number of members who left the bank: {leave_count}")
        st.write(f"Number of members who stayed in the bank: {stay_count}")
        st.write(f"Percentage of members who stayed in the bank: {stay_percentage:.2f}%")
        
       
        st.write("Predictions:")
        st.write(df[['Prediction']])

if __name__ == '__main__':
    main()