import React from 'react';

export default function User( { token, username } ){
    return(
        <div>
            <br></br>
            <h3> Welcome back, {username} </h3>
            <p> Here are your favorites:</p>
        </div>
    )
}