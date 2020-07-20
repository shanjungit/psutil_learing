# -*- encoding: utf-8 -*-
"""
@File    : wx_python_learning.py
@Time    : 2020/7/15 0:40
@Author  : shanjun.li
@Email   : 739051127@qq.com
@Software: PyCharm
"""
# wxPython 快速入门， python写界面
import wx
"""
wxPython是基于Python的跨平台GUI扩展库，对wxWidgets（ C++ 编写）封装实现。
在GUI程序的开发中界面布局是很重要的部分，合理的页面布局能够给予用户良好的使用体验。
虽然在GUI的控件和窗口布局上可以使用坐标，但更多且更方便的是用sizer来布局。
"""





class Panel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent,id=-1)

        pass


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None,title=r'小信运维助手',size=(1000,600), style=wx.DEFAULT_FRAME_STYLE^wx.MAXIMIZE_BOX)
        self.DispPanel = Panel(self)

        # 创建显示区域面板
        self.DispPanel = Panel(self)

        # 创建参数区面板
        self.ParaPanel = wx.Panel(self,-1)

        # 创建Right面板
        self.CtrlPanel = wx.Panel(self,-1)
        self.HBoxPanel = wx.BoxSizer(wx.HORIZONTAL)
        self.HBoxPanel.Add(self.ParaPanel, proportion=1, border=2, flag=wx.EXPAND | wx.ALL)
        self.HBoxPanel.Add(self.DispPanel, proportion=4, border=2, flag=wx.EXPAND | wx.ALL)
        self.HBoxPanel.Add(self.CtrlPanel, proportion=1, border=2, flag=wx.EXPAND | wx.ALL)
        self.SetSizer(self.HBoxPanel)

class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = App()
    app.MainLoop()