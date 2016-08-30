# -*- coding: utf-8 -*-

import tkinter
import tkinter.scrolledtext as tkst
import urllib
import urllib.parse
from tkinter import *
from tkinter import ttk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.pack()
        self.grid(sticky='nswe')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # 新建两个TAB页
        self.nRoot = ttk.Notebook(self)
        one2N_Frame = ttk.Frame(self.nRoot)
        one2one_Frame = ttk.Frame(self.nRoot)
        self.nRoot.add(one2N_Frame, text='1转多')
        self.nRoot.add(one2one_Frame, text='1转1')
        self.nRoot.rowconfigure(0, weight=1)
        self.nRoot.columnconfigure(0, weight=1)
        self.nRoot.grid(row=0, column=0, sticky='nswe', ipady=3, ipadx=3)
        one2N_Frame.rowconfigure(0, weight=1)
        one2N_Frame.columnconfigure(0, weight=1)
        one2one_Frame.rowconfigure(0, weight=1)
        one2one_Frame.columnconfigure(0, weight=1)
        # 第一个TAB页
        # 原始文本
        ttk.Label(one2N_Frame, text='原始文本：').grid(sticky=E)
        self.oriText = tkst.ScrolledText(one2N_Frame, height=5)
        self.oriText.grid(row=0, column=1)
        ttk.Button(one2N_Frame, text='给我转', command=self.runTrans).grid(row=0, column=2, padx=15)
        # URL编码
        ttk.Label(one2N_Frame, text='URL编码：').grid(sticky=E)
        self.urlText = tkst.ScrolledText(one2N_Frame, height=5)
        self.urlText.grid(row=1, column=1)
        # 16进制编码
        ttk.Label(one2N_Frame, text='16进制编码：').grid(sticky=E)
        self.hexText = tkst.ScrolledText(one2N_Frame, height=5)
        self.hexText.grid(row=2, column=1)
        # ASCII编码
        ttk.Label(one2N_Frame, text='ASCII编码：').grid(sticky=E)
        self.asciiText = tkst.ScrolledText(one2N_Frame, height=5)
        self.asciiText.grid(row=3, column=1)
        # MD5_16编码
        ttk.Label(one2N_Frame, text='MD5_16编码：').grid(sticky=E)
        self.md5_16Text = tkst.ScrolledText(one2N_Frame, height=5)
        self.md5_16Text.grid(row=4, column=1)
        # MD5_32编码
        ttk.Label(one2N_Frame, text='MD5_32编码：').grid(sticky=E)
        self.md5_32Text = tkst.ScrolledText(one2N_Frame, height=5)
        self.md5_32Text.grid(row=5, column=1)
        # BASE64编码
        ttk.Label(one2N_Frame, text='BASE64编码：').grid(sticky=E)
        self.base64Text = tkst.ScrolledText(one2N_Frame, height=5)
        self.base64Text.grid(row=6, column=1)


        # 第二个TAB页

    # 消息处理函数
    # 1toN转换
    def runTrans(self):
        s_oriText = self.oriText.get(1.0, END).lstrip().rstrip()
        # url编码
        self.urlText.delete(1.0, END)
        self.urlText.insert(END, urllib.parse.quote_plus(s_oriText))


# End Class Application--------------------------------------------------------------------------------------------------

def main():
    root = tkinter.Tk()
    #f = tkFont.Font(family='Helvetica', size=10)
    #s = ttk.Style()
    #s.theme_use('clam')
    #s.configure('.', font=f)
    app = Application(master=root)
    app.master.title('CodeMagic V0.1 Build20160830')
    app.master.columnconfigure(0, weight=1)
    app.master.rowconfigure(0, weight=1)
    # app.master.maxsize(1000, 4000)
    app.master.resizable(True, False)
    app.mainloop()


#End main function------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()