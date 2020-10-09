import React, { useState } from 'react';
import '../App.css';
import NavBar from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/components/Navbar.js';
import Router from './Router';
import { BrowserRouter, Route } from 'react-router-dom';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  // const loggedIn = true;

  return (
    <BrowserRouter className="App">
      <header className="App-header">
        <NavBar loggedIn={loggedIn} />
        <Router loggedIn={loggedIn} />
      </header>
    </BrowserRouter>
  );
}

export default App;
