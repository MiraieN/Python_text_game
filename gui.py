from tkinter import *
#
win = Tk()
win.title("Temperature converter")
win.configure(bg='lightyellow')


# move window center
winWidth, winHeight = win.winfo_reqwidth(), win.winfo_reqheight()   # taking win params
posWidth = int(win.winfo_screenwidth() / 2 - winWidth / 2)  # taking int only
posHeight = int(win.winfo_screenheight() / 2 - winHeight / 2)
win.geometry(f"+{posWidth}+{posHeight}")
win.geometry('400x185')

nameLabel = Label(text="Input ur grads").pack()

nameEntry = Entry(win)

nameEntry.pack()

def cels_button():
    global result
    grads = int(nameEntry.get())
    result = (grads - 32) * 5 / 9
    resultText.config(state='normal')
    resultText.delete('1.0', END)
    resultText.insert(END, f'{int(result)} Celcius')
    # pass


def fars_button():
    global result
    grads = int(nameEntry.get())
    result = grads * 9 / 5 + 32
    resultText.config(state='normal')
    resultText.delete('1.0', END)
    resultText.insert(END, f'{int(result)} Farengeits')
    # pass


resultText = Text(win, state='disabled', background='lightyellow', width=15, height=0)
resultText.pack(pady=5)

toCel = Button(win, text="To Celcius", highlightcolor='yellow', command=cels_button).pack(pady=10)
toFar = Button(win, text="To Farengeits", highlightcolor='yellow', command=fars_button).pack(pady=10)



win.mainloop()  # calls win
