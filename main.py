import tkinter

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


#window
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
email_label = tkinter.Label(text="Username / email")
email_entry = tkinter.Entry(width=35)
password_label = tkinter.Label(text="Password")
password_entry = tkinter.Entry(width=15)
generate_button = tkinter.Button(text="Generate password", width=15)
add_button = tkinter.Button(text="Add", width=30)


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
