import React from 'react';
import { Route } from 'react-router-dom';
import Login from '../LoginSignup/Login';
import Signup from '../LoginSignup/Signup';
import Graph from '../Graphs/Graphs';
import Globe from '../Globe(Home)/Globe';
import Tracker from '../Tracker/Tracker';
import User from '../AboutMe/About';

const Router = ({ token, setToken}) => {
    if (token) {
        return(
            <div>
                <Route path='/' exact component={Globe} />
                <Route path='/tracker'>
                    <Tracker token={token} setToken={setToken}/>
                </Route>
                <Route path='/graphs'>
                    <Graph token={token} setToken={setToken}/>
                </Route>
                <Route path ='/user'>
                    <User token={token} setToken={setToken} />
                </Route>
            </div>
        )
    } else {
        return(
            <div>
                <Route path='/login'> 
                    <Login token={token} setToken={setToken}/>
                </Route>
                <Route path='/signup'>
                    <Signup token={token} setToken={setToken}/>
                </Route>
                <Route path='/' exact component={Globe}/>
                <Route path='/tracker'>
                    <Tracker />
                </Route>
            </div>
        )
    }
}

export default Router;