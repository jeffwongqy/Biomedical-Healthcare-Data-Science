import streamlit as st
import pickle 
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler

# load the model file 
with open("Desktop/water_quality/best_decision_tree_model.pkl", "rb") as f:
    dtc_model = pickle.load(f)

# load the training data 
X_train = pd.read_csv("Desktop/water_quality/X_train.csv")

# display the title of the webpage
st.title("Is the water safe for consumption?")

# display an image
st.image("Desktop/water_quality/water_quality.jpeg", width = 650)

with st.form(key = "my_form"):
    # prompt user for inputs 
    al = st.number_input("Enter the volume of Aluminium (per liter): ", format = "%.3f")
    am = st.number_input("Enter the volume of Ammonia (per liter): ", format = "%.3f")
    ar = st.number_input("Enter the volume of Arsenic (per liter): ", format = "%.3f")
    ba = st.number_input("Enter the volume of Barium (per liter): ", format = "%.3f")
    ca = st.number_input("Enter the volume of Cadmium (per liter): ", format = "%.3f")
    cl = st.number_input("Enter the volume of Chloramine (per liter): ", format = "%.3f")
    ch = st.number_input("Enter the volume of Chromium (per liter): ", format = "%.3f")
    cu = st.number_input("Enter the volume of Copper (per liter): ", format = "%.3f")
    f = st.number_input("Enter the volume of Fluoride (per liter): ", format = "%.3f")
    bacteria = st.number_input("Enter the volume of Bacteria (per liter): ", format = "%.3f")
    viruses = st.number_input("Enter the volume of Viruses (per liter): ", format = "%.3f")
    pb = st.number_input("Enter the volume of Lead (per liter): ", format = "%.3f")
    nitrates = st.number_input("Enter the volume of Nitrates (per liter): ", format = "%.3f")
    nitrites = st.number_input("Enter the volume of Nitrites (per liter): ", format = "%.3f")
    me = st.number_input("Enter the volume of Mercury (per liter): ", format = "%.3f")
    perchlorate = st.number_input("Enter the volume of Perchlorate (per liter): ", format = "%.3f")
    ra = st.number_input("Enter the volume of Radium (per liter): ", format = "%.3f")
    se = st.number_input("Enter the volume of Selenium (per liter): ", format = "%.3f")
    ag = st.number_input("Enter the volume of Silver (per liter): ", format = "%.3f")
    ur = st.number_input("Enter the volume of Uranium (per liter): ", format = "%.3f")

    predict_button = st.form_submit_button("Predict")

if predict_button:
    # convert input data into dataframe 
    user_inputs = {'aluminium': al, 
                'ammonia': am, 
                'arsenic': ar, 
                'barium': ba, 
                'cadmium': ca, 
                'chloramine': cl, 
                'chromium': ch, 
                'copper': cu, 
                'flouride': f, 
                'bacteria': bacteria, 
                'viruses': viruses, 
                'lead': pb, 
                'nitrates': nitrates, 
                'nitrites': nitrites, 
                'mercury': me, 
                'perchlorate': perchlorate, 
                'radium': ra, 
                'selenium': se, 
                'silver': ag, 
                'uranium': ur}
    user_inputs_df = pd.DataFrame.from_dict([user_inputs])

    # standardize the inputs 
    num_feature_names = X_train.select_dtypes(['int64', 'float64']).columns
    standard_scaler = StandardScaler()
    X_train[num_feature_names] = standard_scaler.fit_transform(X_train[num_feature_names])
    user_inputs_df[num_feature_names] = standard_scaler.transform(user_inputs_df[num_feature_names])

    # perform prediction 
    outcome = dtc_model.predict(user_inputs_df)

    # display the outcome 
    if outcome == 0:
        st.error("The water quality is not safe for consumption.")
    else:
        st.info("The water quality is safe for consumption.")