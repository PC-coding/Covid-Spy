import React from 'react';
import './About.css';

export default function About(){
    return(
        <div className='paragraph'>
            <br></br>
            <h3>Project Goal:</h3>
            <p>
                We’re obviously living in times of a pandemic caused by the virus 
                Covid-19. The problem I’m trying to address is people being able 
                to easily access and track data on positive cases near their area. 
            </p>
            <p>
                Anybody who is concerned about positive cases near them can use my 
                app, a lot of people are still scared of the virus and have been 
                staying indoors due to this dilemma. Hopefully with something 
                interactive, engaging and beginner friendly like my app, people can find 
                information easier to digest. 
            </p>
            <p>
                IN THE FUTURE:
                I will be implementing a functionality for States, Provinces, and counties
                to be viewed on the map and have graphical formatting for each option.
            </p>
            <br></br>
            <h3>Data</h3>
            <p>
            Data was obtained through a free open-source API that is regularly 
            updated. The data provides continent, country, U.S states, and U.S 
            county information.

            https://disease.sh/docs
            https://github.com/disease-sh 
            </p>
        </div>
    )
}