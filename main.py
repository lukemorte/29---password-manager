import tkinter

SCREEN_WIDTH = 200
SCREEN_HEIGHT = 200

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg="white", highlightthickness=0)
logo_image = tkinter.PhotoImage(file="logo.png")

canvas.create_image(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, image=logo_image, anchor="center")

# zobrazení - teprve v ten moment se objekt vykreslí
canvas.grid(column=1, row=1)


window.mainloop()
