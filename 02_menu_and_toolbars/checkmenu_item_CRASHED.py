#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# checkmenu_item.py

import wx

APP_EXIT = 1

class ExampleCheckMenuItem(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(ExampleCheckMenuItem, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        menubar = wx.MenuBar()
        viewMenu = wx.Menu()

        self.showStatusBar = viewMenu.Append(wx.ID_ANY,
                                             'Show statusbar',
                                             'Show Statusbar',
                                             kind=wx.ITEM_CHECK)
        self.showToolBar = viewMenu.Append(wx.ID_ANY,
                                           'Show toolbar',
                                           'Show Toolbar',
                                           kind=wx.ITEM_CHECK)

        viewMenu.Check(self.showStatusBar.GetId(), True)
        viewMenu.Check(self.showToolBar.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.showStatusBar)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.showToolBar)

        menubar.Append(viewMenu, '&View')
        self.SetMenuBar(menubar)

        self.toolBar = self.CreateToolBar()
        self.toolBar.AddTool(1, '', wx.Bitmap('texit.png'))
        self.toolBar.Realize()

        self.statusBar = self.CreateStatusBar()
        self.statusBar.SetStatusText('Ready')
        
        self.SetSize((550, 350))
        self.SetTitle('Check menu item')
        self.Centre()

    def ToggleStatusBar(self, e):
        if self.showStatusBar.IsChecked():
            self.statusBar.Show()
        else:
            self.statusBar.Hide()

    def ToggleToolBar(self, e):
        if self.showToolBar.IsChecked():
            self.toolBar.Show()
        else:
            self.toolBar.Hide()


def main():
    app = wx.App()
    ex = ExampleCheckMenuItem(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
