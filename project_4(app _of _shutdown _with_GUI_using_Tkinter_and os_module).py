from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")
    
def shutdown():
    os.system("shutdown /s /t 1")
    
def restart_after_20_seconds():
    os.system("shutdown /r /t 20")
    
def signout():
    os.system("shutdown -l")


app = Tk()
app.title("Control PC")
app.geometry("700x700")
app.config(bg="black")

restart_button = Button(app, text = "Restart", font = ("Time New Roman",50,"bold"),bg="red", relief = RAISED, cursor = "plus",command=restart)
restart_button.place(x=210,y=100,height=70,width=250)

shutdown_button = Button(app, text = "Shutdown", font = ("Time New Roman",35,"bold"),bg="red", relief = RAISED, cursor = "plus",command=shutdown)
shutdown_button.place(x=210,y=225,height=70,width=250)

logout_button = Button(app, text = "Signout", font = ("Time New Roman",45,"bold"),bg="red", relief = RAISED, cursor = "plus",command=signout)
logout_button.place(x=210,y=350,height=70,width=250)

sleep_with_time_button = Button(app, text = "Restart After 20 seconds",bg="red", font = ("Time New Roman",25,"bold"), relief = RAISED, cursor = "plus",command= restart_after_20_seconds)
sleep_with_time_button.place(x=140,y=475,height=70,width=400)


app.mainloop()