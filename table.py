import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()


def att():

    sql = '''create table att
    (Serial_no int primary key,
    sub_name varchar(100) not null,
    present int,
    absent int,
    total int,
    percentage decimal(5,2),
    req_margin int)'''

    cur1.execute(sql)
    mycon.commit()

def od_det():

    sql = '''create table od_det(
            Serial_no int primary key,
            Sub_Name varchar(100),
            Date varchar(8),
            DO int,
            Faculty_name varchar(100),
            Event varchar(100)
            );'''

    cur1.execute(sql)
    mycon.commit()

def od():

    sql = '''create table od(
            Serial_no int primary key,
            od_hours int,
            ml_hours int,
            n_p decimal(5,2)
            );'''
    cur1.execute(sql)
    mycon.commit()     


att()
od()
od_det()
mycon.close()
