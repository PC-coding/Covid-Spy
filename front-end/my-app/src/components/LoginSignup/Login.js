import React, { useState } from "react";
import { Link } from 'react-router-dom';
import img from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/components/images/userLogin.svg';

export default function Login( { token, setToken } ) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const sendLogin = async () => {
    const userData = JSON.stringify({"username": username, "password": password});
    

    const configs = {
      method: 'POST',
      headers: { "Content-Type": "application/json"},
      body: userData
    };
    const response = await fetch('http://localhost:5000/covid/login', configs);
    const data = await response.json();
    console.log(data);
    sessionStorage.setItem('token', data.session_id)
    setToken(data.session_id);
    }

    return (
        <div className='login'>
          <br></br>
          <h1>Login</h1>
          <img style={{height:'250px', width: '3000px'}} src={img} />
          <br></br>
          <input onChange={e => setUsername(e.target.value)} type="text" placeholder="Username" /><br/>
          <input onChange={e => setPassword(e.target.value)} type="password" placeholder="Password" /><br/>
          <Link style={{color:'white', textDecoration:'none'}} to="/signup">New user? Create an account here!</Link>
          <br></br>
          <button style={{color:'white', backgroundColor:'black', fontWeight:'bold', blockSize: 35}} onClick={sendLogin}>Login</button><br/>
        </div>
        )
    }