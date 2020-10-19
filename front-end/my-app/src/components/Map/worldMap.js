import React from 'react';
import { MenuItem, FormControl, Select } from '@material-ui/core';

export default function Map(){
    return(
        <div>
            <h1>testing11</h1>
            <FormControl className='graph_dropdown'>
                <Select variant='outlined' value='abc'>
                    <MenuItem value='Continents'>Continents</MenuItem>
                    <MenuItem value='Countries'>Countries</MenuItem>
                    <MenuItem value='States'>States</MenuItem>
                    <MenuItem value='Counties'>Counties</MenuItem>
                </Select>
            </FormControl>
        </div>
    )
}