import pickle
import streamlit as st
import numpy as np

# Load the pickled model
model_file = pickle.load(open('model.pkl', 'rb'))

# Streamlit app title
st.title("Titanic Classification")

# Input variables
passenger_class = st.text_input("Enter the passenger class: (1/2/3)")
try:
    passenger_class = int(passenger_class)
except ValueError:
    st.error("Invalid input! Please enter a valid integer.")
sex = st.text_input("Enter your sex (Male/Female): ")
if sex == "Male" or sex == "male":
    sex = 0
elif sex == "Female" or sex == "female":
    sex = 1
else:
    st.error('Invalid Input!')

age = st.text_input("Enter their age: ")
try:
    age = int(age)
except ValueError:
    st.error("Invalid age input! Please enter a number.")

sibsp = st.text_input("Enter their Siblings: ")
try:
    sibsp = int(sibsp)
except ValueError:
    st.error("Invalid siblings input! Please enter a number.")

parch = st.text_input("Enter their parch: ")
try:
    parch = int(parch)
except ValueError:
    st.error("Invalid parch input! Please enter a number.")

fare = st.text_input("Enter their ticket Fare: ")
try:
    fare = float(fare)
except ValueError:
    st.error("Invalid fare input! Please enter a number.")

embarked = st.text_input("Enter their Port of Embarked: (C=Cherbourg | Q=Queentown | S=Southampton) ")
if embarked == "C" or embarked == "c":
    embarked = 1
elif embarked == "S" or embarked == "s":
    embarked = 0
elif embarked == "Q" or embarked == "q":
    embarked = 2
else:
    st.error("Invalid Input!")

# Button to predict
if st.button('Predict'):
    user_input = [passenger_class, sex, age, sibsp, parch, fare, embarked]
    model_input = np.array(user_input)
    make_prediction = model_file.predict(model_input.reshape(-1, 7))

    if make_prediction == 0:
        make_prediction = "Not Survived :("
    elif make_prediction == 1:
        make_prediction = "Survived :)"

    st.success(make_prediction)