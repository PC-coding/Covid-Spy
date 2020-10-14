import React from 'react';
import { Route } from 'react-router-dom';
import Login from './Login';
import Signup from './Signup';
import Map from './worldMap';
import Graph from './Graphs';
// import Globe from './Globe';

const Router = ({ loggedIn }) => {
    if (loggedIn) {
        return(
            <div>
                <Route path='/worldmap'>
                    <Map loggedIn={loggedIn}/>
                </Route>
                <Route path='/graphs'>
                    <Graph loggedIn={loggedIn}/>
                </Route>
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
                    <Globe loggedIn={loggedIn} />
                </Route> */}
            </div>
        )
    }
}
export default Router;