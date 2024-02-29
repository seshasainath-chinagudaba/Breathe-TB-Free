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
const db = getFirestore(app);

function logOut() {
    signOut(auth).then(() => {
        alert("Logged out successfully");
        location.href = '/';
    }).catch((error) => {
        // An error happened.
        alert("Error logging out");
    });

}
$(document).ready(() => {

    function appendPredictLink() {
        console.log('Appending Predict Link');
        $('.navbar-nav.ml-auto').append('<a id="predict-link" class="nav-item nav-link" href="/predict">Predict</a>');
    }
    function appendLogoutLink() {
        console.log('Appending Logout Link');
        $('.navbar-nav.ml-auto').append('<a id="logout-link" class="nav-item nav-link" href="/logout">Logout</a>');
    }
    function appendLoginLink() {
        console.log('Appending Login Link');
        $('.navbar-nav.ml-auto').append('<a id="login-link" class="nav-item nav-link" href="/login">Login</a>');
    }
    function appendSignupLink() {
        console.log('Appending Signup Link');
        $('.navbar-nav.ml-auto').append('<a id="signup-link" class="nav-item nav-link" href="/signup">Signup</a>');
    }

    function appendPatientDataLink() {
        console.log('Appending PData Link');
        $('.navbar-nav.ml-auto').append('<a id="patientdata-link" class="nav-item nav-link" href="/pdata">Patient Data</a>');
    }

    let logoutTimeout;

    function setLogoutTimeout() {
        // Clear any existing timeout
        clearTimeout(logoutTimeout);
        // Set new timeout for logout after 10 minutes (600,000 milliseconds) of inactivity
        logoutTimeout = setTimeout(() => {
            logOut().then(() => {
                alert("Logged out successfully due to inactivity ");
                location.href = '/';
            }); // Call the logout function
        }, 6000); // 5 minutes in milliseconds
    }

    // Function to clear the logout timeout
    function clearLogoutTimeout() {
        clearTimeout(logoutTimeout);
    }


    function removeLoginLink() {
        console.log('Removing Login Link');
        $('.navbar-nav.ml-auto #login-link').remove();
    }
    function removeSignupLink() {
        console.log('Removing Signup Link');
        $('.navbar-nav.ml-auto #signup-link').remove();
    }
    function removeLogoutLink() {
        console.log('Removing Logout Link');
        $('.navbar-nav.ml-auto #logout-link').remove();
    }
    // Function to remove the "Predict" link
    function removePredictLink() {
        console.log('Removing Predict Link');
        $('.navbar-nav.ml-auto #predict-link').remove();
    }

    function removePatientDataLink() {
        console.log('Removing PatientData Link');
        $('.navbar-nav.ml-auto #patientdata-link').remove();
    }


    console.log("Sairamlogoutlink", $('#logout-link'));

    // Handle unverified emails
    onAuthStateChanged(auth, (user) => {
        if (user) {
            setLogoutTimeout();
            // User is signed in, see docs for a list of available properties
            // https://firebase.google.com/docs/reference/js/auth.user
            const uid = user.uid;
            console.log(user);
            if (!user.emailVerified) {
                window.location.replace('/verify');
            } else {
                console.log("Logging in");
                // remove existing links
                removePredictLink();
                // append predict link
                appendPredictLink();
                // remove Login link
                removeLoginLink();
                // remove Signup link
                removeSignupLink();
                // remove existing logout links
                removeLogoutLink();
                // append logout link
                appendLogoutLink();

                let docRef = doc(db, 'Users', uid);
                getDoc(docRef).then((docSnap) => {
                    if (docSnap.exists()) {

                        let userInfo = docSnap.data();
                        console.log(userInfo);
                        // if(userInfo.firstTime == true){
                        //     sendPasswordResetEmail(auth, user.email).then(() => {
                        //         alert("Please reset your password for more security");
                        //     });
                        // }
                        if (userInfo.role === "doctor") {
                            removePatientDataLink();
                            appendPatientDataLink();
                        }
                    }
                });


            }


        } else {
            // User is signed out
            // ...
            console.log("SAIRAM logged out");
            if (window.location.pathname !== "/") {
                window.location.replace('/');
            }
            clearLogoutTimeout();

            removePredictLink();
            removePatientDataLink();
            removeLogoutLink();
            // remove any existing login links
            removeLoginLink();
            appendLoginLink();

            // remove any existing signup links
            removeSignupLink();
            appendSignupLink();
            // window.location.replace('/');
            console.log(window.location.pathname);

        }
    });
});

export default logOut;
// Function to append the "Predict" link