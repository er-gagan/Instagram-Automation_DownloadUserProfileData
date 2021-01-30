from tkinter import *
from PIL import Image, ImageTk
import instaloader
import requests

root = Tk()
root.geometry("780x270")
root.resizable(0,0)

root.title("Instagram Automation")

photo = PhotoImage(file = "./ico.png")
root.iconphoto(False,photo)

UserName = StringVar()

def downLoad(ProfileName):
    instance = instaloader.Instaloader()
    instance.download_profile(profile_name=ProfileName)

def Check():
    ProfileName = UserName.get()
    response = requests.get("https://instagram.com/" + ProfileName + "/")
    mark = 0
    global b1
    if response.status_code == 404 :
        msg = f'''Username is not exist on instagram
        Please rewrite username carefully!'''
        l1.config(text=msg)
        mark = 1
    else:
        Label(root,text="", font=("Calibri",15)).place(x=100,y=150)
        msg = f'''Username is exist on instagram'''
        l1.config(text=msg)
        btnMsg = f'''Click here to download all data for {ProfileName} user'''
        b1 = Button(root,text=btnMsg,font=("Calibri",14),bd=5,width=50,command=lambda: downLoad(ProfileName))
        b1.place(x=50,y=200)
        
    if mark==1:
        b1.destroy()

im3 = Image.open("./insta.png")
im3 = im3.resize((100,100))
thumimage3 = ImageTk.PhotoImage(im3)
label3 = Label(root, image=thumimage3)
label3.place(x=50,y=5)

Label(root,text="Download Instagram User Profile Data",font=("Calibri",28)).place(x=150,y=26)

Label(root,text="Enter Username",font=("Calibri",15)).place(x=20,y=104)
e1 = Entry(root,width=40,font=("Calibri",15),bd=5,textvariable=UserName)
e1.focus()
e1.place(x=180,y=103)

Button(root,text="Check",font=("Calibri",13),bd=5, width=12, command=Check).place(x=620,y=100)

l1 = Label(root, font=("Calibri",15))
l1.place(x=110,y=160)
root.mainloop()