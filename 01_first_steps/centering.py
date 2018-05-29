#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# centering.py

import wx

class ExampleCenter(wx.Frame):
    
    def __init__(self, parent, title):
        super(ExampleCenter, self).__init__(parent, title=title,
                                            size=(300, 200))
        self.Centre()

def main():
    app = wx.App()
    ex = ExampleCenter(None, title='Centering')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
