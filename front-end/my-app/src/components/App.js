import React, { useState } from 'react';
import '../App.css';
import NavBar from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/components/Navbar.js';
import Router from './Router';
import { BrowserRouter, Route } from 'react-router-dom';
import Space from './video/Space.mp4';

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  // const [loggedIn, setLoggedIn] = useState(true);

  return (
  <BrowserRouter className="App">
        <video className='vid'autoPlay loop muted>
          <source src={Space} type='video/mp4'/>
        </video>
        <header className="App-header">
          <NavBar loggedIn={loggedIn} />
          <Router loggedIn={loggedIn} />
        </header>
    </BrowserRouter>
  );
}
export default App;
