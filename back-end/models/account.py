import sqlite3
from hashlib import sha256

class Account:
    tablename = 'accounts'
    dbpath = 'data/covid.db'

    def __init__(self, username, password_hash, api_key, email, pk):
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
                email=?,
                api_key=?
            WHERE pk=?"""
            cursor.execute(sql, (self.email, self.api_key, self.pk))

    @classmethod
    def login(cls, username, password):
        """Will need to hash input password, and then return either a 
        User instance or None
        """
        with sqlite3.connect(cls.dbpath) as conn:
            curs = conn.cursor()
            sql = """SELECT * FROM accounts WHERE username=? and password_hash=?;"""
            print(username, cls.hash_password(password))
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
                return Account(*account[:1], account[0])
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