# -*- coding: utf-8 -*-

from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
import tkinter

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.grid(sticky='nswe')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        # 新建两个TAB页
        self.nRoot = ttk.Notebook(self)
        BuilderFrame = ttk.Frame(self.nRoot)
        WatchLog = ttk.Frame(self.nRoot)
        self.nRoot.add(BuilderFrame, text='1转多')
        self.nRoot.add(WatchLog, text='1转1')
        self.nRoot.rowconfigure(0, weight=1)
        self.nRoot.columnconfigure(0, weight=1)
        self.nRoot.grid(row=0, column=0, sticky='nswe', ipady=3, ipadx=3)
        BuilderFrame.rowconfigure(0, weight=1)
        BuilderFrame.columnconfigure(0, weight=1)
        WatchLog.rowconfigure(0, weight=1)
        WatchLog.columnconfigure(0, weight=1)
        # 第一个TAB页



        # 第二个TAB页
#End Class -------------------------------------------------------------------------------------------------------------


    # Targets:

def main():
    root = tkinter.Tk()
    #f = tkFont.Font(family='Helvetica', size=10)
    #s = ttk.Style()
    #s.theme_use('clam')
    #s.configure('.', font=f)
    root.title('CodeMagic V0.1 Build20160830')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.resizable(True, False)
    app = Application(master=root)
    app.mainloop()

# -----------------------------------------
if __name__ == '__main__':
    main()