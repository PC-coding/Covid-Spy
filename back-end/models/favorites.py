import sqlite3

class Favorites:
    tablename = 'favorites'
    dbpath = 'data/covid.db'

    def __init__(self, account_pk, updated, state, 
                country, ):
        self.account_pk = account_pk
        self.updated = updated
        self.state = state
        self.country = country

    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                updated,
                county_name,
                state_name,
                country_name,
                continent_name,
            ) VALUES (?,?,?,?,?)"""
            values = (self.updated, self.state, 
            self.country)
            cursor.execute(sql, values)
            return True
        return False

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            UPDATE {self.tablename} SET 
                updated=?,
                state=?,
                country=?
            WHERE account_pk=?"""
            cursor.execute(sql, (self.updated, self.state, 
                                self.country, self.account_pk))