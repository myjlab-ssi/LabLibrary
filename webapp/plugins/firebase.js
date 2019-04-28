import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp({
    apiKey: 'AIzaSyB_AY0r94cRpTLnM3bQsDXWlEbkws_y5Cg',
    authDomain: 'labooks-9cc02.firebaseapp.com',
    databaseURL: 'https://labooks-9cc02.firebaseio.com',
    projectId: 'labooks-9cc02',
    storageBucket: 'labooks-9cc02.appspot.com',
    messagingSenderId: '150152982483'
  })
}

export default firebase
