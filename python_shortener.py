import pyperclip
import pyshorteners
from tkinter import*

root = Tk()
root.geometry("400x200")
root.title("URL SHORTENER")
root.configure(bg = "#49A")
url =StringVar()
url_address =   StringVar()


def urlshortener():
    url_address = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()  
    pyperclip.copy(url_short)  
Label(root,text = "my URL SHORTENER",font ="poppins").pack(pady= 10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text = "generate short url",command=urlshortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root,text="copy url",command= copyurl).pack(pady=5)   


root.mainloop()
