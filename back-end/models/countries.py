import sqlite3

class Countries:
    tablename = 'covid_data_countries'
    dbpath = 'data/covid.db'

    def __init__(self, updated=0, country='', active=0, cases=0, todayCases=0, recovered=0,
                todayRecovered=0, deaths=0, todayDeaths=0, iso2='', lat=0.0, long=0.0, flag=''):
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

    def to_json(self):
        return {"updated": self.updated,
                "country": self.country,
                "active": self.active,
                "cases": self.cases,
                "todayCases": self.todayCases,
                "recovered": self.recovered,
                "todayRecovered": self.todayRecovered,
                "deaths": self.deaths,
                "todayDeaths": self.todayDeaths,
                "iso2": self.iso2,
                "lat": self.lat,
                "long": self.long,
                "flag": self.flag}
    
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
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE country =?
            ;"""
            values = (country,)
            cursor.execute(sql, values)
            return cls(**cursor.fetchone())
        return False

    @classmethod
    def select_all_countries(cls):
        with sqlite3.connect(cls.dbpath) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename}
            ;"""
            cursor.execute(sql)
            # return cursor.fetchall()
            return [cls(**row) for row in cursor.fetchall()]
        return []