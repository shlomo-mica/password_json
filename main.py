import json
import tkinter as tk
from tkinter import messagebox
from random import shuffle, randint, choice
from json.decoder import JSONDecodeError


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)
    #

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    letters_list = [choice(letters) for char in
                    range(nr_letters)]  # or range(randint(8,10) because we import randint above
    symbols_list = [choice(symbols) for c in range(randint(2, 4))]
    numbers_list = [choice(numbers) for n in range(nr_numbers)]
    password_list = letters_list + symbols_list + numbers_list
    password_list.sort()

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char
    password = ''.join(password_list)
    print(f"Your password is: {password}")
    Password_entry.insert(0, password)


def find_password():
    # web entry search
    web_name = website_var.get()
    print(web_name)
    w = open("112.json", "r")
    try:
        web_dictionary = json.load(w)
        messagebox.showinfo("web search detail", web_dictionary[web_name])
        print(web_dictionary[web_name])
    except KeyError:
        messagebox.showinfo("No details for the web site exist")


    # if web_name == web_dictionary[web_name]:
    #     print("oooo")
    #     print(web_dictionary[web_name])
    #     messagebox.showinfo(title='result search', message=web_name)


# ---------------------------- SAVE PASSWORD +JSON CLASS------------------------------- #
def save():

    new_data = {
        website_var.get(): {
            "email": email_var.get(),
            "password": password_var.get()
        }
    }

    if password_var.get() == '' or email_var.get() == '' or website_var.get() == '':
        messagebox.showinfo("Empty fields")
    else:

        try:
            # here you can try to change file name the original is 112g.json
            with open("112.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                print(data)
                 # updating old data with new data (from here is a dictionary)
                data.update(new_data)
            with open("112.json", "w") as data_file:
                json.dump(data, data_file, indent=4)


        except JSONDecodeError:
            #TODO error handling
            print("succeed adding new item")
            # start enter a value
            with open("112.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            Password_entry.delete(0, 'end')
            Website_entry.delete(0, 'end')


# y = messagebox.askokcancel(f"you are going to enter password {password_var} Email {email_var} and website"
#                            f" {website_var}"
#                            f"is it ok?")
# if y:
#     new_data_line.writelines([password_var.get(), '   I', email_var.get(), '  I ', website_var.get(), '\n'])

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("PASSWORD")
root.config(padx=20, pady=20, bg='gray')

canvas = tk.Canvas(root, width=180, height=180, bg="#FFE873")
photo = tk.PhotoImage(file="logo.png")
canvas.create_image(90, 90, image=photo)
canvas.grid(column=1, row=0)

add_button = tk.Button(root, text="ADD", bg='pink', width=14, command=save)
add_button.grid(column=1, row=4)

search_button = tk.Button(root, text="SEARCH", bg='pink', width=14, command=find_password)
search_button.config(width=14)
search_button.grid(column=2, row=2)

Generate_password_button = tk.Button(root, text="Generate Password", command=password_generator)
Generate_password_button.config(width=14)
Generate_password_button.grid(column=2, row=3)
# ENTRY LIST
website_var = tk.StringVar(root)
Website_entry = tk.Entry(root, width=30, textvariable=website_var)
Website_entry.grid(column=1, row=1, columnspan=1)
Website_entry.focus()

email_var = tk.StringVar(root)

Email_username = tk.Entry(width=30, textvariable=email_var)
Email_username.grid(column=1, row=2)
Email_username.insert(0, 'shlomo_m@gmail.com')
m = (email_var.get())

password_var = tk.StringVar(root)
Password_entry = tk.Entry(root, width=30, textvariable=password_var, show='*')
Password_entry.grid(column=1, row=3)

# label _list
label_web = tk.Label(text="Website", width=15)
label_web.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password")
password_label.grid(column=0, row=3)
# TODO read from entry

# web_object.pack()


# write and save data to  file
new_data_line = open(f"data.txt", 'a')
print(Website_entry.get())

root.mainloop()
