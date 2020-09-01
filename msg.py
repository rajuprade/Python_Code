#!/usr/bin/python

import wx
class MainFrame(wx.Frame):
     def __init__(self):
         wx.Frame.__init__(self,None,wx.ID_ANY,title='hello world')
         self.buthello = wx.Button(self,wx.ID_ANY,label = 'hello')
         self.buthello.Bind(wx.EVT_LEFT_DOWN,self.helloevent)
         self.Show()
     def helloevent(self,event):
         msg = 'hello'
         msgbox = wx.MessageDialog(self,message = msg,style = wx.OK)
         if msgbox.ShowModal() == wx.ID_OK:
              msgbox.Destroy()

app = wx.App(redirect=False)
frame = MainFrame()
app.MainLoop()

