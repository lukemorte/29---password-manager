import tkinter
import tkinter.messagebox
import pyperclip
from random import randint, choice, shuffle
import json

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
               'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
               'W', 'X', 'Y', 'Z']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/',
               ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{',
               '|', '}', '~']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = []
    password = ""

    password_list = [choice(letters) for _ in range(randint(5, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 7))]
    password_list += [choice(numbers) for _ in range(randint(4, 8))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)

    pyperclip.copy(password)
    window.bell()  # Zahraje pípnutí


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        tkinter.messagebox.showerror("Error", "Please, fill in all fields.")
    else:

        try:
            with open("data.json", "r") as data_file:
                # load
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # save new_data
                json.dump(new_data, data_file, indent=4)

        else:
            # update
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # save updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

            confirm = tkinter.Label(text="Úspěšně jste uložili heslo.", bg="#899d00", fg="white", padx=10, pady=5)
            confirm.place(x=0, y=0)
            window.after(1500, confirm.destroy)


# ---------------------------- SEARCH ------------------------------- #        


def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo("Error", "JSON File not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            msg = f"username: {data[website]["email"]}\npassword: {data[website]["password"]}"
            info = "\n\n(password waas coppied to clipboard)"
            msg += info
            pyperclip.copy(data[website]["password"])
            tkinter.messagebox.showinfo(website, msg)
        else:
            tkinter.messagebox.showerror("Error", f"{website} is not in records.")

# ---------------------------- UI SETUP ------------------------------- #


# window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# canvas
canvas = tkinter.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="white", highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=logo_img, anchor="center")

# form
website_label = tkinter.Label(text="Website")
website_entry = tkinter.Entry(width=15)
website_entry.focus()
search_button = tkinter.Button(text="Search", width=15, command=find_password)
email_label = tkinter.Label(text="Username / email")
email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "docteur@email.cz")
password_label = tkinter.Label(text="Password")
password_entry = tkinter.Entry(width=15)
generate_button = tkinter.Button(text="Generate password", width=15, command=generate_password)
add_button = tkinter.Button(text="Add", width=30, command=save)

# zobrazení - teprve v ten moment se objekt vykreslí
canvas.grid(column=1, row=0, pady=(0, 20), columnspan=2)
website_label.grid(column=0, row=1, sticky="E", padx=5, pady=5)
website_entry.grid(column=1, row=1, sticky="EW", padx=5, pady=5, ipadx=50, ipady=3)
search_button.grid(column=2, row=1, sticky="EW", padx=5, pady=5)
email_label.grid(column=0, row=2, sticky="E", padx=5, pady=5)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", padx=5, pady=5, ipady=3)
password_label.grid(column=0, row=3, sticky="E", padx=5, pady=5)
password_entry.grid(column=1, row=3, sticky="EW", padx=5, pady=5, ipady=3)
generate_button.grid(column=2, row=3, sticky="EW", padx=5, pady=5)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=5, pady=5)

window.mainloop()
