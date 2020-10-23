import sqlite3

class Countries:
    tablename = 'covid_data_countries'
    dbpath = 'data/covid.db'

    def __init__(self, updated, country, active, cases, todayCases, recovered,
                todayRecovered, deaths, todayDeaths, iso2, lat, long, flag):
        self.updated = updated
        self.country = country
        self.active = active
        self.cases = cases
        self.todayCases = todayCases
        self.recovered = recovered
        self.todayRecovered = todayRecovered
        self.deaths = deaths
        self.todayDeaths = todayDeaths
        self.iso2 = iso2
        self.lat = lat
        self.long = long
        self.flag = flag 
    
    def save(self):
        with sqlite3.connect(self.dbpath) as conn:        
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                updated,
                country,
                active,
                cases,
                todayCases,
                recovered,
                todayRecovered,
                deaths,
                todayDeaths,
                iso2,
                lat,
                long,
                flag
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"""
            values = (self.updated, self.country, self.active, 
                    self.cases, self.todayCases, self.recovered, self.todayRecovered, 
                    self.deaths, self.todayDeaths, self.iso2, self.lat, self.long, 
                    self.flag)
            cursor.execute(sql, values)
            return True
        return False
    
    @classmethod
    def select_country(cls, country):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE country =?
            ;"""
            values = (country,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def select_all_countries(cls, ):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename}
            ;"""
            cursor.execute(sql)
            return cursor.fetchall()
        return []