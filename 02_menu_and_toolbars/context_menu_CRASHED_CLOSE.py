#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# context_menu.py

import wx


class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()
        self.parent = parent

        minimizeMenuItem = wx.MenuItem(self, wx.NewId(), 'Minimize')
        self.Append(minimizeMenuItem)
        self.Bind(wx.EVT_MENU, self.OnMinimize, minimizeMenuItem)

        closeMenuItem = wx.MenuItem(self, wx.NewId(), 'Close')
        self.Append(closeMenuItem)
        self.Bind(wx.EVT_MENU, self.OnClose, closeMenuItem)
        
    def OnMinimize(self, e):
        self.parent.Iconize()
        
    def OnClose(self, e):
        self.parent.Close()


class ExampleContextMenu(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(ExampleContextMenu, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle('Context menu')
        self.Centre()

    def OnRightDown(self, e):
        self.PopupMenu(MyPopupMenu(self), e.GetPosition())


def main():
    app = wx.App()
    ex = ExampleContextMenu(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
