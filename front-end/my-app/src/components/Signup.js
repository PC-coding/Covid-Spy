import React from 'react';
import { Link } from 'react-router-dom';


export default function Signup() {
    return(
        <div className='signup'>
            <h1>Sign Up!</h1>
            {/* <p>Enter your desired Username:</p> */}
            <input type='text' name='username' id='user' placeholder='Desired username'></input>
            <br></br>
            {/* <p>Enter your desired Password:</p> */}
            <input type='password' name='password' id='pass' placeholder='Desired password'></input>
            <br></br>
            {/* <p>Confirm your Password:</p> */}
            <input type='password' name='password' id='pass' placeholder='Confirm password'></input>
            <br></br>
            {/* <p>Email:</p> */}
            <input type='text' name='email' id='email' placeholder='Enter your email'></input>
            <br></br>
            <Link to="/login">Existing user? Login here!</Link>
            <br></br>
            <button>Complete</button>
            <br></br>
        </div>
    )
}