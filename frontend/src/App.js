import React, { useEffect } from 'react';
import keycloak from './components/keycloak';

function App() {
  useEffect(() => {
    keycloak.init({ onLoad: 'login-required' }).then((authenticated) => {
      if (authenticated) {
        console.log('User is authenticated');
      }
    });
  }, []);

  return (
    <div className="App">

        <h4>The Digital Quality App</h4>
      <h1>Keycloak React App</h1>
      <p>Welcome to the app!</p>
    </div>
  );
}

export default App;
