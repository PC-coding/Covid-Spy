import React, { useState } from "react";
import { Link } from 'react-router-dom';

export default function Login() {
  const [username, setUsername] = useState("Hello");
  const [password, setPassword] = useState("Hello");

  const sendLogin = async () => {
    const userData = JSON.stringify({"username": username, "password": password});
  }

//   const configs = {
//     method: 'POST',
//     headers: { "Content-Type": "application/json"},
//     body: userData
//   };
//   const response = await fetch('http://localhost:5000/api/login', configs);
//   const data = await response.json();
//   console.log(data);
//   setToken(data.session_id);
//   }

    return (
        <div className='login'>
            <h1>Login</h1>
            <input onChange={e => setUsername(e.target.value)} type="text" placeholder="Username" /><br/>
            <input onChange={e => setPassword(e.target.value)} type="password" placeholder="Password" /><br/>
            <button onClick={sendLogin}>Login</button><br/>
            <Link to="/signup">New user? Create an account here!</Link>
        </div>
        )
    }