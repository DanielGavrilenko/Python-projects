import tkinter
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_click():
    user_website = website_field.get()
    user_email = email_field.get()
    user_password = password_field.get()
    print(len(user_password))
    if len(user_password) == 0 or len(user_email) == 0 or len(user_password) == 0:
        error = messagebox.showinfo(title="O0Ps", message="Please don't leave any fields empty")
    else:
        message = messagebox.askokcancel(title=user_website, message=f"There are  the details entered:\n "
                                                                     f"Email: {user_email}\n Password: {user_password}")
        if message:
            with (open("data.txt", "a") as write_file):
                write_file.write(f"{user_website} | {user_email} | {user_password}\n")
            website_field.delete(0, tkinter.END)
            email_field.delete(0, tkinter.END)
            password_field.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

website_field = tkinter.Entry(width=55)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()
email_field = tkinter.Entry(width=55)
email_field.grid(column=1, row=2, columnspan=2)
email_field.insert(tkinter.END, "gavrilenko@gmail.com")
password_field = tkinter.Entry(width=37)
password_field.grid(column=1, row=3)

generate_button = tkinter.Button(text="Generate Password")
generate_button.grid(column=2, row=3)
add_button = tkinter.Button(width=47, text="Add", command=add_button_click)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
