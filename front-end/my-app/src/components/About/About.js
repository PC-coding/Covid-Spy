import React from 'react';
import './About.css';

export default function About(){
    return(
        <div className='paragraph'>
            <h3>Background Info:</h3>
            <p>
            We’re obviously living in times of a pandemic caused by the virus 
            Covid-19. The problem I’m trying to address is people being able 
            to easily access and track data on positive cases near their area. 
            I do believe there are Coronavirus tracker apps built already but 
            they don’t seem as user friendly or easy to understand as my idea. 
            </p>
            <p>
            Anybody who is concerned about positive cases near them can use my 
            app, a lot of people are still scared of the virus and have been 
            staying indoors due to this dilemma. Hopefully with something 
            interactive and beginner friendly like my app, people can find 
            information easier to digest. 
            </p>

            <h3>Data</h3>
            <p>
            Data was obtained through a free open-source API that is regularly 
            updated. The data provides continent, country, U.S states, and U.S 
            county information.
             
            https://github.com/disease-sh 
            </p>
        </div>
    )
}