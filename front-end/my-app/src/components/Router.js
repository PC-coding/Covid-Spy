import React from 'react';
import { Route } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
// import Map from './Map';
// import Graph from './Graph';

const Router = ({ loggedIn }) => {
    if (loggedIn) {
        return(
            <div>
                <Route path='/' />
                <Route path='/' />
            </div>
        )
    } else {
        return(
            <div>
                <Route path='/login'> 
                    <Login loggedIn={loggedIn}/>
                </Route>
                <Route path='/signup'>
                    <Signup loggedIn={loggedIn}/>
                </Route>
            </div>
        )
    }
}
export default Router;