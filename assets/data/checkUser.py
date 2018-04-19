#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import requests
import socket






# 创建Teacher 表
Teacher='''
    create table Teacher(
        TID int primary key not null,
        TName varchar(100) not null
    )
'''

User = '''
    create table User(
      UID int auto_increment primary key,
      UNAME VARCHAR (100) NOT NULL ,
      UPASSWD VARCHAR (100) NOT NULL 
    )
'''


TMP='''
    set @i :=0;
    create table TMP as select (@i := @i + 1) as id from information_schema.tables limit 10;
'''

sql = """INSERT INTO User VALUES (%s, %s, %s)"""
param = ((1, 'LEESHEEQEE', '456258'), (2, 'MESSAGE', 'SSA55258'))  #对应的param是一个tuple或者list


searchUserName = '''
    SELECT * FROM User WHERE UNAME = 'LEESHEEQEE'
'''

searchPassWord = '''
  SELECT * FROM User WHERE UPASSWD = passWord
'''

def create_db(host, user, passwd, dbdata, port):
  try:
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, port=port, charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 执行sql语句
    cursor.execute('show databases')
    rows = cursor.fetchall()
    for row in rows:
      tmp = "%2s" % row
      print(tmp)
      # 判断数据库是否存在
      if dbdata == tmp:
        cursor.execute('drop database if EXISTS ' + dbdata)
        cursor.execute('create database if not EXISTS ' + dbdata)
        db.commit()
  except MySQLdb.Error, e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
  finally:
    db.close()



def connect_mysql():
    db_config = dict(host="localhost", port=3307, db="BLOG", charset="utf8", user="root", passwd="8008208820")
    try:
        cnx = MySQLdb.connect(**db_config)
    except Exception as err:
        raise err
    return cnx


def get_message():
  # Address
  HOST = 'localhost'
  PORT = 4200
  # Prepare HTTP response
  text_content = '''HTTP/1.x 200 OK 
    Content-Type: text/html
    <head>
    <title>WOW</title>
    </head>
    <html>
    <p>Wow, Python Server</p>
    <IMG src="test.jpg"/>
    </html>
    '''
  # Read picture, put into HTTP format
  f = open('test.jpg', 'rb')
  pic_content = '''
    HTTP/1.x 200 OK 
    Content-Type: image/jpg
    '''
  pic_content = pic_content.bytes() + f.read()
  f.close()
  # Configure socket
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((HOST, PORT))
  # infinite loop, server forever
  while True:
    # 3: maximum number of requests waiting
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    method = request.split(' ')[0]
    src = request.split(' ')[1]
    # deal with GET method
    if method == 'GET':
      # ULR
      if src == '/test.jpg':
        content = pic_content
      else:
        content = text_content
      print ('Connected by', addr)
      print ('Request is:', request)
      conn.sendall(content.bytes())
    # close connection
    conn.close()

if __name__ == "__main__":
    get_message()
    # sql = "create table test(id int not null);"
    cnx = connect_mysql()  # 连接mysql
    cus = cnx.cursor()     # 创建一个游标对象    try:
    try:
        # cus.execute("DROP TABLE IF EXISTS User")
        # cus.execute(User)
        # cus.executemany(sql, param)
        cus.execute(searchUserName)
        result = cus.fetchall()
        for row in result:
            fid = row[0]
            fname = row[1]
            fpass = row[2]
            print('fid=%s,fname=%s,fpass=%s'%(fid, fname, fpass))
        cus.close()
        cnx.commit()
    except Exception as err:
        cnx.rollback()
        raise err
    finally:
        cnx.close()



