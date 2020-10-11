import React from 'react';
import { Route } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
// import Map from './Map';
// import Graph from './Graph';
import Globe from './Globe';

const Router = ({ loggedIn }) => {
    if (loggedIn) {
        return(
            <div>
                <Route path='/worldmap' />
                <Route path='/graphs' />
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
                {/* <Route path='/globes'>
                    <Globe />
                </Route> */}
            </div>
        )
    }
}
export default Router;