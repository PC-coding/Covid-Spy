import sqlite3
from hashlib import sha256
import random
from models.favorites import Favorites
from models.countries import Countries

class Account:
    tablename = 'accounts'
    dbpath = 'data/covid.db'

    def __init__(self, username, password_hash, api_key, email, pk=None):
        self.username = username
        self.password_hash = password_hash
        self.api_key = api_key
        self.email = email
        self.pk = pk

    def save(self):
        if self.pk:
            self._update()
        else:
            self._insert()
    
    def _insert(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO {self.tablename} (
                username,
                password_hash,
                api_key,
                email
            ) VALUES (?,?,?,?)"""
            values = (self.username, self.password_hash, self.api_key, self.email)
            cursor.execute(sql, values)
            return cursor.lastrowid

    def _update(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            UPDATE {self.tablename} SET 
                api_key=?
            WHERE pk=?"""
            cursor.execute(sql, (self.api_key, self.pk))

    # -- for country names + country active cases -- 
    # def save_favorites(self, country):
    #     with sqlite3.connect(self.dbpath) as conn:
    #         cursor = conn.cursor()
    #         sql = f"""
    #         INSERT INTO favorites (
    #             account_pk,
    #             country,
    #             active
    #         ) VALUES (?,?,?)"""
    #         values = (self.pk, country, active)
    #         cursor.execute(sql, values)
    #         return True
    #     return False

    def save_favorites(self, country):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            INSERT INTO favorites (
                account_pk,
                country
            ) VALUES (?,?)"""
            values = (self.pk, country)
            cursor.execute(sql, values)
            return True
        return False

    # def save_favorites(self, country):
    #     if self.pk:
    #         self._updatefav(country)
    #     else:
    #         self._insertfav(country)

    # def _updatefav(self, country):
    #     with sqlite3.connect(self.dbpath) as conn:
    #         cursor = conn.cursor()
    #         sql = f"""
    #         UPDATE favorites SET 
    #             country=?
    #         WHERE account_pk=?"""
    #         cursor.execute(sql, (country, self.pk))

    # def _insertfav(self, country):
    #         with sqlite3.connect(self.dbpath) as conn:
    #             cursor = conn.cursor()
    #             sql = f"""
    #             INSERT INTO favorites (
    #                 account_pk,
    #                 country
    #             ) VALUES (?,?)"""
    #             values = (self.pk, country)
    #             cursor.execute(sql, values)
    #             return True
    #         return False

    def delete_favorites(self, country):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            DELETE FROM favorites WHERE account_pk=? AND country=?
            """
            values = (self.pk, country)
            cursor.execute(sql, values)
            # cursor.execute(sql)            
            return True
        return False

    def filter_favs(self):
        with sqlite3.connect(self.dbpath) as conn:
            cursor = conn.cursor()
            sql = f"""
            SELECT * FROM favorites WHERE account_pk=?
            """
            values = (self.pk, )
            req = cursor.execute(sql, values)
            return list(set(req.fetchall()))
        return False


    @classmethod
    def login(cls, username, password):
        with sqlite3.connect(cls.dbpath) as conn:
            curs = conn.cursor()
            sql = """SELECT * FROM accounts WHERE username=? and password_hash=?;"""
            curs.execute(sql, (username, cls.hash_password(password)))
            account = curs.fetchone()
            if account:
                return Account(*account[1:], account[0])
            return None

    @classmethod
    def api_authenticate(cls, api_key):
        with sqlite3.connect(cls.dbpath) as conn:
            cursor = conn.cursor()
            sql = """SELECT * FROM accounts WHERE api_key=?"""
            cursor.execute(sql, (api_key,))
            account = cursor.fetchone()
            if account:
                return Account(*account[1:], account[0])
                # return Account(account[1], account[2], account[3], account[4], account[5], account[0])
            return None

    @staticmethod
    def hash_password(password):
        hasher = sha256()
        hasher.update(password.encode())
        return hasher.hexdigest()

    @staticmethod
    def random_api_key(length=15):
        random_string = "".join([str(random.randint(1,10)) for i in range(25)])
        hasher = sha256()
        hasher.update(random_string.encode())
        return hasher.hexdigest()[:length]
