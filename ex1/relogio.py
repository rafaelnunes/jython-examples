# -*- coding: utf-8 -*-
'''
Created on May 18, 2012

@author: Rafael Nunes
'''

from javax.swing import *
from java.awt import Font
from time import strftime

class Clock(JFrame):
    def __init__(self):
        JFrame.__init__(self, u'TicTac', defaultCloseOperation=JFrame.DISPOSE_ON_CLOSE)
        self.mostrador = JLabel('00:00:00', font=Font('Sanserif', Font.BOLD, 70))
        self.contentPane.add(self.mostrador)
        self.pack()
        self.visible = True
        
    def start(self):
        def tic(evento):
            now = strftime('%H:%M:%S')
            if self.mostrador.text != now:
                self.mostrador.text = now
        Timer(100, tic).start()

if __name__ == '__main__':
    rel = Clock()
    rel.start()
