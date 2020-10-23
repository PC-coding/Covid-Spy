import React,{  useState, useEffect  } from 'react';
import { Card, CardContent } from '@material-ui/core';
import Table from '../Table/Table.js';
import LineGraph from '../Graphs/LineGraph.js';
import { sortData, prettyPrintStat } from '../util.js';
import InfoBox from '../InfoBox/InfoBox.js';

export default function Graph(){
    const [countries, setCountries] = useState([]);
    const [country, setCountry] = useState('worldwide');
    const [countryInfo, setCountryInfo] = useState({});
    const [tableData, setTableData] = useState([]);
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

   return(
        <Card className="app_right">
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
            <CardContent>
            <h3>Live Cases by Country</h3>
            <Table countries={tableData} />
            <h3>Worldwide new {casesType}</h3>
            <LineGraph className="app_graph" casesType={casesType}/>
            </CardContent>
                </Card>     
   )  
}