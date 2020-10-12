import sqlite3

class Continents:
    tablename = 'covidDataContinents'
    dbpath = 'data/covid.db'

    def __init__(self, date, continent_name, positive_cases=0, recovered_cases=0, mortality_rate=0, total_cases=0):
        self.date = date
        self.continent_name = continent_name
        self.positive_cases = positive_cases
        self.recovered_cases = recovered_cases
        self.mortality_rate = mortality_rate
        self.total_cases = total_cases

    def save(self):
        with sqlite3.connect(self.dbpath) as conn:        
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                date,
                continent_name,
                positive_cases,
                recovered_cases,
                mortality_rate,
                total_cases
            ) VALUES (?,?,?,?,?,?)"""
            values = (self.date, self.continent_name, self.positive_cases, self.recovered_cases, self.mortality_rate, self.total_cases)
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def select_continent(cls, continent_name, date):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE continent_name =?, date =?
            ;"""
            values = (continent_name, date,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def select_all_continents(cls, date):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE date =?
            ;"""
            cursor.execute(sql, (date,))
            return cursor.fetchall()
        return []
    
    @classmethod
    def select_all_continent_month(cls, date):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE date =? - 00/30/00
            ;"""
    