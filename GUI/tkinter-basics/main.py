import tkinter

window = tkinter.Tk()
window.title("Welcome to Tkinter")
window.minsize(width=400, height=400)

click_count = 0


def on_button_click():
    global click_count
    click_count += 1

    new_text = textfield.get()
    label["text"] = f"{new_text}: {click_count}"


label = tkinter.Label(text=f"Button Clicked: {click_count}", font=("Arial", 24, "bold"))
label.pack()

button = tkinter.Button(text="Click Me", command=on_button_click)
button.pack()

textfield = tkinter.Entry()
textfield.pack()

window.mainloop()
