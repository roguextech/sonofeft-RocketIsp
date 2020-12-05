#!/usr/bin/env python
# -*- coding: ascii -*-
from __future__ import print_function

# NOTICE... this file is generated by TkGridGUI.
# Any code or comments added by the user must be in designated areas ONLY.
# User additions will be lost if they are placed in code-generated areas.
# (i.e. Saving from TkGridGUI will over-write code-generated areas.)

# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "imports"


from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import str
from builtins import range
from builtins import object

from tkinter.ttk import Combobox, Progressbar, Separator, Treeview, Notebook

from tkinter import *
from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, LabelFrame
from tkinter import Listbox, Message, Radiobutton, Spinbox, Text
from tkinter import OptionMenu
import tkinter.filedialog
from tkinter import _setit as set_command


# >>>>>>insert any user code below this comment for section "imports"
# Place any user import statements here
import os
# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "top_of_init"

if sys.version_info < (3,):
    from tkSimpleDialog import Dialog
else:
    from tkinter.simpledialog import Dialog

class _Dialog(Dialog):
    # use dialogOptions dictionary to set any values in the dialog
    def __init__(self, parent, title = None, dialogOptions=None):
    
        self.dialogOptions = dialogOptions
        Dialog.__init__(self, parent, title)

class _select_recent_file(_Dialog):

    def body(self, master):
        dialogframe = Frame(master, width=248, height=293)
        self.dialogframe = dialogframe
        dialogframe.pack()


        self.make_Label_1( self.dialogframe )          #       Label: Select Recent File : at Main(1,1)
        self.make_Label_2( self.dialogframe )          #       Label:  at Main(2,1)
        self.make_Listbox_1( self.dialogframe )        #     Listbox:  at Main(3,1)


        
        # make a Status Bar
        self.statusMessage = StringVar()
        self.statusMessage.set("")
        self.statusbar = Label(self.dialogframe, textvariable=self.statusMessage, bd=1, relief=SUNKEN)
        self.statusbar.grid(row=99, column=0, columnspan=99, sticky='ew')


        # >>>>>>insert any user code below this comment for section "top_of_init"


        self.statusMessage.set("Select File from Recent List")

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_1"
    def make_Label_1(self, frame):
        """       Label: Select Recent File : at Main(1,1)"""
        self.Label_1 = Label( frame , text="Select Recent File", width="30")
        self.Label_1.grid(row=1, column=1)

        # >>>>>>insert any user code below this comment for section "make_Label_1"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_2"
    def make_Label_2(self, frame):
        """       Label:  at Main(2,1)"""
        self.Label_2 = Label( frame , text="", width="30")
        self.Label_2.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Label_2"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Listbox_1"
    def make_Listbox_1(self, frame):
        """     Listbox:  at Main(3,1)"""

        lbframe = Frame( frame )
        self.Listbox_1_frame = lbframe
        vbar=Scrollbar(lbframe, orient=VERTICAL)
        self.Listbox_1 = Listbox(lbframe, width="30", height="12", yscrollcommand=vbar.set)
        vbar.config(command=self.Listbox_1.yview)
        
        vbar.grid(row=0, column=1, sticky='ns')        
        self.Listbox_1.grid(row=0, column=0)

        self.Listbox_1_frame.grid(row=3, column=1)

        # >>>>>>insert any user code below this comment for section "make_Listbox_1"
        
        self.input_fileL = [] # list of (head, tail)

        # Edit the Listbox Entries
        self.Listbox_1.configure( exportselection=False ) # stay highlighted after focus leaves
        for i,name in enumerate(self.dialogOptions['fileL']):
            head, tail = os.path.split( name )
            self.input_fileL.append( (head, tail) )
            self.Listbox_1.insert(END, tail)

        self.Listbox_1.bind("<ButtonRelease-1>", self.Listbox_1_Click)
        self.Listbox_1.bind('<Double-1>', self.double_click) # bind double left clicks

        self.Listbox_1.bind('<Enter>',  self.snapHighlightToMouse)
        self.Listbox_1.bind('<Motion>', self.snapHighlightToMouse)
        self.Listbox_1.bind('<Leave>',  self.unhighlight)


    def snapHighlightToMouse(self, event):
        #self.Listbox_1.selection_clear(0, END)
        #self.Listbox_1.selection_set( self.Listbox_1.nearest(event.y) )
        #print( self.Listbox_1.get( self.Listbox_1.nearest(event.y) ), self.Listbox_1.nearest(event.y) )
        
        self.statusMessage.set( self.input_fileL[self.Listbox_1.nearest(event.y)][0] )
        

    def unhighlight(self, event=None):
        #self.Listbox_1.selection_clear(0, END)
        pass
        
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Listbox_1_Click"
    def Listbox_1_Click(self, event): #bind method for component ID=Listbox_1
        """     Listbox:  at Main(3,1)"""
        pass
        # >>>>>>insert any user code below this comment for section "Listbox_1_Click"
        # replace, delete, or comment-out the following
        #print( "executed method Listbox_1_Click" )
        #print(event)

        #print( "current selection(s) =",self.Listbox_1.curselection() )
        labelL = []
        isel = -1
        for i in self.Listbox_1.curselection():
            isel = i
            labelL.append( self.Listbox_1.get(i))
        #print( "current label(s) =",labelL )
        
        if isel >= 0:
            self.Label_1.config(text=self.input_fileL[isel][0])
            self.Label_2.config(text=self.input_fileL[isel][1])
    
    def double_click(self, event):
        self.Listbox_1_Click( event )
        self.ok()
        
    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "dialog_validate"
    def validate(self):
        self.result = {} # return a dictionary of results
    


        # >>>>>>insert any user code below this comment for section "dialog_validate"
        # set values in "self.result" dictionary for return
        # for example...
        # self.result["age"] = self.Entry_2_StringVar.get() 
        self.result["file_name"] = ''
        for i in self.Listbox_1.curselection():
            self.result["file_name"] = self.dialogOptions['fileL'][i]
            break
            
        return 1
    """
    Use this for testing dialog
        fileL = ['c:/myhome/file 1', 'd:/really/deep/path/to/file/Really_Important_File','e:/yesterdays/news/YesterdayAtNoon']
        for i in range(30):
            fileL.append('f:/dummy%i/area%i/Dummy_File_%i'%(i,i,i) + 'x'*i)
        dialog = _select_recent_file(self.master, "Pick Recent File", dialogOptions={'fileL':fileL})
    
    """
        
        
# TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "end"


    def apply(self):
        pass
        #print( 'apply called' )

class _Testdialog:
    def __init__(self, master):
        frame = Frame(master, width=300, height=300)
        frame.pack()
        self.master = master
        self.x, self.y, self.w, self.h = -1,-1,-1,-1
        
        self.Button_1 = Button(text="Test Dialog", relief="raised", width="15")
        self.Button_1.place(x=84, y=36)
        self.Button_1.bind("<ButtonRelease-1>", self.Button_1_Click)

    def Button_1_Click(self, event): #click method for component ID=1
        fileL = ['c:/myhome/file 1', 'd:/really/deep/path/to/file/Really_Important_File','e:/yesterdays/news/YesterdayAtNoon']
        for i in range(30):
            fileL.append('f:/dummy%i/area%i/Dummy_File_%i'%(i,i,i) + 'x'*i)
        dialog = _select_recent_file(self.master, "Pick Recent File", dialogOptions={'fileL':fileL})
        print( '===============Result from Dialog====================' )
        print( dialog.result )
        print( '=====================================================' )

def main():
    root = Tk()
    app = _Testdialog(root)
    root.mainloop()

if __name__ == '__main__':
    main()