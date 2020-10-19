import React from 'react';
import { Link } from 'react-router-dom';

export default function Globe() {
        return(
            <Link to='/tracker'>
                <div className="pulse">
                    <span></span>
                    <span></span>
                </div>
            </Link>
        )
}