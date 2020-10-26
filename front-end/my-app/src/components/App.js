import React, { useState } from 'react';
import '../App.css';
import NavBar from './NavBar/Navbar.js';
import Router from './NavBar/Router';
import { BrowserRouter } from 'react-router-dom';

const useStateWithSessionStorage = (token, defaultValue) => {
  const [value, setValue] = useState(sessionStorage.getItem(token) || defaultValue);
  return [value, setValue];
}

function App() {
  const [token, setToken] = useStateWithSessionStorage('token', '');

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

