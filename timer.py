import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()

root.title("Timer")
root.geometry("250x200")


hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()
        
hour.set("00")
minute.set("00")
second.set("00")

timeframe = tk.Frame(root)

hourentry = tk.Entry(timeframe, width=2, font=("Arial, 18"), textvariable=hour)
hourentry.grid(row=0, column=0)
minuteentry = tk.Entry(timeframe, width=2, font=("Arial, 18"), textvariable=minute)
minuteentry.grid(row=0, column=1)
secondentry = tk.Entry(timeframe, width=2, font=("Arial, 18"), textvariable=second)
secondentry.grid(row=0, column=2)

timeframe.pack(fill='x')

root.update()

btn = tk.Button(root, text="Start", font=("Arial, 20"))
btn.pack(pady= 60)
root.mainloop()