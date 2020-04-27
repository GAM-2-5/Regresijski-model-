from tkinter import *

root = Tk()
a=[]
e = Entry(root, width=50, bg= "black",fg= "green", borderwidth="5")
e.pack()
e.insert(0,"Ime kompanije:")
def klik ():
    tekst= e.get()
    label= Label(root, text=tekst )
    label.pack()
gumb= Button(root,text="Click for graph", padx=25, pady= 25,command=klik, fg= 'blue', bg='green')
gumb.pack()

root.mainloop()
