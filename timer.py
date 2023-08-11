import tkinter as tk
from tkinter import messagebox
import time

#functions
def submit():
    try:       #exception check
        temp = (int(hour.get())*3600) + (int(minute.get())* 60) + (int(second.get()))
    except:
        print("There is no value inputed")
    while temp > -1:
        mins,secs = divmod(temp, 60)     #converts minutes or seconds entered to hours
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo(title="Time's up!", message="The timer countdown has finished")
        
        temp -= 1

root = tk.Tk()

root.title("Timer")
root.geometry("250x150")
root.iconbitmap('Python-timer/favicon.ico')


hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()
        
hour.set("00")
minute.set("00")
second.set("00")

hourentry = tk.Entry(root, width=2, font=("Arial, 18"), textvariable=hour)
hourentry.pack(side='left', expand=True)
minuteentry = tk.Entry(root, width=2, font=("Arial, 18"), textvariable=minute)
minuteentry.pack(side='left', expand=True)
secondentry = tk.Entry(root, width=2, font=("Arial, 18"), textvariable=second)
secondentry.pack(side='left', expand=True)

btn = tk.Button(root, text="Start", font=("Arial, 20") , command=submit)
btn.pack(expand=True)
root.mainloop()


        


