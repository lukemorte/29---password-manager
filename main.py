import tkinter
import tkinter.messagebox
import random

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

    password = ""

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    all_counts = [nr_letters, nr_symbols, nr_numbers]

    lenpass = nr_letters + nr_symbols + nr_numbers

    for i in range(0, lenpass):
        arr = []	
        arr.append(random.choice(letters))
        arr.append(random.choice(symbols))
        arr.append(random.choice(numbers))

        arr_types = []
        if all_counts[0] > 0:
            arr_types.append(0)
        if all_counts[1] > 0:
            arr_types.append(1)
        if all_counts[2] > 0:
            arr_types.append(2)

        choice = random.choice(arr_types)
        all_counts[choice] -= 1
        password += arr[choice]

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if website_entry.get() == "" or email_entry.get() == "" or password_entry.get() == "":
        tkinter.messagebox.showerror("Error", "Please, fill in all fields.")
    else:
        ask_for_save = tkinter.messagebox.askokcancel(title="Confirm", message=
                                       f"These are the details entered: \nEmail: {email_entry.get()}"
                                       f"\nPassword: {password_entry.get()} \n\nIs it OK to save?")

        if ask_for_save == True:
            save_str = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
            with open("data.txt", "a") as file:
                file.write(save_str)

            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

            confirm = tkinter.Label(text="Úspěšně jste uložili heslo.", bg="#899d00", fg="white", padx=10, pady=5)
            confirm.place(x=0, y=0)
            window.after(1500, confirm.destroy)


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
website_entry = tkinter.Entry(width=35)
website_entry.focus()
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
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW", padx=5, pady=5, ipadx=50, ipady=3)
email_label.grid(column=0, row=2, sticky="E", padx=5, pady=5)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW", padx=5, pady=5, ipady=3)
password_label.grid(column=0, row=3, sticky="E", padx=5, pady=5)
password_entry.grid(column=1, row=3, sticky="EW", padx=5, pady=5, ipady=3)
generate_button.grid(column=2, row=3, sticky="EW", padx=5, pady=5)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=5, pady=5)



window.mainloop()
