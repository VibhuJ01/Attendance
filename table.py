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


def od():

    sql = '''create table od(
            Serial_no int primary key,
            Name varchar(100),
            od_hours int,
            ml_hours int,
            n_p decimal(5,2)
            );'''
    cur1.execute(sql)
    mycon.commit()     

mycon.close()
