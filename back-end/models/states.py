import sqlite3

class States:
    tablename = 'covidDataStates'
    dbpath = 'data/covid.db'

    def __init__(self, date, state_name, positive_cases=0, recovered_cases=0, mortality_rate=0, total_cases=0):
        self.date = date
        self.state_name = state_name
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
                state_name,
                positive_cases,
                recovered_cases,
                mortality_rate,
                total_cases
            ) VALUES (?,?,?,?,?,?)"""
            values = (self.date, self.state_name, self.positive_cases, self.recovered_cases, self.mortality_rate, self.total_cases)
            cursor.execute(sql, values)
            return True
        return False

    @classmethod
    def select_state(cls, state_name, date):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql= f"""
            SELECT * FROM {cls.tablename} WHERE state_name =?, date =?
            ;"""
            values = (state_name, date,)
            cursor.execute(sql, values)
            return cursor.fetchall()
        return False

    @classmethod
    def states_all_states(cls, date):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM {cls.tablename} WHERE date =?
            ;"""
            cursor.execute(sql, (date,))
            return cursor.fetchall()
        return []
    