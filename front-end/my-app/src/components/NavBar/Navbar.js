import React from 'react';
import { Link } from 'react-router-dom';
import img from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/covid19_cell.png';

const NavBar = ({ loggedIn }) => {
    if (loggedIn) {
        return(
            <nav>
                <Link to='/'> 
                    <img src={img} className='top-nav-icon' alt='icon' />
                </Link>
                <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/tracker'>Map-Tracker</Link>
                <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/graphs'>Graphs</Link>
            </nav>
        )
    } else {
        return(
            <nav>
                <Link to='/'> 
                    <img src={img} className='top-nav-icon' alt='icon' />
                </Link>
                <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/login'>Login</Link>
                <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/signup'>Signup</Link>
                {/* <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/tracker'>Map-Tracker</Link> */}
            </nav>
        )
    }
}
export default NavBar;