import sqlite3

def schema(dbpath='covid.db'):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE covidDataContinents(
            date DATETIME,
            continent_name VARCHAR, 
            positive_cases INTEGER,
            recovered_cases INTEGER,
            mortality_rate INTEGER,
            total_cases INTEGER
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCountries(
            date DATETIME,
            country_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")

        cursor.execute("""
        CREATE TABLE covidDataStates(
            date DATETIME,
            state_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCounties(
            date DATETIME,
            county_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")

        cursor.execute("""
        CREATE TABLE accounts(
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(11) UNIQUE NOT NULL,
            password_hash VARCHAR(128),
            api_key VARCHAR,
            email VARCHAR
        );""")
if __name__ = '__main__':
    schema()