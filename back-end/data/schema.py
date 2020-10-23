import sqlite3

def schema(dbpath="covid.db"):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE covid_data_countries (
            updated INTEGER,
            country VARCHAR,
            active INTEGER,
            cases INTEGER,
            todayCases INTEGER,
            recovered INTEGER, 
            todayRecovered INTEGER,
            deaths INTEGER, 
            todayDeaths INTEGER,
            iso2 INTEGER,
            lat INTEGER,
            long INTEGER,
            flag VARCHAR
        );""")

        cursor.execute("""
        CREATE TABLE covid_data_states (
            updated INTEGER,
            state VARCHAR,
            active INTEGER,
            cases INTEGER,
            todayCases INTEGER,
            recovered INTEGER, 
            deaths INTEGER, 
            todayDeaths INTEGER,
            lat INTEGER,
            long INTEGER
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
            state_name VARCHAR,
            country_name VARCHAR
        );""")

if __name__ == "__main__":
    schema()