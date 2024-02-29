import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
// import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";
import { getAuth } from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js';        // TODO: Add SDKs for Firebase products that you want to use
import { getFirestore, addDoc, getDocs, getDoc, doc, query, orderBy, collection, where } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
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
const auth = getAuth(app);
const db = getFirestore(app);


// Get data for patient follow-up details
// Function to format the current date as yyyy-mm-dd
function getCurrentDate() {
    var currentDate = new Date();
    return currentDate.getFullYear() + '-' + (currentDate.getMonth() + 1) + '-' + currentDate.getDate();
}



$(document).ready(() => {

    

    $('#search').submit((e) => {
        e.preventDefault();
        console.log("SEARCHING", $('#patient-id').val());
        const docRef = doc(db, "patients", $('#patient-id').val());
        let tableBody = document.getElementById('patientTableBody');
        tableBody.innerHTML = '';
        getDoc(docRef).then((docSnap) => {
            if(docSnap.exists()){
                const pdat = docSnap.data();
                let row = document.createElement('tr');
                row.innerHTML = `
                <td>${docSnap.id}</td>
                <td>${pdat.FollowupDone_Count}</td>
                <td>${getCurrentDate()}</td>
                <td>${pdat.Age}</td>
                <td><a href="/followup-details/${docSnap.id}">Patient Details</a></td>
            `;
            tableBody.appendChild(row);
            }
        });
        // const q = query(collection(db, 'patient-data'))
        // getDocs(q).then((querySnapshot) => {
        //     // Populate the table with patient data
            // var tableBody = document.getElementById('patientTableBody');
        //     querySnapshot.forEach(function(patient) {
        //     var row = document.createElement('tr');
        //     const pdat = patient.data();
        //     row.innerHTML = `
        //         <td>${patient.id}</td>
        //         <td>${pdat.FollowupDone_Count}</td>
        //         <td>${getCurrentDate()}</td>
        //         <td>${pdat.Age}</td>
        //         <td><a href="#">Patient Details</a></td>
        //     `;
        //     tableBody.appendChild(row);
        // });


        
    });
    
    });






