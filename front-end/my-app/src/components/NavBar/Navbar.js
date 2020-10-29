import React from 'react';
import { Link, Redirect } from 'react-router-dom';
import img from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/covid19_cell.png';
import logo from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/components/images/Covid-spy-logo.png';

const NavBar = ({ token, setToken }) => {
    function logOut(){
        sessionStorage.setItem('token', '');
        setToken('');
    }
    if (token) {
        return(
            <nav className='navStyle'>
                <div>
                    <Link to='/'>
                        <img src={logo} className='logo' />
                    </Link>
                    {/* <Link to='/'> 
                        <img src={img} className='top-nav-icon' alt='icon' />
                    </Link> */}
                </div>
                <div>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/tracker'>Map</Link>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/graphs'>Graph</Link>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/user'>Account</Link>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/login' onClick={logOut} >Logout</Link>
                </div>
                <Redirect from='/' to='/user' />
            </nav>
        )
    } else {
        return(
            <nav className='navStyle1'>
                <div>
                    <Link to='/'>
                        <img src={logo} className='logo' />
                    </Link>
                    {/* <Link to='/'> 
                        <img src={img} className='top-nav-icon' alt='icon' />
                    </Link> */}
                </div>
                <div className="justify-content-end nav" justify="true">
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/about'>About</Link>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/login'>Login</Link>
                    <Link style={{color:'white', fontWeight:'bold', textDecoration:'none', padding:20}} to='/signup'>Signup</Link>
                </div>
            </nav>
        )
    }
}
export default NavBar;