import React from 'react';
import { useState, useEffect } from 'react';

export default function User( { token, username, userFav, setUserFav } ){
    // const [userFav, setUserFav] = useState([]);

    const [userInfo, setUserInfo] = useState([]);
    
    const saveFavorites = async () => {
        const userData = JSON.stringify({"favorites": userFav})
        const configs = {
            methods: 'POST',
            headers: {"Content-Type": "application/json"},
            body: userData
        };
        const response = await fetch('http://localhost:5000/covid/countries/filter');
        const data = await response.json();
        setUserInfo(data.Favorites);
    }

    return(
        <div>
            <br></br>
            <h3> Welcome back, {sessionStorage.getItem('username')} </h3>
            <h4> Here are your favorites:</h4>
            <p>{setUserFav}</p>
        </div>
    )
}