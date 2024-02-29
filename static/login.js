import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
// import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

import { getFirestore, addDoc, setDoc, doc, collection } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getAuth, getRedirectResult, onAuthStateChanged, sendEmailVerification, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut } from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js';        // TODO: Add SDKs for Firebase products that you want to use
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
// const db = getFirestore(app);


$(document).ready(() => {
    function login() {
        let email = $('#emailAddress').val();
        let password = $('#password').val();
    
        signInWithEmailAndPassword(auth, email, password)
            .then((userCredential) => {
                // Signed in 
                const user = userCredential.user;
                console.log("Sairam signed in");
                window.location = '/';
                // ...
            })
            .catch((error) => {
                const errorCode = error.code;
                const errorMessage = error.message;
                console.log(errorMessage);
                alert("Invalid credentials");
            });
    }
    $('#login-form').on('submit', function (e) {
        e.preventDefault();
        console.log("Sairam")
        login();
    });
});