import React from 'react';
import './About.css';
import img from '/Users/tappy/Byte/Phase_3_Project/front-end/my-app/src/components/images/Covid-spy-logo.png';

export default function About(){
    return(
        <div className='aboutapp'>
            <div className='about-logo'>
                <img src={img} />
            </div>
            <div className='paragraph'>
                <br></br>
                <h3>What is Covid-Spy?:</h3>
                <p>
                    We're living in times of a pandemic caused by the virus Covid-19.
                    This application was created to provide accessible and 
                    trackable data in a more engaging and easily digestable way. My 
                    goal is to keep working and updating functionalities on this application. 
                </p>
                <p>
                    IN THE FUTURE:
                    I will be implementing a functionality for  provinces and counties around 
                    the world to be viewed on the map and have graphical formatting for each 
                    option.
                    I'm currently working on the United States' states feature, currently around
                    50% done with that. 
                </p>
                <br></br>
                <h3>Data</h3>
                <p>
                    Data was obtained through a free open-source API that is regularly 
                    updated. The data provides continent, country, U.S states, and U.S 
                    county information.
                </p>
                <a href="https://disease.sh" style={{color:'white'}}>Visit the API's documentation</a>
                <a href="https://github.com/disease-sh" style={{color:'white'}}>Visit the API's github</a>
                <br></br>
                <h3>Technologies used:</h3>
                <p>
                    For the frontend: ReactJS, CSS, Material UI
                </p>
                <p>
                    For the backend: Python-Flask
                </p>
                <p>
                    Libraries: React Leaflet for the map component and React Charts 2 was
                    used for the graph component. 
                </p>
                <br></br>
            </div>
        </div>
    )
}