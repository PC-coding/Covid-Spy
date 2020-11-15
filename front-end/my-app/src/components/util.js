import React, { useState, useEffect } from "react";
import numeral from "numeral";
import { Circle, Popup } from "react-leaflet";


const casesTypeColors = {
  cases: {
    hex: "#7dd71d",
    rgb: "rgb(125, 215, 29)",
    half_op: "rgba(125, 215, 29, 0.5)",
    multiplier: 800,
  },
  recovered: {
    hex: "#a820df",
    rgb: "rgb(169, 32, 223)",
    half_op: "rgba(169, 32, 223, 0.5)",
    multiplier: 1200,
  },
  deaths: {
    hex: "#fb4443",
    rgb: "rgb(251, 68, 67)",
    half_op: "rgba(251, 68, 67, 0.5)",
    multiplier: 2000,
  },
};

export const sortData = (data) => {
  let sortedData = [...data];
  sortedData.sort((a, b) => {
    if (a.cases > b.cases) {
      return -1;
    } else {
      return 1;
    }
  });
  return sortedData;
};


  function Favorites({ token: token , country: country , userFav: userFav, setUserFav: setUserFav }){
    const SaveFavorites = async () => {
      const userData = JSON.stringify({'country': country, 'userFav': userFav, 'api_key': sessionStorage.getItem("token")});
      console.log(token);
      const configs = {
          method: 'POST',
          headers: {"Content-Type": "application/json"},
          body: userData
      };
      console.log(token);
      const response = await fetch('http://localhost:5000/covid/favorites', configs);
      console.log(response);
      const favData = await response.json();
      console.log(favData);
      // setUserFav(favData);
    }
    SaveFavorites();
  }

export const prettyPrintStat = (stat) =>
  stat ? `+${numeral(stat).format("0.0a")}` : "+0";

export const showDataOnMap = (data, casesType = "cases", { userFav: userFav, setUserFav: setUserFav, token: token } ) =>


  data.map((country) => (
    <Circle
      center={[country.lat, country.long]}

      color={casesTypeColors[casesType].hex}
      fillColor={casesTypeColors[casesType].hex}
      fillOpacity={0.4}
      radius={
        Math.sqrt(country[casesType]) * casesTypeColors[casesType].multiplier
      }
    >
      <Popup>
        <div className="info-container">
            <div className="info-flag"
                  style={{ backgroundImage: `url(${country.flag})` }}>
            </div>
            
            <div className="info-name">{country.country}</div>

            <div className="info-confirmed">
              Cases: {numeral(country.cases).format("0,0")}
            </div>

            <div className="info-recovered">
              Recovered: {numeral(country.recovered).format("0,0")}
            </div>

            <div className="info-deaths">
              Deaths: {numeral(country.deaths).format("0,0")}
            </div>
            {/* <button style={{backgroundColor:'blue', color:'white', fontWeight:'bold'}}>Add to List</button> */}
            <button style={{backgroundColor:'blue', color:'white', fontWeight:'bold'}} onClick={e => Favorites({token: token, country: country, userFav: userFav, setUserFav: setUserFav})}>
                    Add to List</button>
        </div>
          
      </Popup>
    </Circle>
    
  ));