# -*- coding: utf-8 -*-

import sqlite3
#connect to sqlite3 
#database file is test.db
#if not exit, it will be created

testconn= sqlite3.connect('test.db')
#create a cursor
#cursor = testconn.cursor()
# excute a sql 
#cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
#cursor.execute('insert into user(id,name) values (\'13\',\'Tom Wang\')')
#print cursor.rowcount
#testconn.commit()
#cursor.close()
cursor=testconn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(id,name) values (\'2\',\'王者\')')
cursor.execute('select * from user')
values = cursor.fetchall()
testconn.commit()
testconn.close()
print values

