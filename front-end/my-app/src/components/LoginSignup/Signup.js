import React, { useState } from 'react';
import { Link } from 'react-router-dom';


export default function Signup( { token, setToken } ) {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');

    const sendSignup = async () => {
        const userData = JSON.stringify({"username": username, "password": password, "email": email});
        
    
        const configs = {
          method: 'POST',
          headers: { "Content-Type": "application/json"},
          body: userData
        };
        const response = await fetch('http://localhost:5000/covid/create', configs);
        const data = await response.json();
        console.log(data);
        setToken(data.session_id);
        }

    return(
        <div className='signup'>
            <br></br>
            <h1>Sign Up!</h1>
            <br></br>
            <input onChange={e => setUsername(e.target.value)} type='text' name='username' id='user' placeholder='Desired username'></input>
            <br></br>
            <input onChange={e => setPassword(e.target.value)}  type='password' name='password' id='pass' placeholder='Desired password'></input>
            <br></br>
            {/* <input type='password' name='password' id='pass' placeholder='Confirm password'></input>
            <br></br>  */}
            <input onChange={e => setEmail(e.target.value)} type='text' name='email' id='email' placeholder='Enter your email'></input>
            <br></br>
            <Link style={{color:'white', textDecoration:'none'}} to="/login">Existing user? Login here!</Link>
            <br></br>
            <button style={{color:'white', backgroundColor:'black', fontWeight:'bold', blockSize: 35}} onClick={sendSignup}>Complete</button>
            <br></br>
        </div>
    )
}