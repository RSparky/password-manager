from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT= "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def create_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #list comprehension adding
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
    data_dict ={
        website:{
            "Email":user,
            "Password": password_given
        }
    }

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("data.json", "w") as data_file:
            json.dump(data_dict, data_file, indent=4)
    else:
        data.update(data_dict)
        with open("data.json", 'w') as data_file:
            json.dump(data,data_file, indent=4)
    finally:
        website_name_entry.delete(0, END)
        password_entry.delete(0,END)   
#---------------------------Search Password-----------------------------#
def find_password():
    website = website_name_entry.get()
    try:
        with open("data.json",'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File doesnot exist!")
    else:
        if website in data.keys():
            info = data[website]
            messagebox.showinfo(title=website, message=f"Email: {info['Email']}\nPassword: {info['Password']}")
        else:
            messagebox.showerror(title = "SearchError", message =f"{website} details are not stored in the Password Manager")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = logo)
canvas.grid(row=0, column=1)

website_name = Label(text="Website:")
website_name.grid(row=1, column=0)

website_name_entry = Entry(width= 32)
website_name_entry.grid(row=1, column=1)
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

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(row=1, column=2,padx=1, pady=1)

window.mainloop()