import sqlite3 as sql

con = sql.connect('users.db')

with con:
    db = con.cursor()
    db.execute("""CREATE TABLE IF NOT EXISTS `userss`
        (id INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT 0, 
        vk_id STRING,
        clicks INTEGER DEFAULT 0)
        """)
    con.commit()


class UsersInfo:
    def rows(self):
        db.execute("SELECT COUNT(*) FROM 'userss'")
        con.commit()
        values = db.fetchone()
        return int(values[0])

    def is_reg(user_vk_id):
        db.execute(f"SELECT * FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        if values is None:
            return False
        else:
            return True


    def insert(user_vk_id):
        db.execute(f"INSERT INTO 'userss' (vk_id) VALUES (?)", [user_vk_id])
        con.commit()

        db.execute(f"SELECT Login FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values[0]

    def get_login(user_vk_id):
        db.execute(f"SELECT Login FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values[0]

    def update_login(user_vk_id, update):
        db.execute(f"UPDATE 'userss' SET Login = ? WHERE vk_id = {user_vk_id}", [update])
        con.commit()

    def get_password(user_vk_id):
        db.execute(f"SELECT Password FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values[0]

    def update_password(user_vk_id, update):
        db.execute(f"UPDATE 'userss' SET Password = ? WHERE vk_id = {user_vk_id}", [update])
        con.commit()

    def get_name_of_school(user_vk_id):
        db.execute(f"SELECT Name_of_school FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values[0]

    def update_name_of_school(user_vk_id, update):
        db.execute(f"UPDATE 'userss' SET Name_of_school = ? WHERE vk_id = {user_vk_id}", [update])
        con.commit()

    def get_registration(user_vk_id):
        db.execute(f"SELECT registration FROM 'userss' WHERE vk_id= '{user_vk_id}'")
        con.commit()
        values = db.fetchone()
        return values

    def update_registration(user_vk_id, update):
        db.execute(f"UPDATE 'userss' SET registration = ? WHERE vk_id = {user_vk_id}", [update])
        con.commit()