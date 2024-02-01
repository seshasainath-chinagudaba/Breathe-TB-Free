from flask import Flask, render_template, request, jsonify
import pandas as pd
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./tbproject-e2a3f-firebase-adminsdk-stk15-cf6e246512.json")
firebase_app = firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)

# Store logged-in status
logged_in = False

# Serve the index.html page
@app.route('/')
def index():
    return render_template('home.html')

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    global logged_in
    username = request.form.get('username')
    password = request.form.get('password')

    if username == 'sairam' and password == 'sairam':
        logged_in = True
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'})


# @app.route('/signin')
# def signin():
#     return render_template('signin.html')


# Logout endpoint
@app.route('/logout')
def logout():
    global logged_in
    logged_in = False
    return jsonify({'success': True})
@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    
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


    patient_id_ref = db.collection("patient-ids").document(str(patient_id))
    patient_id_ref.set({'patientId': patient_id})
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
    patient_id_ref = db.collection("patient-ids").document(str(patient_id))
    existing_data = patient_id_ref.get()
    if existing_data.exists:
        existing_data = existing_data.to_dict()

        existing_result = existing_data.get('resultMessage', '')
        new_result = '70%'  # Replace this with your actual calculation

        improvement = False
        if new_result > existing_result:
            improvement = Positive

        main_data_ref = db.collection("patient-data").document(str(patient_id))
        data = dict(request.form)
        del data['patientId']
        main_data_ref.set(data)

        main_data_ref.update({'resultMessage': new_result, 'improvement': improvement})

        # Render the result template with the relevant data
        return render_template('result.html', patient_id=patient_id, existing_result=existing_result, new_result=new_result, improvement=improvement)

    else:
        patient_id_ref.set({'patientId': patient_id})

        # Your existing code for saving new data and predicting result goes here

        # Render a message for new patient ID
        return f'<h1>Result</h1><p>New patient ID, data saved.</p>'
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=80, debug=True)   
#     if existing_data.exists:
#         # Patient ID exists, retrieve the existing data
#         existing_data = existing_data.to_dict()

#         # Compare the existing result with the new result
#         existing_result = existing_data.get('resultMessage', '')
#         new_result = '70%'  # Replace this with your actual calculation

#         improvement = False
#         if new_result > existing_result:
#             improvement = True

#         # Update the database with new data and result
#         main_data_ref = db.collection("patient-data").document(str(patient_id))
#         data = dict(request.form)
#         del data['patientId']
#         main_data_ref.set(data)

#         # Update the result message and improvement status
#         main_data_ref.update({'resultMessage': new_result, 'improvement': improvement})

#         return f'<h1>Result</h1><p>Previous Result: {existing_result}, New Result: {new_result}, Improvement: {improvement}</p>'

#     else:
#         # Patient ID doesn't exist, create a new entry in the database
#         patient_id_ref.set({'patientId': patient_id})

#         # Your existing code for saving new data and predicting result goes here

#         return f'<h1>Result</h1><p>New patient ID, data saved.</p>'
#     # return render_template('result.html', probability=probability_of_class_1, percentage=percentage)
#     # return render_template('result.html', probability=0.3, percentage=10)


# # @app.route('/', methods=['GET'])
# # def home():
# #    print("SAIRAM from index.html")
# #    return render_template('index.html')

# # if __name__ == '__main__':
# #  app.run(host='127.0.0.1', port=8001)

# if __name__ == '__main__':
#     app.run(debug=True)


