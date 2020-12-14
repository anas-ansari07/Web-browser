import tkinter as tk
import webbrowser
#main window
root = tk.Tk()
root.geometry("400x150")
root.title("My Webbrowser")

x=tk.StringVar()

#functions
def fbook():
    webbrowser.open_new("www.facebook.com")
    
def yt():
    webbrowser.open_new("www.youtube.com")
    
def Ig():
    webbrowser.open_new("www.instagram.com")
    
def tw():
    webbrowser.open_new("www.twitter.com")
    
def go():
    webbrowser.open_new("www.google.com")
    
def find():
    word = x.get()
    search = "https://www.google.com/search?q=" + word
    webbrowser.open_new(search)
    
#button
b1=tk.Button(root,text="Facebook",font="arial",bd=1,fg="white",relief="groove",bg="#3b5998",activeforeground="yellow" ,command=fbook)
b1.place(x=10, y=70, width=80,height=30)


b2=tk.Button(root,text="Youtube",font="arial",bd=1,fg="white",relief="groove", bg="#FF0000", command=yt)
b2.place(x=100,y=70,width=80,height=30)


b3=tk.Button(root,text="Instagram",font="arial",bd=1,relief="groove", fg="white", bg="#C13584",command=Ig)
b3.place(x=190,y=70,width=80,height=30)

b4=tk.Button(root,text="Twitter",font="arial",bd=1,relief="groove", fg="white", bg="#00acee", command=tw)
b4.place(x=10,y=105,width=135,height=30)

b5=tk.Button(root,text="Google",font="arial",bd=1,relief="groove", fg="white", bg="#db3236",command=go)
b5.place(x=155,y=105,width=135,height=30)

b6=tk.Button(root,text="Search",font="arial",bd=2,relief="solid",fg="blue",bg="white", command=find)
b6.place(x=320,y=10,width=70,height=40)

e1=tk.Entry(root,textvariable=x,relief="groove",cursor="dot",bd=3,highlightcolor="red")
e1.place(x=30,y=10,width=220,height=40)

#close window
root.mainloop()