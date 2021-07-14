from tkinter import *
import random

root = Tk()
root.geometry("779x536")
root.title("seizure app")

col = {"colours" : ["cyan", "turquoise", "DeepSkyBlue2", "hot pink", "red2", "gold"]}

def yeeeyeyeyeyeyeyeyee() :
    bdwhk = random.randint(0, 5)
    ehb = str(col["colours"][bdwhk])
    print(ehb)
    root.configure(background = ehb)


btn = Button(root, text="Click here!!",command=yeeeyeyeyeyeyeyeyee)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
