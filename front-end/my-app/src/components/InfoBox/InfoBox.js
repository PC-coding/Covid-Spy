import React from 'react';
import './InfoBox.css';
import { Card, CardContent, Typography } from "@material-ui/core";

function InfoBox({ title, cases, active, total, isRed, ...props }) {
    return (
        <Card
        onClick={props.onClick}
        className={`infoBox ${active && 'infoBox--selected'}
        ${ isRed && "infoBox--red"}`} 
            >
            <CardContent>
                <Typography className="infoBox_title" color="textSecondary">
                    {title}
                </Typography>
                <h2 className={`infoBox__cases ${!isRed && "infoBox__cases--green"}`}>
                {cases}
                </h2>
                <Typography className="infoBox_total" color="textSecondary">
                    Total Cases: {total}
                </Typography>
            </CardContent>
        </Card>
    )
}

export default InfoBox