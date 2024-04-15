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

# sc=[]
# model = []
model = pickle.load(open('Bank_Growth_Rate_Prediction.pkl', 'rb'))

def bank_groth_rate_prediction(input_data):
       input_data_numpy_array = np.asarray(input_data)
       print(input_data_numpy_array)
       #reshaping the array as the predcition is for one instance
       input_data_reshaped = input_data_numpy_array.reshape(1, -1)
       prediction = model.predict(input_data_reshaped)

       if (prediction==0):
            return "The member will not leave the bank"
       else:
            return "The member will leave the bank"



def main():
    
    
    # giving a title
    st.title('Bank Growth Rate Prediction Web App')
    
    
    # getting the input data from the user
    
    
    age = st.text_area('Enter age')
    creditscore = st.text_area('Enter credit score')
    tenure = st.text_area('Enter tenure')
    balance = st.text_area('Enter balance')
    numOfProducts = st.text_area('Enter num of products')
    hasCrCard = st.text_area('Do Member have credit card? (1 or 0)')
    isActiveMember = st.text_area('Member is Active? (1 or 0)')
    estimatedSalary = st.text_area('Enter estimated salary')
    geography_Germany = st.text_area('From germany? (1 or 0)')
    geography_Spain = st.text_area('From Spain (1 or 0)')
    # geography_France = st.text_area('From France (1 or 0)')
    gender_Male = st.text_area('Is the person male? (1 or 0)')
    
    
    # code for Prediction
    growth_rate = ''
    
    # creating a button for Prediction
    if st.button('Predict'):
        growth_rate = bank_groth_rate_prediction([creditscore, age, tenure, balance, numOfProducts, hasCrCard, isActiveMember, estimatedSalary, geography_Germany, geography_Spain, gender_Male])
        
        
    st.success(growth_rate)
    
    
if __name__ == '__main__':
    main()







