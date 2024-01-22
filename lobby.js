
const username = localStorage.getItem('username');
const selected_mode = localStorage.getItem('PVPmode');
const lobbyRef = '';
document.getElementById('chosen_mode').innerText=selected_mode;
const firebaseConfig = {
  apiKey: "AIzaSyD-BBshNUbgt-c1qiSyVqcMLGhf0iz864g",
  authDomain: "baseball-37e0d.firebaseapp.com",
  projectId: "baseball-37e0d",
  storageBucket: "baseball-37e0d.appspot.com",
  messagingSenderId: "422995163027",
  appId: "1:422995163027:web:4b49ffa090ca952ad55a66",
  measurementId: "G-792QSK4ZY7"        
  };
  
  const app = firebase.initializeApp(firebaseConfig);
  const database = firebase.database();   
  document.addEventListener("DOMContentLoaded", function() {
    if (localStorage.getItem('username') !== null) {      
      const usersRef = database.ref('users/' + username);      
      usersRef.once('value', (snapshot) => {
        if (snapshot.exists()) {
          const userData = snapshot.val();                    
          document.getElementById("profile").src = userData["Profile pic"];
        }
      });
    }
if(selected_mode == '1v1')
  {
    lobbyRef = database.ref('lobby/1v1');
    registerForMatchmaking(username);    
  }
  if(selected_mode == '2v2')
  {
    lobbyRef = database.ref('lobby/2v2');    
  }
  if(selected_mode == '3v3')
  {
    lobbyRef = database.ref('lobby/3v3');    
  }
  if(selected_mode == '4v4')
  {
    lobbyRef = database.ref('lobby/4v4');    
  }
  if(selected_mode == 'custom')
  {
    lobbyRef = database.ref('lobby/custom');    
  }

  });
  
function exit()
{
  window.location.href="{{ url_for('main') }}";
}


function myLoop(){
  const timestamp = Date.now();
  lobbyRef.child(playerName).set(timestamp);
  removePlayers();
}
const intervalId = setInterval(myLoop, 2500);

const timeout = 5000;

function removePlayers(){
  lobbyRef.on('value', (snapshot) => {
    snapshot.forEach((childSnapshot) => {
      const playerName = childSnapshot.key;
      const timestamp = childSnapshot.val();
      const currentTime = Date.now();
      const elapsedTime = currentTime - timestamp;
      if (elapsedTime > timeout) {        
        lobbyRef.child(playerName).remove();        
      }
    });
  });
}
const match_maker= false;
function registerForMatchmaking(playerId) {
  lobbyRef.once('value').then((snapshot) => {
    const lobbyData = snapshot.val();

    if (!lobbyData.matchmaker) {
      // If no matchmaker, make the current player the matchmaker
      lobbyRef.update({ matchmaker: playerId });
      console.log(`Player ${playerId} is the matchmaker.`);
      match_maker=true;
      tryMatchmaking(playerId);
    } else {
      // Otherwise, register the player for matchmaking
      lobbyRef.child('matchmakingQueue').push(playerId);
      console.log(`Player ${playerId} registered for matchmaking.`);  
      match_maker=false;    
    }
  });
}

// Function to try matchmaking
function tryMatchmaking(matchmakerId) {
  lobbyRef.child('matchmakingQueue').once('value').then((snapshot) => {
    const matchmakingQueue = snapshot.val();

    // Check if there are enough players for matchmaking
    if (matchmakingQueue && Object.keys(matchmakingQueue).length >= 1) {
      const player = Object.keys(matchmakingQueue)[0];

      console.log(`Match found! Players ${matchmakerId} and ${player} are matched.`);

      const matchNotification = { opponent: player };
      lobbyRef.child(matchmakerId).child('matchFound').set(matchNotification);
      lobbyRef.child(player).child('matchFound').set(matchNotification);

      // Clean up the matchmaking queue
      lobbyRef.child('matchmakingQueue').remove();
    } else {
      console.log('Not enough players for matchmaking.');
    }
  });
}

lobbyRef.on('value', function(snapshot) {
  if (match_maker) {
    tryMatchmaking(username);
  } else if (!lobbyData.matchmaker) {
    // If no matchmaker, make the current player the matchmaker
    lobbyRef.child('matchmakingQueue').once('value').then((snapshot) => {
      const players = snapshot.val();
      const player = Object.keys(players)[0];
      lobbyRef.update({ matchmaker: playerId });
    });    
    console.log(`Player ${playerId} is the matchmaker.`);
    match_maker=false;
    tryMatchmaking(playerId);
  }
});
    

lobbyRef.ref(`/${playerId}/matchFound`).on('value', (snapshot) => {
  const matchInfo = snapshot.val();
  if (matchInfo) {
    console.log(`Match found! Opponent: ${matchInfo.opponent}`);
    // Handle the match details, start the game, etc.
  }
});

// Clean up when the player disconnects
window.addEventListener('beforeunload', () => {
  const lobbyRef = database.ref(`/lobby`);
  lobbyRef.child('matchmaker').remove();
  lobbyRef.child('matchmakingQueue').remove();
  lobbyRef.child(`${playerId}`).remove();
});

function playSoundEffect() {
  var audio = new Audio('../static/select.wav');
  audio.play();
}

document.body.addEventListener('click', function (event) {        
  playSoundEffect();            
});