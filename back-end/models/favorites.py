import sqlite3

class Favorites:
    tablename = 'favorites'
    dbpath = 'data/covid.db'

    def __init__(self, account_pk, date, county_name, state_name, 
                country_name, continent_name):
        self.account_pk = account_pk
        self.date = date
        self.county_name = county_name
        self.state_name = state_name
        self.country_name = country_name
        self.continent_name = continent_name

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                date,
                county_name,
                state_name,
                country_name,
                continent_name,
            ) VALUES (?,?,?,?,?)"""
            values = (self.date, self.county_name, self.state_name, 
            self.country_name, self.continent_name)
            cursor.execute(sql, values)
            return True
        return False

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            UPDATE {self.tablename} SET 
                date=?,
                county_name=?,
                state_name=?,
                country_name=?,
                continent_name=?
            WHERE account_pk=?"""
            cursor.execute(sql, (self.date, self.county_name, self.state_name, 
                                self.country_name, self.continent_name, 
                                self.account_pk))