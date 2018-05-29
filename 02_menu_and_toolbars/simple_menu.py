#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# simple_menu.py

import wx

class ExampleMenu(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(ExampleMenu, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

        self.SetSize((300, 200))
        self.SetTitle('Simple Menu')
        self.Centre()

    def OnQuit(self, e):        
        self.Close()


def main():
    app = wx.App()
    ex = ExampleMenu(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
