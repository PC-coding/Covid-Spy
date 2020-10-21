import sqlite3

class Countries:
    tablename = 'covid_data_countries'
    dbpath = 'data/covid.db'

    def __init__(self, time_stamp, country_name, positive_cases, recovered_cases, 
                mortality_rate, total_cases, iso2, lat, long, flag):
        self.time_stamp = time_stamp
        self.country_name = country_name
        self.positive_cases = positive_cases
        self.recovered_cases = recovered_cases
        self.mortality_rate = mortality_rate
        self.total_cases = total_cases
        self.iso2 = iso2
        self.lat = lat
        self.long = long
        self.flag = flag 
    
    # def save(self):
    #     if self.country_name:
    #         self._update()
    #     else:
    #         self._insert()
    
    def save(self):
        with sqlite3.connect(self.dbpath) as conn:        
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                time_stamp,
                country_name,
                positive_cases,
                recovered_cases,
                mortality_rate,
                total_cases,
                iso2,
                lat,
                long,
                flag
            ) VALUES (?,?,?,?,?,?,?,?,?,?)"""
            values = (self.time_stamp, self.country_name, self.positive_cases, 
                    self.recovered_cases, self.mortality_rate, self.total_cases,
                    self.iso2, self.lat, self.long, self.flag)
            cursor.execute(sql, values)
            return True
        return False

    # def _update(self):
    #     with sqlite3.connect(self.dbpath) as conn:
    #         cursor = conn.cursor()
    #         sql = f"""
    #         UPDATE {self.tablename} SET
    #             time_stamp,
    #             positive_cases,
    #             recovered_cases,
    #             mortality_rate,
    #             total_cases
    #         ) VALUES (?,?,?,?,?,?)"""
    #         values = (self.time_stamp, self.positive_cases, 
    #                 self.recovered_cases, self.mortality_rate, self.total_cases)
    #         cursor.execute(sql, values)
    #         return True
    #     return False
    
    @classmethod
    def select_country(cls, country_name, time_stamp):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE country_name =?, time_stamp =?
            ;"""
            values = (cls.country_name, cls.time_stamp)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    # @classmethod
    # def select_all_countries(cls, date):
    #     with sqlite3.connect(cls.dbpath) as conn:
    #         cursor = conn.cursor()
    #         sql = f"""
    #         SELECT * FROM {cls.tablename} WHERE date =?
    #         ;"""
    #         cursor.execute(sql, (date,))
    #         return cursor.fetchall()
    #     return []


    @classmethod
    def select_all_countries(cls, time_stamp):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE time_stamp =?
            ;"""
            cursor.execute(sql, (cls.time_stamp,))
            return cursor.fetchall()
        return []