import React, { useState } from 'react';
import '../App.css';
import NavBar from './NavBar/Navbar.js';
import Router from './NavBar/Router';
import { BrowserRouter } from 'react-router-dom';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [token, setToken] = useState("");
  // const [loggedIn, setLoggedIn] = useState(true);

  return (
  <BrowserRouter>
        <div className="app"> 
          <header className="App-header">
            <NavBar token={token} setToken={setToken} />
            <Router token={token} setToken={setToken}/>
          </header>
        </div>
    </BrowserRouter>
  );
}

export default App;

