import sqlite3


def db_connection(func):
    def warp(*args):
        global conn
        conn = sqlite3.connect('bonnyhotel.db')
        output = func(*args)
        if conn is not None:
            conn.close()

        return output
    return warp

@db_connection
def read_user_action(line_user_id):
    sql = f"SELECT `line_user_id`, `previous_action` from `users` WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data[1] if data else None

@db_connection
def read_user_data(line_user_id, line_user_name):
    sql = f"SELECT `line_user_id`, `line_user_name`, `kg`, `cm`, `age` from `users` WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    if not data:
        sql = f"INSERT INTO `users` (`line_user_id`, `line_user_name`) VALUES ('{line_user_id}', '{line_user_name}')"
        cursor.execute(sql)
        conn.commit()
        sql = f"SELECT `line_user_id`, `line_user_name`, `kg`, `cm`, `age` from `users` WHERE `line_user_id`='{line_user_id}'"
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
    return data

@db_connection
def update_user_action(line_user_id, action):
    sql = f"UPDATE `users` set `previous_action`='{action}' WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()





@db_connection
def update_user_kg(line_user_id, kg):
    sql = f"UPDATE `users` set `kg`='{kg}' WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@db_connection
def update_user_cm(line_user_id, cm):
    sql = f"UPDATE `users` set `cm`='{cm}' WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

@db_connection
def update_user_age(line_user_id, age):
    sql = f"UPDATE `users` set `age`='{age}' WHERE `line_user_id`='{line_user_id}'"
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()