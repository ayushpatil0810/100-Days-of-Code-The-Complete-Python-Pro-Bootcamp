from tkinter import *
from customtkinter import *
from CTkMessagebox import *
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or password == 0:
        msg_box = CTkMessagebox(title="Oops !", message="Please make sure you haven't left any fields empty.",icon="cancel", option_1="Ok")
    else:
        message_box = CTkMessagebox(title=f"{website}",
                              message=f"These are the details entered: \nEmail: {email} \nPassword : {password} \nIs it ok to save ?",
                              icon="warning", option_1="Ok", option_2="Cancel")
        is_ok = message_box.get()

        if is_ok == "Ok":
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")

            entry_website.delete(0, END)
            entry_password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = CTk()

window.title("Password Manager")
window.resizable(False, False)
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
window.iconphoto(False, logo)
canvas = CTkCanvas(width=200, height=200, bg="#242424", highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, pady=5)

label_website = CTkLabel(window, text="Website : ")
label_website.grid(column=0, row=1)

label_email = CTkLabel(window, text="Email / Username : ")
label_email.grid(column=0, row=2)

label_password = CTkLabel(window, text="Password : ")
label_password.grid(column=0, row=3)

entry_website = CTkEntry(window, width=350)
entry_website.grid(column=1, row=1, columnspan=2, pady=5, padx=5)

entry_email = CTkEntry(window, width=350)
entry_email.insert(0, "ayush@email.com")
entry_email.grid(column=1, row=2, columnspan=2, pady=5, padx=5)

entry_password = CTkEntry(window, width=200)
entry_password.grid(column=1, row=3, pady=5, padx=5)

generate_password_button = CTkButton(window, text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, padx=5)

add_button = CTkButton(window, text="Add", width=360, command=save_info)
add_button.grid(column=1, row=4, pady=5, columnspan=2)

window.after(100, lambda: entry_website.focus())

window.mainloop()
