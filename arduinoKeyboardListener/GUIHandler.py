import tkinter as tk

testVar = True

def GUISetup():
    window = tk.Tk()
    window.geometry('350x350')
    window.title("Fake Streamdeck")

    global greeting
    greeting = tk.Label(text="Hello, tKinter")
    greeting.grid(column=2, row=0)
    # greeting.pack()

    btn = tk.Button(window, text="Click me", command=clicked)
    btn.grid(column=0, row=0)
    # btn.pack()

    txt = tk.Entry(window, width=10)
    txt.grid(column=1, row=0)

    tk.mainloop()

def clicked():
    greeting.configure(text="Button was clicked!!")
    testVar = False