import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

import { getFirestore, doc, getDoc } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getAuth, getRedirectResult, onAuthStateChanged, sendEmailVerification, sendPasswordResetEmail, signInWithEmailAndPassword, createUserWithEmailAndPassword, signOut } from 'https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js';        // TODO: Add SDKs for Firebase products that you want to use

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
  
  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
  console.log("Auth module", app);
  
  // // const provider = new GoogleAuthProvider();
  const auth = getAuth(app);



  $(document).ready(() => {
        $('#password_reset').submit((e) => {
            e.preventDefault();
            sendPasswordResetEmail(auth, $('#emailAddress').val() ).then(() => {
                alert("Sent password reset mail to your registered email address");
            }).catch(err => {
                alert("Unsuccessful", err);
            })
        });
  });