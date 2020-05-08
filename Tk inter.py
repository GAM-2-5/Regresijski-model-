from tkinter import *
import requests

root = Tk()
root.title("Prediktor cijene dionica")
label1=Label(root, text= "Puno ime kompanije :",borderwidth=5, relief="groove",fg= 'deep sky blue')

e = Entry(root, width=35,borderwidth=5, bg= "white",fg= "blue",)

e.grid(row=0, column=1, padx=10, pady=10)




a= ""                                                
def klik ():
    global a 
    a= e.get()

   
gumb= Button(root,text="Click for graph", padx=100, pady= 25,command=klik, fg= 'blue', bg='sky blue')



































if __name__=="__klik__":
    klik()
def get_symbol(symbol):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

    result = requests.get(url).json()

    for x in result['ResultSet']['Result']:
        if x['name'] == symbol:
            return x['symbol']
label1.grid(row=0,column=0)

gumb.grid(row=2,sticky=N+S+E+W,columnspan=2)


root.mainloop()

e=get_symbol(a)


