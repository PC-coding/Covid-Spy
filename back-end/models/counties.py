import sqlite3

class Counties:
    tablename = 'covidDataCounties'
    dbpath = 'data/covid.db'

    def __init__(self, positiveCases=0, recoveredCases=0, mortalityRate=0, totalCases=0):
        self.positiveCases = positiveCases
        self.recoveredCases = recoveredCases
        self. mortalityRate = mortalityRate
        self. totalCases = totalCases