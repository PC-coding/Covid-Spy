import React from 'react';
import { useState, useEffect } from 'react';

export default function User( { token, username, favorites } ){
    const [userInfo, setUserInfo] = useState([]);

    useEffect(() => {
        const getUserInfo = async() => {
            const userToken = JSON.stringify({'token': token})
            const configs = {
                methods: 'POST',
                headers: { "Content-Type": "application/json"},
                body: userToken
            };
            const response = await fetch('http://localhost:5000/covid/getUserInfo');
            const data = await response.json();
            setUserInfo(data.userInfo);
        }
        getUserInfo();
     }, [])

    return(
        <div>
            <br></br>
            <h3> Welcome back, {username} </h3>
            <h4> Here are your favorites:</h4>
            <p>{favorites}</p>
        </div>
    )
}