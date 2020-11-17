import React from 'react';
import { useState, useEffect } from 'react';
import Table from '../Table/Table.js';
import { sortData } from '../util.js'
import numeral from 'numeral';



export default function User( { token, username, userFav, setUserFav } ){
    // const [userFav, setUserFav] = useState([]);

    const [userInfo, setUserInfo] = useState([]);
    const [countries, setCountries] = useState([]);
    const [tableData, setTableData] = useState([]);
    const [mapCountries, setMapCountries] = useState([]);

    useEffect(() => {
        const getCountriesData = async () => {
            await fetch("http://localhost:5000/covid/countries/favorites")
            // await fetch("https://disease.sh/v3/covid-19/countries")

            .then(response => response.json())
            .then(data => {
            const countries = data.map(country => ({
                country: country.country,
                active: country.active
                // value: country.iso2
            }));
    
            const sortedData = sortData(data);
            setTableData(sortedData);
            setMapCountries(data);
            setCountries(countries);
            })
        }
        getCountriesData();
        }, [])
    


    const saveFavorites = async () => {
        const userData = JSON.stringify({"favorites": userFav, "api_key": token})
        const configs = {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: userData
        };
        console.log(token);
        const response = await fetch('http://localhost:5000/covid/countries/filter', configs);
        const data = await response.json();
        // setUserInfo(data.favorites);
        console.log(data);
        setUserFav(data.Favorites);
    };    

      

    return(
        <div>
            <br></br>
            <h3> Welcome back, {sessionStorage.getItem('username')} </h3>
            <h4> Here are your favorites:</h4>
            <br></br>
            
            <div style={{'white-space': 'pre-line'}}>
                {userFav.join('\n')}
            </div>


            {/* {userFav.map(({ country, active }) => (
                <tr>
                    <td>
                        <div className='flaginfo'>
                            <img src={flag} style={{height:'26px', 
                            width:'38px'}} />
                        </div>
                    </td>
                    <td>{country}</td>
                    <td><strong>{numeral(active).format("0,0")}</strong></td>
                </tr>
            ))} */}


            <button onClick={saveFavorites} style={{backgroundColor:'black', color: 'white', fontWeight:'bold'}}>
                Click me to get your favorites!</button>     

            {/* <Table countries={tableData}/> */}
        </div>
    )
}