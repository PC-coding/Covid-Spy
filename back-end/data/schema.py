import sqlite3

def schema(dbpath="covid.db"):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE covid_data_continents (
            time_stamp INTEGER,
            continent_name VARCHAR, 
            positive_cases INTEGER,
            recovered_cases INTEGER,
            mortality_rate INTEGER,
            total_cases INTEGER,
            iso2 VARCHAR,
            lat INTEGER,
            long INTEGER,
            flag VARCHAR
        );""")

        cursor.execute("""
        CREATE TABLE covid_data_countries (
            time_stamp INTEGER,
            country_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER,
            iso2 VARCHAR,
            lat INTEGER,
            long INTEGER,
            flag VARCHAR
        );""")

        cursor.execute("""
        CREATE TABLE covid_data_states (
            time_stamp INTEGER,
            state_name VARCHAR,
            positive_cases INTEGER,
            recovered_cases INTEGER, 
            mortality_rate INTEGER, 
            total_cases INTEGER,
            lat INTEGER,
            long INTEGER,
        );""")

        cursor.execute("""
        CREATE TABLE covid_data_counties (
            time_stamp INTEGER,
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

        cursor.execute("""
        CREATE TABLE favorites(
            time_stamp INTEGER,
            account_pk INTEGER,
            county_name VARCHAR,
            state_name VARCHAR,
            country_name VARCHAR,
            continent_name VARCHAR
        );""")

if __name__ == "__main__":
    schema()