import sqlite3

class States:
    tablename = 'covid_data_states'
    dbpath = 'data/covid.db'

    def __init__(self, updated=0, state='', active=0, cases=0, todayCases=0, 
                recovered=0, deaths=0, todayDeaths=0, lat=0.0, long=0.0):
        self.updated = updated
        self.state = state
        self.active = active       
        self.cases = cases
        self.todayCases = todayCases
        self.recovered = recovered
        self.deaths = deaths
        self.todayDeaths = todayDeaths
        self.lat = lat
        self.long = long

    def save(self):
        with sqlite3.connect(self.dbpath) as conn:        
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                updated,
                state,
                active,
                cases,
                todayCases,
                recovered,
                deaths,
                todayDeaths
            ) VALUES (?,?,?,?,?,?,?,?)"""
            values = (self.updated, self.state, self.active, 
                    self.cases, self.todayCases, self.recovered, 
                    self.deaths, self.todayDeaths)
            cursor.execute(sql, values)
            return True
        return False
    
    def update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            UPDATE {self.tablename} SET 
                lat=?,
                long=?
            WHERE state=?"""
            cursor.execute(sql, (self.lat, self.long, self.state))
            return True
        return False
    
    @classmethod
    def select_state(cls, state):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE state =?
            ;"""
            values = (state,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def select_all_states(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename}
            ;"""
            cursor.execute(sql)
            return cursor.fetchall()
        return []
    