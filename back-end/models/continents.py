import sqlite3

class Continents:
    tablename = 'covid_data_continents'
    dbpath = 'data/covid.db'

    def __init__(self, time_stamp, continent_name, positive_cases=0, 
                recovered_cases=0, mortality_rate=0, total_cases=0):
        self.time_stamp = time_stamp
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
                time_stamp,
                continent_name,
                positive_cases,
                recovered_cases,
                mortality_rate,
                total_cases
            ) VALUES (?,?,?,?,?,?)"""
            values = (self.time_stamp, self.continent_name, self.positive_cases, self.recovered_cases, 
                    self.mortality_rate, self.total_cases)
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def select_continent(cls, continent_name, time_stamp):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE continent_name =?, time_stamp =?
            ;"""
            values = (continent_name, time_stamp,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def select_all_continents(cls, time_stamp):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE time_stamp =?
            ;"""
            cursor.execute(sql, (time_stamp,))
            return cursor.fetchall()
        return []