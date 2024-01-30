import pandas as pd
# import xgboost as xgb
# import category_encoders as ce
# import joblib
from flask import Flask, render_template, request, jsonify
from waitress import serve
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./tbproject-6b17f-firebase-adminsdk-gkhha-121b881af6.json")
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

# Load your pre-trained XGBoost model
# model = xgb.XGBClassifier(objective='binary:logistic', random_state=42)
# model.load_model('xgboost_model.model') # Load the model you saved

# Load your pre-trained CatBoost encoder
# cb_encoder = joblib.load('catboost_encoder.pkl') # Load the encoder you saveds1

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    print(request.form)
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
    current_health_facility_sector = request.form.get('HealthFacilitySector')
    diagnosing_health_facility_sector = request.form.get('DiagnosisHealthFacilitySector')
    basis_of_diagnosis = request.form.get('BasisOfDiagnosis')
    rbs = request.form.get('RBS')
    current_tobacco_user = request.form.get('CurrentTobaccoUser')
    ho_alcohol_intake = request.form.get('HO_AlcoholIntake')
    covid19_status = request.form.get('Covid19Status')
    pregnancy_status = request.form.get('PregnancyStatus')
    # state_of_tb = request.form.get('State_of_TB')
    # key_population = request.form.get('KeyPopulation')
    k_tobacco = request.form.get('hTobacco')
    k_Contact_of_Known_TB_Patient =request.form.get('hContactTB')
    K_Not_Applicable =  request.form.get('hNotApplicable')
    k_Bronchial_Asthma = request.form.get('hBronchialAsthma')
    k_Other = request.form.get('hOther')
    K_Urban_Slum =request.form.get('hUrbanSlum')
    K_Migrant = request.form.get('hMigrant')
    k_Health_Care_Worker = request.form.get('hHealthCareWorker')
    k_Diabetes = request.form.get('hDiabetes')
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
    import random
    doc_ref = db.collection("patient-data").document(str(random.randint(1, 10000)))
    doc_ref.set(dict(request.form))   
    user_input_df = pd.DataFrame(user_input_dict)

    # Ensure that categorical columns are of 'category' data type
    for col in user_input_df.select_dtypes(include=['object']).columns:
        user_input_df[col] = user_input_df[col].astype('category')

    # Encode categorical features using the CatBoost encoder
    # user_input_cb = cb_encoder.transform(user_input_df)

    # Use the trained XGBoost model to predict the probability for the user-provided test point
    # predicted_probabilities = model.predict_proba(user_input_cb)

    # Get the probability of class 1
    # probability_of_class_1 = predicted_probabilities[0][1]  # Probability of Class 1

    # Calculate the percentage from the probability
    # percentage = probability_of_class_1 * 100
    

    return f'<h1>Result</h1><p>Success percentage: 50%</p>'

    # return render_template('result.html', probability=probability_of_class_1, percentage=percentage)
    # return render_template('result.html', probability=0.3, percentage=10)


@app.route('/', methods=['GET'])
def home():
   print("SAIRAM from index.html")
   return render_template('index.html')

if __name__ == '__main__':
 app.run(host='127.0.0.1', port=8001)