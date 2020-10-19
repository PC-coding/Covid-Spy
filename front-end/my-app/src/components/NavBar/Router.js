import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Login from '../LoginSignup/Login';
import Signup from '../LoginSignup/Signup';
import Map from '../Map/worldMap';
import Graph from '../Graphs/Graphs';
import Globe from '../Globe(Home)/Globe';
import Tracker from '../Tracker/Tracker';
import { TransitionGroup, CSSTransition } from "react-transition-group";
import styled from "styled-components";

const Router = ({ loggedIn, location }) => {
    if (loggedIn) {
        return(
            <div>
                <Route path='/' exact component={Globe} />
                <Route path='/tracker'>
                    <Tracker />
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
                <Route path='/' exact component={Globe} />
                <Route path='/tracker'>
                    <Tracker />
                </Route>
            </div>
        )
    }
}

export default Router;