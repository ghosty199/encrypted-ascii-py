
from tkinter import*
root=Tk()
root.geometry("400x400")
root.title("ASCII CONVERTER")
root.configure(background="white")
enterword=Entry(root)
enterword.place(relx=0.5,rely=0.5,anchor=CENTER)
label1=Label(root,text="ASCII=")
label1.place(relx=0.5, rely=0.6, anchor=CENTER)
label2=Label(root)
label2.place(relx=0.5, rely=0.7, anchor=CENTER)
label3=Label(root,text="as encrypted word=")
label3.place(relx=0.5, rely=0.3, anchor=CENTER)

def ASCII():
    input1=enterword.get()
    for letter in input1:
        greg=ord(letter)+1
        character=chr(greg)
        label2["text"]=label2["text"]+str(greg)+" "
        label3["text"]=label3["text"]+str(character)
button1=Button(root,text="ASCII",command=ASCII)
button1.place(relx=0.5, rely=0.8, anchor=CENTER)


























root.mainloop()