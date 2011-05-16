#-*- coding: utf-8 -*-
'''
Created on 17.05.2011

@author: dik
'''

import sqlite3
import hashlib
import os.path

class DBConn(object):
    '''
    Класс для работы со встроеной БД
    '''
    conn = None
    cur = None


    def __init__(self):
        '''
        Конструктор создает базу данных, назначает коннект и курсор
        '''
        if not self.db_exists("maindb.sqlite"):
            """Код для создания БД"""
            self.conn = sqlite3.connect("maindb.sqlite")
            self.cur = self.conn.cursor()
            self.cur.execute("""CREATE TABLE users (id INTEGER PRIMARY KEY ASC, login TEXT, password TEXT)""")
            self.cur.execute('INSERT INTO users values (0, "admin", ?)', (str(hashlib.md5("admin").hexdigest()),))
            self.conn.commit()
        else:
            self.conn = sqlite3.connect("maindb.sqlite")
            self.cur = self.conn.cursor()
        
    def db_exists(self, filename):
        return os.path.exists(filename)
    
if __name__ == "__main__":
    f = DBConn()