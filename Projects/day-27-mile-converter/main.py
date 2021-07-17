from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)


def on_calc_click():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_result_label.config(text=str(km))


mile_input = Entry(width=10)
mile_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_btn = Button(text="Calculate", command=on_calc_click)
calc_btn.grid(column=1, row=2)

window.mainloop()
