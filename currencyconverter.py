from tkinter import *
import requests
import json

usdrequest= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/usd/")
usddata = usdrequest.json()
usd = usddata['rates'][0]['mid']

chfrequest= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/chf/")
chfdata = chfrequest.json()
chf = chfdata['rates'][0]['mid']

gbprequest= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/gbp/")
gbpdata = gbprequest.json()
gbp = gbpdata['rates'][0]['mid']

eurrequest= requests.get("http://api.nbp.pl/api/exchangerates/rates/a/eur/")
eurdata = eurrequest.json()
eur = eurdata['rates'][0]['mid']

print(usd,eur)

window = Tk()
window.title("Api converting price")
window.geometry("500x200")

info = Label(window,text="Enter the amount of PLN for conversion ",font=('Arial', 11, 'italic'),foreground='#000000')
info.pack()

entrybox= Entry()
entrybox.pack()

Usd = Label(window,text="")
Usd.pack()
Chf = Label(window,text="")
Chf.pack()
Gbp = Label(window,text="")
Gbp.pack()
Eur = Label(window,text="")
Eur.pack()
def converter():
    amount = float(entrybox.get())
 
    Usd.config(text=(round(amount/usd,2),"USD"))
    Chf.config(text=(round(amount/chf,2),"CHF"))
    Gbp.config(text=(round(amount/gbp,2),"GBP"))
    Eur.config(text=(round(amount/eur,2),"EUR"))

button = Button(text="CONVERT", command=converter)
button.pack()
window.mainloop()