from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
##
messagebox.askyesno("Question1", "Copying all files", icon='question')
