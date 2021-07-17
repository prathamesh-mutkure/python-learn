from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please enter data in all fields")
        return

    try:
        with open("data.json", "r") as file:
            data = json.load(file)                  # Read old data
    except FileNotFoundError:
        with open("data.json", "w") as file:
            json.dump(new_data, file, indent=4)     # If file not exist create one and save new data
    else:
        data.update(new_data)                       # Update with new data
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)         # Write/Save updated data
    finally:
        pyperclip.copy(password)
        website_input.delete(0, END)
        password_input.delete(0, END)
        website_input.focus()

# ---------------------------- SAVE PASSWORD ------------------------------- #


def search_password():
    website = website_input.get()

    try:
        with open("data.json") as file:
            data = json.load(file)
            website_data = data[website]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists")
    else:
        email = website_data["email"]
        password = website_data["password"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title(string="Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo = canvas.create_image(100, 100, image=logo_img)

# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entry
website_input = Entry(width=18)
email_input = Entry(width=35)
password_input = Entry(width=18)

website_input.focus()
email_input.insert(END, "prathamesh@gmail.com")

# Buttons
search_btn = Button(text="Search", command=search_password, width=11)
generate_pass_btn = Button(text="Generate Password", command=generate_random_password, width=11)
add_btn = Button(text="Add", width=33, command=save_password)

# Grid Placements
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

website_input.grid(row=1, column=1)
email_input.grid(row=2, column=1, columnspan=2)
password_input.grid(row=3, column=1)

search_btn.grid(row=1, column=2)
generate_pass_btn.grid(row=3, column=2)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
