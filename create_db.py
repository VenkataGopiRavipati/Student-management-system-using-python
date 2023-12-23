import sqlite3

def create_db():
    con = sqlite3.connect(database = "rms.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course (cid INTEGER PRIMARY KEY AUTOINCREMENT, name text, duration text, charges text ,description text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY AUTOINCREMENT, name text,email text,gender text,dob text,contact text,course text,account_status text,address text,state text,city text,zip text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT, roll text, name text, course text ,marks text, full_marks text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS studentlogin(sid INTEGER PRIMARY KEY AUTOINCREMENT ,username text, password text)")
    con.commit()

    con.close()


create_db()