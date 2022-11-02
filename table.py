import mysql.connector as ms
mycon = ms.connect(host="localhost",user="root",db="attendance",passwd="vibhu")
cur1 = mycon.cursor()


def att():

    sql = '''create table att
    (serial int primary key,
    sub_name varchar(100) not null,
    present int,
    absent int,
    total int,
    percentage decimal(4,2),
    req_margin int)'''

    cur1.execute(sql)
    mycon.commit()

att()
mycon.close()
