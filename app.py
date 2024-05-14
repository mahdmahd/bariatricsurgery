import streamlit as st
import pandas as pd
import pickle

# Load the model
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define the Streamlit app
st.title('Weight Prediction After Bariatric Surgery')

# Create a form to input the new patient data
with st.form("prediction_form"):
    timestamp = st.number_input('Timestamp', min_value=0)
    sex = st.selectbox('Sex', options=[1, 2])
    age = st.number_input('Age', min_value=0)
    times_of_operation = st.number_input('Times of Operation', min_value=0)
    height = st.number_input('Height', min_value=0)
    weight = st.number_input('Weight', min_value=0)
    bmi = st.number_input('BMI', min_value=0.0)
    alcohol_lookup = st.selectbox('Alcohol Lookup', options=[0, 1])
    smoking_lookup = st.selectbox('Smoking Lookup', options=[0, 1])
    comorbidities = {
        'T2DM': st.selectbox('T2DM', options=[0, 1]),
        '100FBS125': st.selectbox('100FBS125', options=[0, 1]),
        'Dyslipidemia': st.selectbox('Dyslipidemia', options=[0, 1]),
        'Hypothyroidism': st.selectbox('Hypothyroidism', options=[0, 1]),
        'HTN': st.selectbox('HTN', options=[0, 1]),
        'CVD': st.selectbox('CVD', options=[0, 1]),
        'CVA': st.selectbox('CVA', options=[0, 1]),
        'DVTPE': st.selectbox('DVTPE', options=[0, 1]),
        'Varices': st.selectbox('Varices', options=[0, 1]),
        'SleepApnea': st.selectbox('Sleep Apnea', options=[0, 1]),
        'Asthma': st.selectbox('Asthma', options=[0, 1]),
        'Heartburn': st.selectbox('Heartburn', options=[0, 1]),
        'Lowbackpain': st.selectbox('Low Back Pain', options=[0, 1]),
        'Kneepain': st.selectbox('Knee Pain', options=[0, 1]),
        'Headache': st.selectbox('Headache', options=[0, 1]),
        'Psychiatricproblems': st.selectbox('Psychiatric Problems', options=[0, 1]),
        'Pseudotumorcerebri': st.selectbox('Pseudotumor Cerebri', options=[0, 1]),
        'Intertrigo': st.selectbox('Intertrigo', options=[0, 1]),
        'AbdoWallHernia': st.selectbox('Abdo Wall Hernia', options=[0, 1]),
        'MenstrualAb': st.selectbox('Menstrual Abnormalities', options=[0, 1]),
        'Hirsutism': st.selectbox('Hirsutism', options=[0, 1]),
        'Infertility': st.selectbox('Infertility', options=[0, 1]),
        'PCO': st.selectbox('PCO', options=[0, 1]),
        'Stressincontinency': st.selectbox('Stress Incontinency', options=[0, 1])
    }
    nutritn_habit = {
        'SweetEater': st.selectbox('Sweet Eater', options=[0, 1]),
        'VolumeEater': st.selectbox('Volume Eater', options=[0, 1]),
        'EmotionalEater': st.selectbox('Emotional Eater', options=[0, 1]),
        'SnackerNibbling': st.selectbox('Snacker Nibbling', options=[0, 1]),
        'None': st.selectbox('None', options=[0, 1])
    }
    family_history = {
        'Obesity': st.selectbox('Family History of Obesity', options=[0, 1]),
        'HTN': st.selectbox('Family History of HTN', options=[0, 1]),
        'T2DM': st.selectbox('Family History of T2DM', options=[0, 1]),
        'Cancer': st.selectbox('Family History of Cancer', options=[0, 1]),
        'None': st.selectbox('Family History of None', options=[0, 1])
    }
    drugs = {
        'Acetaminophen': st.selectbox('Acetaminophen', options=[0, 1]),
        'Alendronate': st.selectbox('Alendronate', options=[0, 1]),
        'Amlodipine': st.selectbox('Amlodipine', options=[0, 1]),
        'Aspirin': st.selectbox('Aspirin', options=[0, 1]),
        'Atenolol': st.selectbox('Atenolol', options=[0, 1]),
        'Atorvastatin': st.selectbox('Atorvastatin', options=[0, 1]),
        'Beclomethasone': st.selectbox('Beclomethasone', options=[0, 1]),
        'Captopril': st.selectbox('Captopril', options=[0, 1]),
        'Carvedilol': st.selectbox('Carvedilol', options=[0, 1]),
        'Chlordiazepoxide': st.selectbox('Chlordiazepoxide', options=[0, 1]),
        'Citalopram': st.selectbox('Citalopram', options=[0, 1]),
        'Clonazepam': st.selectbox('Clonazepam', options=[0, 1]),
        'CombinOralContracept': st.selectbox('Combin Oral Contracept', options=[0, 1]),
        'Diazepam': st.selectbox('Diazepam', options=[0, 1]),
        'Diclofenac': st.selectbox('Diclofenac', options=[0, 1]),
        'Digoxin': st.selectbox('Digoxin', options=[0, 1]),
        'Enalapril': st.selectbox('Enalapril', options=[0, 1]),
        'FenofibricAcid': st.selectbox('Fenofibric Acid', options=[0, 1]),
        'Fluoxetine': st.selectbox('Fluoxetine', options=[0, 1]),
        'Furosemide': st.selectbox('Furosemide', options=[0, 1]),
        'Gemfibrozil': st.selectbox('Gemfibrozil', options=[0, 1]),
        'Glibenclamide': st.selectbox('Glibenclamide', options=[0, 1]),
        'Hydrochlorothiazide': st.selectbox('Hydrochlorothiazide', options=[0, 1]),
        'Hydroxychloroqin': st.selectbox('Hydroxychloroqin', options=[0, 1]),
        'Ibuprofen': st.selectbox('Ibuprofen', options=[0, 1]),
        'Indomethacin': st.selectbox('Indomethacin', options=[0, 1]),
        'Insulin': st.selectbox('Insulin', options=[0, 1]),
        'Ipratropiumbromide': st.selectbox('Ipratropiumbromide', options=[0, 1]),
        'Levothyroxine': st.selectbox('Levothyroxine', options=[0, 1]),
        'Lorazepam': st.selectbox('Lorazepam', options=[0, 1]),
        'Losartan': st.selectbox('Losartan', options=[0, 1]),
        'Metformin': st.selectbox('Metformin', options=[0, 1]),
        'Methotrexate': st.selectbox('Methotrexate', options=[0, 1]),
        'Metoprolol': st.selectbox('Metoprolol', options=[0, 1]),
        'Nitrocontin': st.selectbox('Nitrocontin', options=[0, 1]),
        'Nitroglycerin': st.selectbox('Nitroglycerin', options=[0, 1]),
        'Omeprazole': st.selectbox('Omeprazole', options=[0, 1]),
        'Pantoprazole': st.selectbox('Pantoprazole', options=[0, 1]),
        'Pioglitazone': st.selectbox('Pioglitazone', options=[0, 1]),
        'Prednisolone': st.selectbox('Prednisolone', options=[0, 1]),
        'Propranolol': st.selectbox('Propranolol', options=[0, 1]),
        'PropylThiouracil': st.selectbox('Propyl Thiouracil', options=[0, 1]),
        'Ranitidine': st.selectbox('Ranitidine', options=[0, 1]),
        'Respidon': st.selectbox('Respidon', options=[0, 1]),
        'Salbutamol': st.selectbox('Salbutamol', options=[0, 1]),
        'Salmeterol': st.selectbox('Salmeterol', options=[0, 1]),
        'Sertraline': st.selectbox('Sertraline', options=[0, 1]),
        'Simvastatin': st.selectbox('Simvastatin', options=[0, 1]),
        'Spironolactone': st.selectbox('Spironolactone', options=[0, 1]),
        'Topiramate': st.selectbox('Topiramate', options=[0, 1]),
        'Triamterene': st.selectbox('Triamterene', options=[0, 1]),
        'Valsartan': st.selectbox('Valsartan', options=[0, 1]),
        'Warfarin': st.selectbox('Warfarin', options=[0, 1])
    }
    surgery_type = st.selectbox('Surgery Type', options=[5, 6, 8])
    
    submitted = st.form_submit_button("Predict")

# On form submission, make predictions
if submitted:
    # Prepare the input data in the correct order
    input_data = {
        'Timestamp': [timestamp],
        'FV_Sex': [sex],
        'Age': [age],
        'FV_TimesofOperation': [times_of_operation],
        'FV_Height': [height],
        'FV_Weight': [weight],
        'FV_BMI': [bmi],
        'FV_Alcohol_Lookup_Name': [alcohol_lookup],
        'FV_Smoking_Lookup_Name': [smoking_lookup],
        'FV_Como_T2DM': [comorbidities['T2DM']],
        'FV_Como_100FBS125': [comorbidities['100FBS125']],
        'FV_Como_Dyslipidemia': [comorbidities['Dyslipidemia']],
        'FV_Como_Hypothyroidism': [comorbidities['Hypothyroidism']],
        'FV_Como_HTN': [comorbidities['HTN']],
        'FV_Como_CVD': [comorbidities['CVD']],
        'FV_Como_CVA': [comorbidities['CVA']],
        'FV_Como_DVTPE': [comorbidities['DVTPE']],
        'FV_Como_Varices': [comorbidities['Varices']],
        'FV_Como_SleepApnea': [comorbidities['SleepApnea']],
        'FV_Como_Asthma': [comorbidities['Asthma']],
        'FV_Como_Heartburn': [comorbidities['Heartburn']],
        'FV_Como_Lowbackpain': [comorbidities['Lowbackpain']],
        'FV_Como_Kneepain': [comorbidities['Kneepain']],
        'FV_Como_Headache': [comorbidities['Headache']],
        'FV_Como_Psychiatricproblems': [comorbidities['Psychiatricproblems']],
        'FV_Como_Pseudotumorcerebri': [comorbidities['Pseudotumorcerebri']],
        'FV_Como_Intertrigo': [comorbidities['Intertrigo']],
        'FV_Como_AbdoWallHernia': [comorbidities['AbdoWallHernia']],
        'FV_Como_MenstrualAb': [comorbidities['MenstrualAb']],
        'FV_Como_Hirsutism': [comorbidities['Hirsutism']],
        'FV_Como_Infertility': [comorbidities['Infertility']],
        'FV_Como_PCO': [comorbidities['PCO']],
        'FV_Como_Stressincontinency': [comorbidities['Stressincontinency']],
        'FV_NutritnHabit_SweetEater': [nutritn_habit['SweetEater']],
        'FV_NutritnHabit_VolumeEater': [nutritn_habit['VolumeEater']],
        'FV_NutritnHabit_EmotionalEater': [nutritn_habit['EmotionalEater']],
        'FV_NutritnHabit_SnackerNibbling': [nutritn_habit['SnackerNibbling']],
        'FV_NutritnHabit_None': [nutritn_habit['None']],
        'FV_FamilyHistory_Obesity': [family_history['Obesity']],
        'FV_FamilyHistory_HTN': [family_history['HTN']],
        'FV_FamilyHistory_T2DM': [family_history['T2DM']],
        'FV_FamilyHistory_Cancer': [family_history['Cancer']],
        'FV_FamilyHistory_None': [family_history['None']],
        'FV_Drug_Acetaminophen': [drugs['Acetaminophen']],
        'FV_Drug_Alendronate': [drugs['Alendronate']],
        'FV_Drug_Amlodipine': [drugs['Amlodipine']],
        'FV_Drug_Aspirin': [drugs['Aspirin']],
        'FV_Drug_Atenolol': [drugs['Atenolol']],
        'FV_Drug_Atorvastatin': [drugs['Atorvastatin']],
        'FV_Drug_beclomethasone': [drugs['Beclomethasone']],
        'FV_Drug_Captopril': [drugs['Captopril']],
        'FV_Drug_Carvedilol': [drugs['Carvedilol']],
        'FV_Drug_Chlordiazepoxide': [drugs['Chlordiazepoxide']],
        'FV_Drug_Citalopram': [drugs['Citalopram']],
        'FV_Drug_Clonazepam': [drugs['Clonazepam']],
        'FV_Drug_CombinOralContracept': [drugs['CombinOralContracept']],
        'FV_Drug_Diazepam': [drugs['Diazepam']],
        'FV_Drug_Diclofenac': [drugs['Diclofenac']],
        'FV_Drug_Digoxin': [drugs['Digoxin']],
        'FV_Drug_Enalapril': [drugs['Enalapril']],
        'FV_Drug_FenofibricAcid': [drugs['FenofibricAcid']],
        'FV_Drug_Fluoxetine': [drugs['Fluoxetine']],
        'FV_Drug_Furosemide': [drugs['Furosemide']],
        'FV_Drug_Gemfibrozil': [drugs['Gemfibrozil']],
        'FV_Drug_Glibenclamide': [drugs['Glibenclamide']],
        'FV_Drug_Hydrochlorothiazide': [drugs['Hydrochlorothiazide']],
        'FV_Drug_Hydroxychloroqin': [drugs['Hydroxychloroqin']],
        'FV_Drug_Ibuprofen': [drugs['Ibuprofen']],
        'FV_Drug_Indomethacin': [drugs['Indomethacin']],
        'FV_Drug_Insulin': [drugs['Insulin']],
        'FV_Drug_Ipratropiumbromide': [drugs['Ipratropiumbromide']],
        'FV_Drug_Levothyroxine': [drugs['Levothyroxine']],
        'FV_Drug_Lorazepam': [drugs['Lorazepam']],
        'FV_Drug_Losartan': [drugs['Losartan']],
        'FV_Drug_Metformin': [drugs['Metformin']],
        'FV_Drug_Methotrexate': [drugs['Methotrexate']],
        'FV_Drug_Metoprolol': [drugs['Metoprolol']],
        'FV_Drug_Nitrocontin': [drugs['Nitrocontin']],
        'FV_Drug_Nitroglycerin': [drugs['Nitroglycerin']],
        'FV_Drug_Omeprazole': [drugs['Omeprazole']],
        'FV_Drug_Pantoprazole': [drugs['Pantoprazole']],
        'FV_Drug_Pioglitazone': [drugs['Pioglitazone']],
        'FV_Drug_Prednisolone': [drugs['Prednisolone']],
        'FV_Drug_Propranolol': [drugs['Propranolol']],
        'FV_Drug_PropylThiouracil': [drugs['PropylThiouracil']],
        'FV_Drug_Ranitidine': [drugs['Ranitidine']],
        'FV_Drug_Respidon': [drugs['Respidon']],
        'FV_Drug_Salbutamol': [drugs['Salbutamol']],
        'FV_Drug_Salmeterol': [drugs['Salmeterol']],
        'FV_Drug_Sertraline': [drugs['Sertraline']],
        'FV_Drug_Simvastatin': [drugs['Simvastatin']],
        'FV_Drug_Spironolactone': [drugs['Spironolactone']],
        'FV_Drug_Topiramate': [drugs['Topiramate']],
        'FV_Drug_Triamterene': [drugs['Triamterene']],
        'FV_Drug_Valsartan': [drugs['Valsartan']],
        'FV_Drug_Warfarin': [drugs['Warfarin']],
        'SurgeryTypeName': [surgery_type]
    }

    input_df = pd.DataFrame(input_data)
    
    # Make prediction
    predicted_weight = model.predict(input_df)
    
    st.write(f"Predicted Weight for the new patient at timestamp {timestamp}: {predicted_weight[0]} kg")
