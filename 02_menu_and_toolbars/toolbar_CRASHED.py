#!/usr/bin/env pythonw
#-*- coding: utf-8 -*-

# toolbar.py

import wx


class ExampleToolbar(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(ExampleToolbar, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        toolbar = self.CreateToolBar()
        qtool = toolbar.AddTool(wx.ID_ANY, 'Quit', wx.Bitmap('texit.png'))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetSize((350, 250))
        self.SetTitle('Simple toolbar')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = ExampleToolbar(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
