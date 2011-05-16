#-*- coding: utf-8 -*-
'''
Created on 16.05.2011

@author: dik
'''

import pygtk
pygtk.require('2.0')
import gtk


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
        print "1"
        

if __name__ == '__main__':
    pr = MainForm()
    pr.main()