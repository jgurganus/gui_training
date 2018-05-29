#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# submenu.py

import wx

APP_EXIT = 1

class ExampleSubMenu(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(ExampleSubMenu, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, '&New') 
        fileMenu.Append(wx.ID_OPEN, '&Open') 
        fileMenu.Append(wx.ID_SAVE, '&Save') 
        fileMenu.AppendSeparator()

        imp  = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import newsfeed list...') 
        imp.Append(wx.ID_ANY, 'Import bookmarks...') 
        imp.Append(wx.ID_ANY, 'Import mail...') 
        
        fileMenu.Append(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT,'&Quit\tCtrl+W')
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Submenu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = ExampleSubMenu(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
