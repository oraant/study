# coding:utf-8
import MySQLdb
from MySQLdb.cursors import DictCursor

conn = MySQLdb.connect('localhost','django','django','test',3306)
cursor = conn.cursor(cursorclass=DictCursor)

cursor.execute('select ID, name from ttt')
print cursor.fetchall()
# 结论：
# 数据库中的NULL，在Python中会变成None
# 列填的是大写，字典的键就是大写
