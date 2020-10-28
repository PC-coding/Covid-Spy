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

    def save_fav(self, account_pk):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                updated,
                state,
                country,
            ) VALUES (?,?,?)"""
            values = (self.updated, self.state, 
            self.country)
            cursor.execute(sql, values)
            return True
        return False