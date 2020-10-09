import sqlite3

def schema(dbpath='covid.db'):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE covidDataContinents(
            date DATE,
            continent_name VARCHAR, 
            positive_cases INTEGER,
            recovered_cases INTEGER,
            mortality_rate INTEGER,
            total_cases INTEGER
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCountries(
            date DATE,
            country_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")

        cursor.execute("""
        CREATE TABLE covidDataStates(
            date DATE,
            state_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCounties(
            date DATE,
            county_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER 
        );""")
if __name__ = '__main__':
    schema()