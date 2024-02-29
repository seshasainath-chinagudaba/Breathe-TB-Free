
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-analytics.js";

import { getFirestore } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
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

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
console.log(app);

// // const provider = new GoogleAuthProvider();
const auth = getAuth();
const db = getFirestore(app);
// console.log("I am here");






// $('a').on('click', function (event) {
//     event.preventDefault();
//     var page = this.hash.substring(1);
//     $(".content").hide();
//     $("#" + page).fadeIn(1000);
// });

var idleTime = 0;
var idleInterval = setInterval(timerIncrement, 60000); // 1 minute

$(this).mousemove(function (e) {
    idleTime = 0;
});

function timerIncrement() {
    idleTime = idleTime + 1;
    if (idleTime > 4) { // 5 minutes

        signOut(auth).then(() => {
            // Sign-out successful.
            // logout('inactivity');
            $('a[href="#login"]').text('Login');
            removePredictLink();
            location.reload();

        }).catch((error) => {
            // An error happened.
            console.log("Error logging out")
        });
    }
}



// Function to append the "Predict" link
function appendPredictLink() {
    console.log('Appending Predict Link');
    $('.navbar-nav.ml-auto').append('<a class="nav-item nav-link" href="/predict">Predict</a>');
}

// Function to remove the "Predict" link
function removePredictLink() {
    console.log('Removing Predict Link');
    $('.navbar-nav.ml-auto a[href="/predict"]').remove();
}


$('a').on('click', function (event) {
    event.preventDefault();
    var page = this.hash.substring(1);
    $(".content").hide();
    $("#" + page).fadeIn(1000);

    // Update the "Predict" link after navigating to a new section
    // updatePredictLink();
});

function logout(reason) {
    // sessionStorage.removeItem('loggedIn'); // Clear the login state
    $('a[href="#login"]').text('Login');
    removePredictLink();
    location.reload();

    if (reason === 'inactivity') {
        alert('You have been logged out due to inactivity.');
    } else if (reason === 'manual') {
        alert('You have been manually logged out.');
    }

    // updatePredictLink();
}
function login2(formidx) {
    var email = $(`#username-${formidx}`).val();
    var password = $(`#password-${formidx}`).val();

    signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;
            console.log("Sairam signed in");

            // ...
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            console.log(errorMessage);
            alert("Invalid credentials");
        });
}
$('#login-form-2').on('submit', function (e) {
    e.preventDefault();
    console.log("Sairam")
    login2(2);
});



/// trails///
// Function to handle signup
function signup() {
    var email = $('#username').val();
    var password = $('#password').val();

    var role = $('#role').val();
    createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed up 
            const user = userCredential.user

            console.log(user);
            alert('Signed up successfully. Pending email verification.');
            return signOut(auth);
            // ...
        }).then(() => {
            alert("Please login again after verification");
            location.reload();
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage);
            // ..
        });


}

// Attach a submit event listener to the signup form
$('#signup-form').on('submit', function (e) {
    e.preventDefault();
    signup();
});







function redirectToURL(url) {
    window.location.href = url;
}
$(document).ready(function () {
    // Check sessionStorage for login state on page load


    $('a[href="#login"]').on('click', function (e) {
        if ($(this).text() === 'Logout') {
            e.preventDefault();
            signOut(auth).then(() => {
                // Sign-out successful.
                // logout('inactivity');
                $('a[href="#login"]').text('Login');
                removePredictLink();
                location.reload();

            }).catch((error) => {
                // An error happened.
                console.log("Error logging out")
            });
        }
    });



});