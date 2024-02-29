import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
// import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

import { getFirestore, addDoc, getDocs, getDoc, doc, query, collection, where, orderBy } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
// import { getAuth, getRedirectResult, onAuthStateChanged, sendEmailVerification, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut } from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js';        // TODO: Add SDKs for Firebase products that you want to use
// Import the functions you need from the SDKs you need
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCWMH2CFCHt5-vwZgkasBEcGOAFDwmUoUE",
  authDomain: "tbproject-6b17f.firebaseapp.com",
  databaseURL: "https://tbproject-6b17f-default-rtdb.asia-southeast1.firebasedatabase.app",
  projectId: "tbproject-6b17f",
  storageBucket: "tbproject-6b17f.appspot.com",
  messagingSenderId: "498459381473",
  appId: "1:498459381473:web:36b8849a2558554c0d31a0",
  measurementId: "G-EPXSRMQJDL"
};

const app = initializeApp(firebaseConfig);
// const auth = getAuth(app);
const db = getFirestore(app);






$(document).ready(() => {
    let followUpDetails = [];
    function showFollowUpDetails(docId) 
    {
        // Display patient details

        let docSelected = followUpDetails.filter(doc => {
            return doc.id == docId;
        })[0];
        console.log(followUpDetails);
        console.log(docId, docSelected);
        const data = docSelected.data();
        document.getElementById('patientID').innerText = data.patientId;
        // document.getElementById('patientName').innerText = data.name;
        document.getElementById('patientAge').innerText = data.Age;
        document.getElementById('patientGender').innerText = data.Gender;
        document.getElementById('patientStatus').innerText = data.Patient_Status;
        document.getElementById('siteOfDisease').innerText = data.SiteOfDisease;
        document.getElementById('basis of diagnosis').innerText = data.BasisOfDiagnosis;
        document.getElementById('Contact tracing done').innerText = data.ContactTracing_Done;
        document.getElementById('DiagnosingFacilityDistrict').innerText = data.DiagnosingFacilityDistrict;
        document.getElementById('DiagnosingFacilityPHI').innerText = data.DiagnosingFacilityPHI;
        document.getElementById('DiagnosingFacilityPHIType').innerText = data.DiagnosingFacilityPHIType;
        document.getElementById('CurrentFacilityDistrict').innerText = data.CurrentFacilityDistrict;
        document.getElementById('CurrentFacilityTBU').innerText = data.CurrentFacilityTBU;
        document.getElementById('CurrentFacilityPHI').innerText = data.CurrentFacilityPHI;
        document.getElementById('CurrentFacilityPHIType').innerText = data.CurrentFacilityPHIType;
        document.getElementById('Diagnosis Health Facility Sector').innerText = data['Diagnosis Health Facility Sector'];
        document.getElementById('DiagnosingFacilityTBU').innerText = data.DiagnosingFacilityTBU;
        document.getElementById('EPSite').innerText = data.EPSite;
        document.getElementById('FollowupDone_Count').innerText = data.FollowupDone_Count;
        document.getElementById('HIV_Status').innerText = data.HIV_Status;
        document.getElementById('HO_AlcoholIntake').innerText = data.HO_AlcoholIntake;
        document.getElementById('Health Care Worker').innerText = data['Health Care Worker'];
        document.getElementById('Migrant').innerText = data.Migrant;
        document.getElementById('Not Applicable').innerText = data['Not Applicable'];
        document.getElementById('Other').innerText = data.Other;
        document.getElementById('PregnancyStatus').innerText = data.PregnancyStatus;
        document.getElementById('Tobacco').innerText = data.Tobacco;
        document.getElementById('TypeOfCase').innerText = data.TypeOfCase;
        document.getElementById('Urban Slum').innerText = data['Urban Slum'];
        document.getElementById('Weight').innerText = data.Weight;
        document.getElementById('basisOfDiagnosis_TestName').innerText = data.basisOfDiagnosis_TestName;
        document.getElementById('date').innerText = data.date;
        document.getElementById('resultMessage').innerText = data.resultMessage;
        document.getElementById('BankDetailsAdded').innerText = data.BankDetailsAdded;
        document.getElementById('Bronchial Asthma').innerText = data['Bronchial Asthma'];
        document.getElementById('Contact of Known TB Patients').innerText = data['Contact of Known TB Patients'];
        document.getElementById('Covid19Status').innerText = data.Covid19Status;
        document.getElementById('Current Health Facility Sector').innerText = data['Current Health Facility Sector'];
        document.getElementById('CurrentTobaccoUser').innerText = data.CurrentTobaccoUser;
        document.getElementById('Diabetes').innerText = data.Diabetes;
        document.getElementById('DiabetesStatus').innerText = data.DiabetesStatus;
        document.getElementById('DiagnosingFacilityState').innerText = data.DiagnosingFacilityState;
        document.getElementById('rbs').innerText = data.RBS;

        


        // Show patient details
        document.getElementById('patientDetails').style.display = 'block';
        
    }
    function getPatientDetails()
    {
        let patient_id = document.getElementById('patient_id').value;
        console.log(patient_id);
        const q = query(collection(db, 'patient-data'), where("patientId", "==", patient_id), orderBy('date', 'desc'));
        followUpDetails = [];
        let tableBody = document.getElementById('followUpTableBody');
        tableBody.innerHTML = '';
        getDocs(q).then((querySnapshot) => {
            querySnapshot.forEach((doc) => {
                const det = doc.data();
                followUpDetails.push(doc);
                let row = document.createElement('tr');
                console.log(doc);
                row.innerHTML = `
                    <td>${det.date}</td>
                    <td><button type="button" id="show_${doc.id}">Show</button></td>
                `
                tableBody.appendChild(row);


            
                $('#followUpTableBody').on('click', `#show_${doc.id}`, () => {
                    showFollowUpDetails(doc.id);
                });

                console.log(followUpDetails);
            });



        });

    }

    getPatientDetails();
    

    
    
});






