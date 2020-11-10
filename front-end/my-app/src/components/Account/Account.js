import React from 'react';
import { useState, useEffect } from 'react';

export default function User( { token, username, userFav, setUserFav } ){
    // const [userFav, setUserFav] = useState([]);

    const [userInfo, setUserInfo] = useState([]);
    
    const saveFavorites = async () => {
        const userData = JSON.stringify({"favorites": userFav, "api_key": token})
        const configs = {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: userData
        };
        console.log(token);
        const response = await fetch('http://localhost:5000/covid/countries/filter', configs);
        const data = await response.json();
        setUserInfo(data.favorites);
    }
    // saveFavorites();
    

    return(
        <div>
            <br></br>
            <h3> Welcome back, {sessionStorage.getItem('username')} </h3>
            <h4> Here are your favorites:</h4>
            <br></br>
            <br></br>
            <h1> Coming Soon ...</h1>
            <br></br>
            <p>{setUserFav}</p>
            <p>{userFav}</p>
        </div>
    )
}