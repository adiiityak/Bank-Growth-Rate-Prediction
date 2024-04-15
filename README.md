## Bank Growth Rate Prediction
## Overview
Machine learning project aimed at Bank Growth Rate Prediction using the Random Forest algorithm. The project employs a Streamlit based web application to provide a user-friendly interface for predicting growth rate based on provided input data.

## Table of Contents
- [Installation](#installation)
- [Steps to Execute](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## Installation
To use this project locally, follow these steps:
1. Clone the repository:
   ```
   git clone https://github.com/adiiityak/Bank-Growth-Rate-Prediction.git
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Setup Anaconda environment:

4. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
5. Access the web application in your browser at `http://localhost:8501/`.

## Steps to Execute
The web application allows users to input customer data (such as credit score, age, tenure, balance, etc.) and get predictions. Users can input their data via the web interface and receive predictions in real-time.

To predict growth:
1. Fill in the required fields with customer information.
2. Click on the "Predict" button.
3. The application will generate a prediction based on the input data using the Random Forest algorithm.

## Project Structure
The project structure is organized as follows:
- `app.py`: Streamlit application handling web requests and model predictions.
- `test.ipynb`: Contains python code.
- `requirements`: Contains all dependencies used in the prediction
- `Bank_Growth_Rate_Prediction.pkl`: Contains the trained Random Forest model for growth rate prediction.
- `Dataset.csv`: Data used for training and testing the model.

## Dependencies
- ### Python 3:
  Python is a widely-used programming language in the field of data science and machine learning. It serves as the foundation for developing the entire project, including the web application and machine learning model.
- ### Streamlit==1.27.2: S
  Streamlit is a popular Python library for building interactive web applications for machine learning and data science projects. In this project, Streamlit is used to create the user-friendly interface that allows users to input customer data and receive predictions in real-time. Version 1.27.2 specifically indicates the version of Streamlit used, ensuring compatibility with other components of the project.
- ### Pandas==2.0.0:
  Pandas is a powerful library in Python used for data manipulation and analysis. In this project, Pandas likely plays a role in preprocessing the input data, handling missing values, and transforming the data into a format suitable for the machine learning model. Version 2.0.0 of Pandas is specified to ensure consistency and compatibility with the project.
- ### Scikit-learn==1.2.2:
  Scikit-learn is a popular machine learning library in Python that provides various algorithms and tools for building predictive models. In this project, Scikit-learn is used specifically for implementing the Random Forest algorithm, which predicts the bank growth rate based on the provided customer data. Version 1.2.2 is specified to ensure that the project utilizes the desired version with its corresponding features and bug fixes
- ### Numpy==1.23.1:
  NumPy is a fundamental package for numerical computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. In this project, NumPy likely aids in handling numerical data and performing computations required during the preprocessing and prediction stages. Version 1.23.1 is specified to ensure compatibility with other dependencies and maintain consistency in the project.
- ... (Other dependencies are listed in `requirements.txt`)

## Contributing
Contributions to improve the project are welcome! Here's how you can contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature`)
- Make modifications and commit changes (`git commit -am 'Add new feature'`)
- Push changes to the branch (`git push origin feature`)
- Create a pull request

Feel free to modify this README file to include more specific instructions, additional details about the model, or any other relevant information about your project. Good luck with your project!

### Model Screenshots

I've included screenshots from my Jupyter Notebook to showcase various aspects of the model's performance and insights.
![2](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/60d4875e-398c-48f0-b4b8-d7fe60f88c9b)

#### Feature Importance
![1 1](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/2e4b12bc-9787-4582-8c0e-3f82831f22d6)
![1 2](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/715a92c2-f40f-4fb5-91df-c60325d9f05d)
![1 3](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/68ad0211-db9a-439d-8a05-33e00575c5e4)

This screenshot demonstrates the feature importance plot generated from the Random Forest model, highlighting the key factors influencing prediction.
![3 2](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/845c072f-0ee3-4b32-89e7-ffe8969bb524)
![3 1](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/0320f13d-bd51-4225-baf8-a38b68303836)

#### Model Evaluation Metrics
![3](https://github.com/adiiityak/Bank-Growth-Rate-Prediction/assets/83272901/1debf226-a6dc-4eaf-865d-9e7297cd99b8)

