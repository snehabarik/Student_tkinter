from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Student Form")

# icon
root.iconbitmap(r"C:\Users\HP\OneDrive\Documents\advancedpython\pixel2.ico")

root.geometry('500x500+0+0')
root.configure(background='#FADADD')

# -------- LOGIN FUNCTION --------
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "" or password == "":
        messagebox.showwarning("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Login Successful!\nWelcome {email}")

# image
img = Image.open(r"C:\Users\HP\OneDrive\Documents\advancedpython\star.png")
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg='#00704A')
img_label.pack(pady=10, padx=20)

# text label
text_label = Label(root,
                   text="MUSIFY",
                   font=('Arial',18,'bold'),
                   bg='#00704A',
                   fg='white')
text_label.pack(pady=10)

# email
email_label = Label(root,
                    text="Email",
                    font=('Arial',18,'bold'),
                    bg='#00704A',
                    fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root,
                    font=('Arial',18),
                    fg='white',
                    bg='grey')
email_entry.pack(pady=(5,10))

# password
password_label = Label(root,
                       text="Password",
                       font=('Arial',18,'bold'),
                       bg='#00704A',
                       fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root,
                       font=('Arial',18),
                       fg='white',
                       bg='grey',
                       show="*")
password_entry.pack(pady=(5,10))

# login button
login_btn = Button(root,
                   text="Login",
                   font=('Arial',18,'bold'),
                   bg='#00704A',
                   fg='white',
                   command=login)
login_btn.pack(pady=(5,10))

root.mainloop()
