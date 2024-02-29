import pandas as pd
import xgboost as xgb
import category_encoders as ce
import joblib
from flask import Flask, render_template, request, jsonify
import hashlib
from cachetools import LFUCache
import datetime as dt

app = Flask(__name__)

model = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
model.load_model('xgboost_model (2).model')

# Load the pre-trained category encoder
cb_encoder = joblib.load('catboost_encoder (1).pkl')

import firebase_admin
from firebase_admin import credentials, firestore, auth

cred = credentials.Certificate("./tbproject-6b17f-firebase-adminsdk-gkhha-4068ae14d9.json")
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()


# app = Flask(__name__)





cache = LFUCache(maxsize=1000) 
# Store logged-in status
logged_in = False

# Serve the index.html page
@app.route('/')
def index():
    return render_template('home.html')



# Signup endpoint
@app.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')
    


# Login endpoint
@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html')


# Logout endpoint
@app.route('/logout')
def logout():
    return render_template('logout.html')
    

@app.route('/verify')
def verify():
    return render_template('verify.html')



@app.route('/reset')
def reset():
    return render_template('forgot_password.html')

@app.route('/pdata')
def pdata():
    return render_template('p_data.html')


@app.route('/followup-details/<patientId>')
def followups(patientId):
    return render_template('test_p_data.html', patientId=patientId)


## PREDICTION SERVICE


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return render_template('predict.html')
    
    # Get the input values from the form
    
    
    print(request.form)
    patient_id = request.form.get('patientId')
    diagnosing_facility_state = request.form.get('DiagnosingFacilityState')
    diagnosing_facility_district = request.form.get('DiagnosingFacilityDistrict')
    diagnosing_facility_tbu = request.form.get('DTBUnit')
    diagnosing_facility_phi = request.form.get('DPHI')
    diagnosing_facility_phi_type = request.form.get('DiagnosingFacilityPHI')
    patient_status = request.form.get('Patient_Status')
    age = request.form.get('Age')
    gender = request.form.get('Gender')
    weight = request.form.get('Weight')
    # user_id_enrollment = request.form.get('UserID_Enrollment')
    hiv_status = request.form.get('HIV_Status')
    diabetes_status = request.form.get('DiabetesStatus')
    basis_of_diagnosis_test_name = request.form.get('basisOfDiagnosis_TestName')
    current_facility_district = request.form.get('CurrentFacilityDistrict')
    current_facility_tbu = request.form.get('CTBUnit')
    current_facility_phi = request.form.get('CPHI')
    current_facility_phi_type = request.form.get('CurrentFacilityPHI')
    type_of_case = request.form.get('TypeOfCase')
    site_of_disease = request.form.get('SiteOfDisease')
    ep_site = request.form.get('EPSite')
    bank_details_added = request.form.get('BankDetailsAdded')
    followup_done_count = request.form.get('FollowupDone_Count')
    contact_tracing_done = request.form.get('ContactTracing_Done')
    current_health_facility_sector = request.form.get('Current Health Facility Sector')
    diagnosing_health_facility_sector = request.form.get('Diagnosis Health Facility Sector')
    basis_of_diagnosis = request.form.get('BasisOfDiagnosis')
    rbs = request.form.get('RBS')
    current_tobacco_user = request.form.get('CurrentTobaccoUser')
    ho_alcohol_intake = request.form.get('HO_AlcoholIntake')
    covid19_status = request.form.get('Covid19Status')
    pregnancy_status = request.form.get('PregnancyStatus')
    # state_of_tb = request.form.get('State_of_TB')
    # key_population = request.form.get('KeyPopulation')
    k_tobacco = request.form.get('hTobacco')
    k_Contact_of_Known_TB_Patient =request.form.get('hContact of Known TB Patients')
    K_Not_Applicable =  request.form.get('hNot Applicable')
    k_Bronchial_Asthma = request.form.get('hBronchial Asthma')
    k_Other = request.form.get('hOther')
    K_Urban_Slum =request.form.get('hUrban Slum')
    K_Migrant = request.form.get('hMigrant')
    k_Health_Care_Worker = request.form.get('hHealth Care Worker')
    k_Diabetes = request.form.get('hDiabetes')


    # patient_id_ref = db.collection("patient-ids").document(str(patient_id))
    # patient_id_ref.set({'patientId': patient_id})
    # import random
     
    # Create a DataFrame from user input
    user_input_dict = {
        
        'DiagnosingFacilityState': [diagnosing_facility_state],
        'DiagnosingFacilityDistrict': [diagnosing_facility_district],
        'DiagnosingFacilityTBU': [diagnosing_facility_tbu],
        'DiagnosingFacilityPHI': [diagnosing_facility_phi],
        'DiagnosingFacilityPHIType': [diagnosing_facility_phi_type],
        'Patient_Status': [patient_status],
        'Age': [age],
        'Gender': [gender],
        'Weight': [weight],
        # 'UserID_Enrollment': [user_id_enrollment],
        'HIV_Status': [hiv_status],
        'DiabetesStatus': [diabetes_status],
        'basisOfDiagnosis_TestName': [basis_of_diagnosis_test_name],
        'CurrentFacilityDistrict': [current_facility_district],
        'CurrentFacilityTBU': [current_facility_tbu],
        'CurrentFacilityPHI': [current_facility_phi],
        'CurrentFacilityPHIType': [current_facility_phi_type],
        'TypeOfCase': [type_of_case],
        'SiteOfDisease': [site_of_disease],
        'EPSite': [ep_site],
        'BankDetailsAdded': [bank_details_added],
        'FollowupDone_Count': [followup_done_count],
        'ContactTracing_Done': [contact_tracing_done],
        'Current Health Facility Sector': [current_health_facility_sector],
        'Diagnosis Health Facility Sector': [diagnosing_health_facility_sector],
        'BasisOfDiagnosis': [basis_of_diagnosis],
        'RBS': [rbs],
        'CurrentTobaccoUser': [current_tobacco_user],
        'HO_AlcoholIntake': [ho_alcohol_intake],
        'Covid19Status': [covid19_status],
        'PregnancyStatus': [pregnancy_status],
        # 'State_of_TB': [state_of_tb],
        'Tobacco': [k_tobacco],
       'Contact of Known TB Patients': [k_Contact_of_Known_TB_Patient], 
       'Not Applicable': [K_Not_Applicable], 
       'Bronchial Asthma':[k_Bronchial_Asthma] ,
       'Other': [k_Other], 
       'Urban Slum':[K_Urban_Slum] , 
       'Migrant': [ K_Migrant], 
       'Health Care Worker':[k_Health_Care_Worker] , 
       'Diabetes': [k_Diabetes],
    
    }
  


   
    # Convert numerical columns to float
    

    # Load your encoder model (assuming it's already initialized and named cb_encoder)
    # cb_encoder = your_model_initialization()
    # Ensure that categorical columns are of 'category' data type
    user_input_df = pd.DataFrame(user_input_dict)

    for col in user_input_df.select_dtypes(include=['object']).columns:
        user_input_df[col] = user_input_df[col].astype('category')


    print(user_input_df.to_dict())
    # Encode categorical features using the CatBoost encoder

    numerical_columns = ['Age', 'Weight', 'FollowupDone_Count', 'RBS', 'Tobacco', 
                        'Contact of Known TB Patients', 'Not Applicable', 
                        'Bronchial Asthma', 'Other', 'Urban Slum', 'Migrant', 
                        'Health Care Worker', 'Diabetes']

    for col in numerical_columns:
        user_input_df[col] = user_input_df[col].astype(float)

    user_input_cb = cb_encoder.transform(user_input_df)

    # Use the trained XGBoost model to predict the probability for the user-provided test point
    predicted_probabilities = model.predict_proba(user_input_cb)
    print("Sairam predicted probabilities:", predicted_probabilities)
    # Get the probability of class 1
    success_prob = predicted_probabilities[0][0]  # Probability of Class 1
    
    # Calculate the percentage from the probability
    percentage_success = success_prob * 100

    # Format the result 
    new_result = percentage_success


    # Get the probability of class 1
    unsuccess_prob = predicted_probabilities[0][1]  # Probability of Class 1
    
    # Calculate the percentage from the probability
    percentage_unsuccess = unsuccess_prob * 100

    lfu_result = percentage_unsuccess

    

    # Store the new data and result in the database
    user_input_dict['patientId'] = patient_id
    user_input_dict['resultMessage'] = new_result
    user_input_dict['date'] = dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    for key in user_input_dict.keys():
        if type(user_input_dict[key]) == list:
            user_input_dict[key] = user_input_dict[key][0]

    print(user_input_dict)

    main_data_ref = db.collection("patient-data").add(user_input_dict)
    docref = db.collection("patients").document(str(patient_id))
    docref.set({
        'FollowupDone_Count': user_input_dict['FollowupDone_Count'], 
        'Age': user_input_dict['Age'], 
        'Gender': user_input_dict['Gender']
    })
    # main_data_ref.set(user_input_dict)
    # main_data_ref.update({'resultMessage': new_result})

    # # Update cache
    # cache[patient_id] = new_result

    return render_template('result.html', patient_id=patient_id, new_result = new_result, lfu_score=lfu_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)