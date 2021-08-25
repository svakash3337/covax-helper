import mysql.connector as sql

def sqlfunc(area, hospital, name, age, gender, vax):
    db = sql.connect(
        host="localhost",
        user="root",
        password="password",
        database=area
    )
    cur = db.cursor()
    query = "INSERT INTO " + hospital + "(`Name`, `Age`, `Gender`, `Vaccine`) VALUES ('" + name + "' , " + age + " , '" + gender + "','" + vax + "'" + "); "
    cur.execute(query)
    db.commit()
    a = cur.lastrowid
    db.close()
    return a

def hospitalz(area):
    db = sql.connect(
        host="localhost",
        user="root",
        password="password",
        database=area
    )
    cur = db.cursor()
    query = "SHOW TABLES"
    cur.execute(query)
    a = cur.fetchall()
    lis = []
    for i in a:
        lis.append(i[0])

    tupile = tuple(lis)
    db.close()
    return tupile





def search_1(area, hospital, id):
    name = ''
    age = ''
    gender = ''
    vaccine = ''
    # # print(area)
    if area == 1:
        # print("we're gonna be talking about the north")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='northchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
        name = result[1]
        age = result[2]
        gender = result[3]
        vaccine = result[4]
    elif area == 2:
        # print("we're gonna be talking about the central")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='centralchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
        name = result[1]
        age = result[2]
        gender = result[3]
        vaccine = result[4]
    elif area == 3:
        # print("we're gonna be talking about the south")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='southchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id) + ";"
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
        name = result[1]
        age = result[2]
        gender = result[3]
        vaccine = result[4]
    else:
        print("you messed up")
    db.close()
    return name, age, gender, vaccine


def isreal(area, hospital, id):
    result = False
    # print(area)
    if area == 1:
        # print("we're gonna be talking about the north")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='northchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
    elif area == 2:
        # print("we're gonna be talking about the central")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='centralchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
    elif area == 3:
        # print("we're gonna be talking about the south")
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='southchennai'
        )
        cur = db.cursor()
        query = "SELECT * from " + hospital + " WHERE ID = " + str(id) + ";"
        # print(query)
        cur.execute(query)
        result = cur.fetchone()
    db.close()
    if result is None:
        return False
    elif result is not None:
        return True


# noinspection PyGlobalUndefined
def cancel_1(area, hospital, id):
    global db
    # print(area)
    if area == 1:
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='northchennai'
        )
        # print("we're gonna be talking about the north")
        cur = db.cursor()
        query = "DELETE FROM " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
    elif area == 2:
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='centralchennai'
        )
        # print("we're gonna be talking about the central")
        cur = db.cursor()
        query = "DELETE FROM " + hospital + " WHERE ID = " + str(id)
        # print(query)
        cur.execute(query)
    elif area == 3:
        db = sql.connect(
            host="localhost",
            user="root",
            password="password",
            database='southchennai'
        )
        # print("we're gonna be talking about the south")
        cur = db.cursor()
        query = "DELETE FROM " + hospital + " WHERE ID = " + str(id) + ";"
        # print(query)
        cur.execute(query)
    else:
        print("you messed up")
    db.commit()
    db.close()
