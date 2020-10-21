import React, { useState, useEffect } from 'react';
import { MenuItem, FormControl, Select } from "@material-ui/core";
import './Tracker.css';
import InfoBox from '../InfoBox/InfoBox.js';
import Map from '../Map/map.js';
// import Table from '../Table/Table.js';
// import LineGraph from '../Graphs/LineGraph.js';
import { sortData, prettyPrintStat } from '../util.js';
import "leaflet/dist/leaflet.css";


function Tracker() {
  const [countries, setCountries] = useState([]);
  const [country, setCountry] = useState('worldwide');
  const [countryInfo, setCountryInfo] = useState({});
  const [tableData, setTableData] = useState([]);
  const [mapCenter, setMapCenter] = useState({
                                                lat: 34.80746,
                                                lng: -40.4796
                                            });
  const [mapZoom, setMapZoom] = useState(4);
  const [mapCountries, setMapCountries] = useState([]);
  const [casesType, setCasesType] = useState("cases");


  useEffect(() => {
    fetch('https://disease.sh/v3/covid-19/all')
    .then(resp => resp.json())
    .then(data => {
      setCountryInfo(data);
    })
  }, [])

  useEffect(() => {
    const getCountriesData = async () => {
      await fetch("https://disease.sh/v3/covid-19/countries")
    //   await fetch("https://localhost:5000/covid/save_country/")
      .then(response => response.json())
      .then(data => {
        const countries = data.map(country => ({
          name: country.country,
          value: country.countryInfo.iso2
        }));

        const sortedData = sortData(data);
        setTableData(sortedData);
        setMapCountries(data);
        setCountries(countries);
      })
    }
    getCountriesData();
  }, [])

  const onCountryChange = async (e) => {
    const countryCode = e.target.value
    setCountry(countryCode);

    const url = countryCode === 'worldwide' 
      ? 'https://disease.sh/v3/covid-19/all' 
    //   : `https://localhost:5000/covid/save_country/${countryCode}`
      : `https://disease.sh/v3/covid-19/countries/${countryCode}`
    await fetch(url)
    .then(resp => resp.json())
    .then(data => {
      setCountry(countryCode); 
      setCountryInfo(data);

      // setMapCenter([data.countryInfo.lat, data.countryInfo.long]);
      // setMapZoom(4);
      countryCode === "worldwide"
          ? setMapCenter([34.80746, -40.4796])
          : setMapCenter([data.countryInfo.lat, data.countryInfo.long]);
    })
  }

  return (
    <div className="app_main">
      <div className="app_left">
        <div className="app_header">
          <h1 style={{color:'white'}}>Covid-19 TRACKER</h1>
          <FormControl className="app_dropdown">
            <Select variant="outlined" value={country} onChange={onCountryChange}>
              <MenuItem value="worldwide">Worldwide</MenuItem>
              {countries.map(country => (
                <MenuItem value={country.value}>{country.name}</MenuItem>
                ))
              }
            </Select> 
          </FormControl>
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

        </div>

        <Map casesType={casesType} countries={mapCountries} center={mapCenter} zoom={mapZoom}/>
      </div> 
    </div>
  );
}

export default Tracker;