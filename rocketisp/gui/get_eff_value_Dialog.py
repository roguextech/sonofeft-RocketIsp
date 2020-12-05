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
import tkinter.messagebox

from tkinter import *
from tkinter import Button, Canvas, Checkbutton, Entry, Frame, Label, LabelFrame
from tkinter import Listbox, Message, Radiobutton, Spinbox, Text
from tkinter import OptionMenu
import tkinter.filedialog
from tkinter import _setit as set_command


# >>>>>>insert any user code below this comment for section "imports"
# Place any user import statements here
from rocketisp.cast import floatCast, is_float, is_int, intCast

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

class _get_eff_value(_Dialog):

    def body(self, master):
        dialogframe = Frame(master, width=426, height=213)
        self.dialogframe = dialogframe
        dialogframe.pack()


        self.RadioGroup_1_StringVar = StringVar()

        self.make_Entry_1( self.dialogframe )          #       Entry:  at Main(3,2)
        self.make_Label_1( self.dialogframe )          #       Label: Input XXX Value : at Main(1,1)
        self.make_Label_2( self.dialogframe )          #       Label: definition : at Main(2,1)
        self.make_Label_3( self.dialogframe )          #       Label: XXX= : at Main(3,1)
        self.make_RadioGroup_1( self.dialogframe )     #  RadioGroup: XXX= : at Main(4,1)
        self.make_Radiobutton_1( self.RadioGroup_1 )   # Radiobutton: True : at RadioGroup_1(2,1)
        self.make_Radiobutton_2( self.RadioGroup_1 )   # Radiobutton: False : at RadioGroup_1(3,1)


        self.RadioGroup_1_StringVar.set("1")
        self.RadioGroup_1_StringVar_traceName = self.RadioGroup_1_StringVar.trace_variable("w", self.RadioGroup_1_StringVar_Callback)
        # >>>>>>insert any user code below this comment for section "top_of_init"
        
        if self.dialogOptions['val_type'] == True:
            self.RadioGroup_1_StringVar.set("1")
        else:
            self.RadioGroup_1_StringVar.set("2")
            
        self.Entry_1.focus_set()
        self.Entry_1.select_range(0, END)


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Entry_1"
    def make_Entry_1(self, frame):
        """       Entry:  at Main(3,2)"""
        self.Entry_1 = Entry( frame , width="30")
        self.Entry_1.grid(row=3, column=2, sticky="w", columnspan="1")
        self.Entry_1_StringVar = StringVar()

        # >>>>>>insert any user code below this comment for section "make_Entry_1"
        value = self.dialogOptions.get('value', '')
        self.Entry_1_StringVar.set( value )

        self.Entry_1.configure(textvariable=self.Entry_1_StringVar)
        self.Entry_1_StringVar_traceName = self.Entry_1_StringVar.trace_variable("w", self.Entry_1_StringVar_Callback)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_1"
    def make_Label_1(self, frame):
        """       Label: Input XXX Value : at Main(1,1)"""
        self.Label_1 = Label( frame , text="Input XXX Value", width="60")
        self.Label_1.grid(row=1, column=1, columnspan="2")

        # >>>>>>insert any user code below this comment for section "make_Label_1"
        name = self.dialogOptions.get('label', '')
        if not name:
            name = self.dialogOptions.get('name', '')
        self.Label_1.configure( text='Input: '+name+' Efficiency' )


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_2"
    def make_Label_2(self, frame):
        """       Label: definition : at Main(2,1)"""
        self.Label_2 = Label( frame , text="definition", width="60", height="4")
        self.Label_2.grid(row=2, column=1, columnspan="2")

        # >>>>>>insert any user code below this comment for section "make_Label_2"
        desc = self.dialogOptions.get('desc', '')
        self.Label_2.configure( text=desc, wraplength=400 )


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Label_3"
    def make_Label_3(self, frame):
        """       Label: XXX= : at Main(3,1)"""
        self.Label_3 = Label( frame , text="XXX=", width="20", anchor="e")
        self.Label_3.grid(row=3, column=1, sticky="e")

        # >>>>>>insert any user code below this comment for section "make_Label_3"
        name = self.dialogOptions.get('name', '')
        self.Label_3.configure( text=name+'=' )


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_RadioGroup_1"
    def make_RadioGroup_1(self, frame):
        """  RadioGroup: XXX= : at Main(4,1)"""
        self.RadioGroup_1 = LabelFrame( frame , width="60", height="50", text="XXX=")
        self.RadioGroup_1.grid(row=4, column=1, columnspan="2")

        # >>>>>>insert any user code below this comment for section "make_RadioGroup_1"
        name = self.dialogOptions.get('label', '')
        if not name:
            name = self.dialogOptions.get('name', '')
        self.RadioGroup_1.configure( text='Const: '+name+' Efficiency???' )


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_1"
    def make_Radiobutton_1(self, frame):
        """ Radiobutton: True : at RadioGroup_1(2,1)"""
        self.Radiobutton_1 = Radiobutton( frame , value="1", text="Is Constant", width="15", anchor="w")
        self.Radiobutton_1.grid(row=2, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_1"

        self.Radiobutton_1.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "make_Radiobutton_2"
    def make_Radiobutton_2(self, frame):
        """ Radiobutton: False : at RadioGroup_1(3,1)"""
        self.Radiobutton_2 = Radiobutton( frame , value="2", text="Calculated", width="15", anchor="w")
        self.Radiobutton_2.grid(row=3, column=1)

        # >>>>>>insert any user code below this comment for section "make_Radiobutton_2"

        self.Radiobutton_2.configure(variable=self.RadioGroup_1_StringVar)

    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "Entry_1_StringVar_traceName"
    def Entry_1_StringVar_Callback(self, varName, index, mode):
        """       Entry:  at Main(3,2)"""
        pass

        # >>>>>>insert any user code below this comment for section "Entry_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "Entry_1_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.Entry_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "RadioGroup_1_StringVar_traceName"
    def RadioGroup_1_StringVar_Callback(self, varName, index, mode):
        """  RadioGroup: XXX= : at Main(4,1)"""
        pass

        # >>>>>>insert any user code below this comment for section "RadioGroup_1_StringVar_traceName"
        # replace, delete, or comment-out the following
        #print( "RadioGroup_1_StringVar_Callback varName, index, mode",varName, index, mode )
        #print( "    new StringVar value =",self.RadioGroup_1_StringVar.get() )



    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "standard_message_dialogs"

    # standard message dialogs... showinfo, showwarning, showerror
    def ShowInfo(self, title='Title', message='your message here.'):
        tkinter.messagebox.showinfo( title, message )
        return
    def ShowWarning(self, title='Title', message='your message here.'):
        tkinter.messagebox.showwarning( title, message )
        return
    def ShowError(self, title='Title', message='your message here.'):
        tkinter.messagebox.showerror( title, message )
        return
        
    # standard question dialogs... askquestion, askokcancel, askyesno, or askretrycancel
    # return True for OK, Yes, Retry, False for Cancel or No
    def AskYesNo(self, title='Title', message='your question here.'):
        return tkinter.messagebox.askyesno( title, message )
    def AskOK_Cancel(self, title='Title', message='your question here.'):
        return tkinter.messagebox.askokcancel( title, message )
    def AskRetryCancel(self, title='Title', message='your question here.'):
        return tkinter.messagebox.askretrycancel( title, message )
        
    # return "yes" for Yes, "no" for No
    def AskQuestion(self, title='Title', message='your question here.'):
        return tkinter.messagebox.askquestion( title, message )
    # END of standard message dialogs

    # >>>>>>insert any user code below this comment for section "standard_message_dialogs"


    # TkGridGUI generated code. DO NOT EDIT THE FOLLOWING. section "dialog_validate"
    def validate(self):
        self.result = {} # return a dictionary of results
    

        #self.result["Entry_1"] = self.Entry_1_StringVar.get()
        #self.result["RadioGroup_1"] = self.RadioGroup_1_StringVar.get()

        # >>>>>>insert any user code below this comment for section "dialog_validate"
        
        self.result["is_const"] = self.RadioGroup_1_StringVar.get() == '1'
        
        value = self.Entry_1_StringVar.get()
        try:
            value = eval( value )
        except:
            self.ShowError( title='Invalid Efficiency', message='"%s" NOT recognized as float\nPlease Try Again.'%value)
            return 0
        
        value = floatCast( value )
        
        if value>1.0 or value<0.0:
            self.ShowError( title='Invalid Efficiency', message='"%s" MUST be in range 0.0 to 1.0\nPlease Try Again.'%value)
            return 0

        self.result["return_value"] = value
        #print('Eff Dialog result =', self.result)
            
        return 1
    """
    # for testing, reinstate this code below
    def Button_1_Click(self, event): #click method for component ID=1
        desc = 'radius of curvature just downstream of throat (Rdownstream / Rthrt) this could be a very long description and we would just need to wrap it.'
        value = False
        dialog = _get_eff_value(self.master, "Test Dialog", 
                 dialogOptions={'name':'Area Ratio', 'value':value, 'desc':desc, 'val_type':type(value)})

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
        desc = 'Total Isp Efficiency.'
        value = 0.954321 #False
        dialog = _get_eff_value(self.master, "Test Dialog", 
                 dialogOptions={'name':'Isp', 'value':value, 'desc':desc, 
                                'val_type':type(value), 'is_const':False})
        print( '===============Result from Dialog====================' )
        print( dialog.result )
        print( '=====================================================' )

def main():
    root = Tk()
    app = _Testdialog(root)
    root.mainloop()

if __name__ == '__main__':
    main()