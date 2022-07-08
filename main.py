from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
FONT= "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehension 
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list+=[choice(symbols) for _ in range(randint(2, 4))]
    password_list+=[choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_the_data():
    website = website_name_entry.get()
    user = user_name_entry.get()
    password_given = password_entry.get()

    if len(website)==0 or len(user)==0 or len(password_given)==0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have entered \n Email: {user} \n Password: {password_given}" 
                                                                f"\n Is it Okay to Save it?")
        if is_ok:
            with open("data.txt","a") as data:
                data.write(f"{website}|{user}|{password_given}\n")
                website_name_entry.delete(0, END)
                password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(bg= "green",padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)

website_name = Label(text="Website:")
website_name.grid(row=1, column=0)

website_name_entry = Entry(width= 51)
website_name_entry.grid(row=1, column=1, columnspan=2)
website_name_entry.focus()

user_name = Label(text="Email/Username:")
user_name.grid(row=2, column=0)

user_name_entry = Entry(width=51)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "abc@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generate_button = Button(text="Generate Password", command=create_password)
generate_button.grid(row=3, column=2,padx=1, pady=1)

add_button = Button(text="Add", width= 44, command=save_the_data)
add_button.grid(row=4, column=1, columnspan=2, padx=1, pady=1)

window.mainloop()