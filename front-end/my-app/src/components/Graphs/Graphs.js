import React,{  useState, useEffect  } from 'react';
import { MenuItem, FormControl, Select, Card, CardContent } from '@material-ui/core';
import Table from '../Table/Table.js';
import LineGraph from '../Graphs/LineGraph.js';
import { sortData, prettyPrintStat } from '../util.js';
import InfoBox from '../InfoBox/InfoBox.js';



// export default function Graph(){
//     return(
//         <div className='graphApp'>
//             <h1>testing tracker</h1>
//             <FormControl className='graph_dropdown'>
//                 <Select variant='outlined' value='ab'>
//                     <MenuItem value='Continents'>Continents</MenuItem>
//                     <MenuItem value='Countries'>Countries</MenuItem>
//                     <MenuItem value='States'>States</MenuItem>
//                     <MenuItem value='Counties'>Counties</MenuItem>
//                 </Select>
//             </FormControl>
//         </div>
//     )
// }

export default function Graph(){
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