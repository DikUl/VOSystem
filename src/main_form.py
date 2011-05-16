#-*- coding: utf-8 -*-
'''
Created on 16.05.2011

@author: dik
'''

import pygtk
pygtk.require('2.0')
import gtk
import db_conn
import hashlib


class MainForm(gtk.Builder):
    """Просто главная форма"""

    def __init__(self):
        """Загрузка данных Glade v3.6"""
        super(MainForm, self).__init__()
        self.add_from_file("vosystem.glade")
        self.connect_signals(self)
        
    def main(self):
        gtk.main()
        
    """Много много функций закрытия"""
    def on_window1_destroy(self, _):
        gtk.main_quit()
        
    def on_button2_pressed(self, _):
        gtk.main_quit()
    
    def on_button2_activate(self, _):
        gtk.main_quit()
        
    def on_imagemenuitem5_activate(self, _):
        gtk.main_quit()
    """Закрытия кончились"""
    
    def on_login_button_clicked(self, _):
        """Обработчик залогинивания"""
        self.db = db_conn.DBConn()
        login = self.get_object("login_entry").get_text()
        password = self.get_object("password_entry").get_text()
        try:
            self.db.cur.execute("SELECT id, password FROM users WHERE login=?", (login,))
            id, crypted_password = self.db.cur.fetchone()
            if str(hashlib.md5(password).hexdigest()) == crypted_password:
                print "Authoraised"
            else:
                print "Not authoraised"
        except(TypeError):
            print "User does not exist"
        
        

if __name__ == '__main__':
    pr = MainForm()
    pr.main()