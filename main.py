from tkinter import *
from tkinter import messagebox  # it's not a class, but a module, so imported it separately
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    my_web = web_entry.get()
    try:
        with open("data.json", "r") as file:
            # reads the data and prints it on console
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    else:
        if my_web in data:
            email = data[my_web]["email"]
            password = data[my_web]["password"]
            messagebox.showinfo(title=my_web, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {my_web} exists.")


def generate_password():

    # checking if anything is written in password entry box if not than execute
    if len(pass_entry.get()) == 0:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        # list of letters, nums and symbols been created by random choices in random range
        # e.g. 9-11 letters, 3-5 symbols, 3-5 numbers
        list_letters = [choice(letters) for _ in range(randint(8, 10))]
        list_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        list_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        # making it a single list
        combine = list_letters + list_symbols + list_numbers

        # randomizing the order of numbers, letters and symbols
        shuffle(combine)
        # converting randomize list into string
        password = "".join(combine)
        # inserting in entry box
        pass_entry.insert(0, password)

        # spontaneously copy your password to clipboard ready to paste it on another place
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def write_json(data_pass):
    # writing in json file
    with open("data.json", "w") as data_file:
        json.dump(data_pass, data_file, indent=4)


def save():  # runs when add button is pressed
    # returning the values typed in entries by user
    my_web = web_entry.get()
    my_email = e_entry.get()
    my_pass = pass_entry.get()

    # creating a dict for each set of data entry by user to pass it on in json file
    new_data = {
        my_web: {
            "email": my_email,
            "password": my_pass
        }
    }

    # if any entry field is left empty, while pressing add button, than a error prompt appears
    if len(my_web) == 0 or len(my_pass) == 0 or len(my_email) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")
    else:
        # asking for conformation
        is_ok = messagebox.askokcancel(title=my_web, message=f"These are the details entered: \nEmail: {my_email} "
                                                              f"\nPassword: {my_pass} \nIs it ok to save?")

        # making a new file, writing the entries in it, and deleting it from the canvas entries
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # reads the data and prints it on console
                    data = json.load(file)
                    # updating old data with the new_data
                    data.update(new_data)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                data = new_data
            finally:
                write_json(data)
                web_entry.delete(0, END)
                e_entry.delete(0, END)
                pass_entry.delete(0, END)
                put_default()


def put_default():  # will display the last entered email in email entry
    try:
        with open("data.json") as file:
            data = json.load(file)
            if len(data) != 0:
                for website in data:
                    e_entry.delete(0, END)
                    e_entry.insert(END, data[website]["email"])
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        e_entry.delete(0, END)
        e_entry.insert(END, "example@gmail.com")
# ---------------------------- UI SETUP ------------------------------- #
# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="light blue")

# Canvas setup
canvas = Canvas(width=200, height=200, highlightthickness=0, bg="light blue")
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Labels formation and placement
website_label = Label(text="Website: ", bg="light blue", font=("aerial", 10, "bold"), fg="red")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username: ", bg="light blue", font=("aerial", 10, "bold"), fg="red")
email_label.grid(row=2, column=0)

password_label = Label(text="Password: ", bg="light blue", font=("aerial", 10, "bold"), fg="red")
password_label.grid(row=3, column=0)

# Buttons formation and placement
pass_generation = Button(text="Generate Password", width=15, command=generate_password)
pass_generation.grid(row=3, column=3)

add = Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=13, command=find_password, bg="grey")
search.grid(row=1, column=2, columnspan=2)

# Entries formation and placement
web_entry = Entry(width=35, bg="light green", font=("aerial", 8, "bold"))
web_entry.grid(row=1, column=1, columnspan=2)
# this will automatically put the cursor in this entry when the program starts
web_entry.focus()

e_entry = Entry(width=53, bg="light green", font=("aerial", 8, "bold"))
e_entry.grid(row=2, column=1, columnspan=3)
put_default()

pass_entry = Entry(width=35, bg="light green", font=("aerial", 8, "bold"))
pass_entry.grid(row=3, column=1, columnspan=2)

window.mainloop()
