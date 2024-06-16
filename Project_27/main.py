import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(300, 200)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label_changed = tkinter.Label(text="0")
label_changed.grid(column=1, row=1)

entry = tkinter.Entry(width=10)
entry.grid(column=1, row=0)


def button_clicked():
    miles = float(entry.get())
    label_changed.config(text=round(miles*1.609))
    label_changed.grid(column=1, row=1)


button = tkinter.Button(text="calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
