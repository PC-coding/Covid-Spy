import sqlite3

def schema(dbpath='covid.db'):
    with sqlite3.connect(dbpath) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE covidDataContinents(
            positiveCases
            recoveredCases
            mortalityRate
            totalCases
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCountries(
            positiveCases
            recoveredCases
            mortalityRate
            totalCases
        );""")

        cursor.execute("""
        CREATE TABLE covidDataStates(
            positiveCases
            recoveredCases
            mortalityRate
            totalCases
        );""")

        cursor.execute("""
        CREATE TABLE covidDataCounties(
            positiveCases
            recoveredCases
            mortalityRate
            totalCases
        );""")
if __name__ = '__main__':
    schema()