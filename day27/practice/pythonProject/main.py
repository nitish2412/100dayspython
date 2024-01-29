import tkinter


def button_clicked():
    # print("button clicked")
    # my_label['text'] = "Button Got clicked"
    # my_label.config(text="Button Got clicked")
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0,row=0)
my_label.config(padx=10, pady=10)
# my_label.place(x=100,y=0)
#my_label.pack()
# my_label.pack(side='left')
# my_label.pack(expand=True)
# my_label['text'] = "New Text"



# Button
button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

# Button
new_button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
new_button.grid(column=2,row=0)

# entry
input = tkinter.Entry(width=10)
#input.pack()
input.grid(column=3,row=3)

window.mainloop()
