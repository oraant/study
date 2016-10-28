import MySQLdb as M
import warnings

# test for create and drop databases;

"""
db = M.connect(host="127.0.0.1",user="django",passwd="django")
cursor = db.cursor()

sql1 = "CREATE DATABASE IF NOT EXISTS %s DEFAULT CHARACTER SET utf8" % "hahaha"
sql2 = "drop database if exists hahaha"
#sql1 = "CREATE DATABASE %s DEFAULT CHARACTER SET utf8" % "hahaha"
#sql2 = "drop database hahaha"

sql = sql2

with warnings.catch_warnings():
    #warnings.simplefilter("error")
    res1 = cursor.execute(sql)
    print 'res1 done'
    res2 = cursor.execute(sql)
    print 'res2 done'
    res3 = cursor.execute(sql)
    print 'res3 done'
    res4 = cursor.execute(sql)
    print 'res4 done'
    res5 = cursor.execute(sql)
    print 'res5 done'
print 'end'
cursor.close()
db.close()
"""

# test for create and drop tables

ignore_warns = ["database exists", "database doesn't exist", "Table .* already exists", "Unknown table"]
warnings.filterwarnings("ignore", '|'.join(ignore_warns))

db = M.connect(host="127.0.0.1",user="django",passwd="django",db="hahaha")
cursor = db.cursor()

sql1 = "CREATE TABLE IF NOT EXISTS %s (id int, name varchar(4))" % "tttt"
sql2 = "drop table if exists tttt"
sql = sql1

for i in range(4):
    cursor.execute(sql)
cursor.close()
db.close()
