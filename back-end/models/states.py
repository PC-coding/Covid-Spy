import sqlite3

class States:
    tablename = 'covid_data_states'
    dbpath = 'data/covid.db'

    def __init__(self, updated, state, active, cases, todayCases, 
                recovered, deaths, todayDeaths, lat, long):
        self.updated = updated
        self.state = state
        self.active = active       
        self.cases = cases
        self.todayCases = todayCases
        self.recovered = recovered
        self.deaths = deaths, 
        self.todayDeaths = todayDeaths, 
        self.lat = lat,
        self.long = long
        
    def save(self):
        with sqlite3.connect(self.dbpath) as conn:        
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                updated,
                state,
                active                
                cases,
                todayCases,
                recovered,
                deaths, 
                todayDeaths, 
                lat, 
                long)
                VALUES (?,?,?,?,?,?,?,?,?,?)"""
            values = (self.updated, self.state, self.active, self.cases, 
                    self.todayCases, self.recovered, self.deaths, self.todayDeaths, 
                    self.lat, self.long)            
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def select_state(cls, state, updated):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE state =?, updated =?
            ;"""
            values = (cls.state, cls.updated,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def select_all_states(cls, updated):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE updated =?
            ;"""
            cursor.execute(sql, (cls.updated,))
            return cursor.fetchall()
        return []
    