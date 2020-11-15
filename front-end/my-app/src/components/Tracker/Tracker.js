import React, { useState, useEffect } from 'react';
import { MenuItem, FormControl, Select } from "@material-ui/core";
import './Tracker.css';
import InfoBox from '../InfoBox/InfoBox.js';
import Map from '../Map/map.js';
import { sortData, prettyPrintStat } from '../util.js';
import "leaflet/dist/leaflet.css";


function Tracker( { userFav: userFav, setUserFav: setUserFav }) {
    // countries state
  const [countries, setCountries] = useState([]);
  const [country, setCountry] = useState('worldwide');
  const [countryInfo, setCountryInfo] = useState({});
  const [tableData, setTableData] = useState([]);
  const [mapCenter, setMapCenter] = useState({
                                                lat: 34.80746,
                                                lng: -40.4796
                                            });
  const [mapZoom, setMapZoom] = useState(3);
  const [mapCountries, setMapCountries] = useState([]);
  const [casesType, setCasesType] = useState("cases");


    // U.S states state
  // const [states, setStates] = useState([]);
  // const [state, setState] = useState('states');
  // const [stateInfo, setStateInfo] = useState({});
  // const [mapStateCenter, setMapStateCenter] = useState({
  //                                                       lat: 40.1345916,
  //                                                       lng: -102.0903563
  //                                                       });
  // const [mapStateZoom, setMapStateZoom] = useState(4);
  // const [mapStates, setMapStates] = useState([]);

// working 
  useEffect(() => {
    fetch('https://disease.sh/v3/covid-19/all')
    .then(resp => resp.json())
    .then(data => {
      setCountryInfo(data);
    })
  }, [])
  
  // useEffect(() => {
  //   const getCountriesData = async () => {
  //     await fetch("https://disease.sh/v3/covid-19/countries")
  //     .then(response => response.json())
  //     .then(data => {
  //       const countries = data.map(country => ({
  //         name: country.country,
  //         value: country.countryInfo.iso2
  //       }));

  //       const sortedData = sortData(data);
  //       setTableData(sortedData);
  //       setMapCountries(data);
  //       setCountries(countries);
  //     })
  //   }
  //   getCountriesData();
  // }, [])

  // const onCountryChange = async (e) => {
  //   const countryCode = e.target.value
  //   setCountry(countryCode);

  //   const url = countryCode === 'worldwide' 
  //     ? 'https://disease.sh/v3/covid-19/all' 
  //     : `https://disease.sh/v3/covid-19/countries/${countryCode}`
  //   await fetch(url)
  //   .then(resp => resp.json())
  //   .then(data => {
  //     setCountry(countryCode); 
  //     setCountryInfo(data);

  //     countryCode === "worldwide"
  //         ? setMapCenter([34.80746, -40.4796])
  //         : setMapCenter([data.countryInfo.lat, data.countryInfo.long]);
  //   })
  // }




// *                     doesn't work yet, working on getting this to work                      *

  // useEffect(() => {
  //     const getStatesData = async () => {
  //         await fetch('http://localhost:5000/covid/states/')
  //         .then(response => response.json())
  //         .then(data => {
  //             const states = data.map(state=> ({
  //                 name: state.state,
  //                 value: state.state
  //             }));
  //             setMapStates(data);
  //             setStates(countries);
  //         })
  //     }
  //     getStatesData()
  // }, [])

  // const onStateChange = async (e) => {
  //   const stateCode = e.target.value
  //   setState(stateCode);

  //   const url = stateCode === 'states' 
  //     ? 'https://disease.sh/v3/covid-19/all' 
  //     : `http://localhost:5000/covid/states/${stateCode}`
  //   await fetch(url)
  //   .then(resp => resp.json())
  //   .then(data => {
  //     setState(stateCode); 
  //     setStateInfo(data);
  //     stateCode === "states"
  //         ? setMapCenter([40.1345916, -102.0903563])
  //         : setMapCenter([data.lat, data.long]);
  //   })
  // }


  useEffect(() => {
    const getCountriesData = async () => {
      await fetch("http://localhost:5000/covid/countries")
      .then(response => response.json())
      .then(data => {
        const countries = data.map(country => ({
          name: country.country,
          value: country.iso2
        }));

        const sortedData = sortData(data);
        setTableData(sortedData);
        setMapCountries(data);
        setCountries(countries);
      })
    }
    getCountriesData();
  }, [])

  const onCountryChange = async (event) => {
    console.log('================================');
    const countryCode = event.target.value
    console.log('================================');
    console.log(countryCode);
    setCountry(countryCode);

    const url = countryCode === 'worldwide' 
      ? 'https://disease.sh/v3/covid-19/all' 
      : `http://localhost:5000/covid/countries/${countryCode}`
    
    await fetch(url)
    .then(resp => resp.json())
    .then(data => {
      console.log(data)
      console.log(data.country)
      setCountry(countryCode); 
      setCountryInfo(data);
      countryCode === "worldwide"
          ? setMapCenter([34.80746, -40.4796])
          // : setMapCenter([data['lat'], data['long']]);
          : setMapCenter([data.lat, data.long]);
          // setMapZoom(4);
    })
  }


  return (
    <div className="app_main">
      <div className="app_left">
        <div className="app_header">
          <h1 style={{color:'white', fontFamily:"Lucida Console, Courier, monospace"}}>Covid-Spy</h1>
          <FormControl className="app_dropdown">
            <Select variant="outlined" value={country} onChange={onCountryChange}>
              <MenuItem value="worldwide">Worldwide</MenuItem>
              {countries.map(country => (
                <MenuItem value={country.name}>{country.name}</MenuItem>
                // <MenuItem value={Country.value}>{Country.name}</MenuItem>
                ))
              }
            </Select> 
          </FormControl>
          {/* <FormControl className='app_dropdown1'>
              <Select variant='outlined' value={state} onChange={onStateChange}>
                <MenuItem value='states' style={{color:'black'}}>States</MenuItem>
                {states.map(state => (
                    <MenuItem value='states' style={{color:'black'}}>States</MenuItem>
                ))}
              </Select>
          </FormControl> */}
        </div>

        <div className="app_stats">
          <InfoBox active={casesType === "cases"} onClick={e => setCasesType('cases')} 
                    title="Positive Cases" cases={prettyPrintStat(countryInfo.todayCases)} 
                    total={prettyPrintStat(countryInfo.cases)}/>

          <InfoBox active={casesType === "deaths"} onClick={e => setCasesType('deaths')} 
                    title="Mortality Rate" cases={prettyPrintStat(countryInfo.todayDeaths)} 
                    total={prettyPrintStat(countryInfo.deaths)}/>

          <InfoBox active={casesType === "recovered"} onClick={e => setCasesType('recovered')} 
                    title="Recovered" cases={prettyPrintStat(countryInfo.todayRecovered)} 
                    total={prettyPrintStat(countryInfo.recovered)}/>


          {/* working on InfoBox to work with backend */}
          {/* <InfoBox active={casesType === "cases"} onClick={e => setCasesType('cases')} 
                    title="Positive Cases" cases={prettyPrintStat(countryInfo['todayCases'])} 
                    total={prettyPrintStat(countryInfo['cases'])}/>

          <InfoBox active={casesType === "deaths"} onClick={e => setCasesType('deaths')} 
                    title="Mortality Rate" cases={prettyPrintStat(countryInfo['todayDeaths'])} 
                    total={prettyPrintStat(countryInfo['deaths'])}/>

          <InfoBox active={casesType === "recovered"} onClick={e => setCasesType('recovered')} 
                    title="Recovered" cases={prettyPrintStat(countryInfo['todayRecovered'])} 
                    total={prettyPrintStat(countryInfo['recovered'])}/> */}

        </div>

        {/* <div className="app_stats1">
          <InfoBox active={casesType === "cases"} onClick={e => setCasesType('cases')} 
                    title="Positive Cases" cases={prettyPrintStat(stateInfo.todayCases)} 
                    total={prettyPrintStat(stateInfo.cases)}/>

          <InfoBox active={casesType === "deaths"} onClick={e => setCasesType('deaths')} 
                    title="Mortality Rate" cases={prettyPrintStat(stateInfo.todayDeaths)} 
                    total={prettyPrintStat(stateInfo.deaths)}/>

          <InfoBox active={casesType === "recovered"} onClick={e => setCasesType('recovered')} 
                    title="Recovered" cases={prettyPrintStat(stateInfo.todayRecovered)} 
                    total={prettyPrintStat(stateInfo.recovered)}/>

        </div> */}

        {/* <Map casesType={casesType} states={mapStates} center ={mapStateCenter} zoom={mapStateZoom} /> */}
        <Map casesType={casesType} countries={mapCountries} center={mapCenter} zoom={mapZoom} setUserFav={setUserFav} userFav={userFav} />
      </div> 
    </div>
  );
}

export default Tracker;