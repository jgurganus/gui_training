#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# moving.py

import wx

class ExampleMove(wx.Frame):
    
    def __init__(self, parent, title):
        super(ExampleMove, self).__init__(parent, title=title, size=(300, 200))
        self.Move((800, 250))

def main():
    app = wx.App()
    ex = ExampleMove(None, title='Moving')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
