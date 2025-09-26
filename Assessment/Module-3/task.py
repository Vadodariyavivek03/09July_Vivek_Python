import os
import tkinter as tk
from tkinter import messagebox

# class

class User:
    def __init__(self, name):
        self.name = name

# ------------------------------------------------------------------------------------------- #

class Post:
    
    os.chdir("Module-3")        # create folder to save posts
    FOLDER = "Posts"
    os.makedirs(FOLDER, exist_ok=True)

    def __init__(self, author, title, content):
        self.author = author
        self.title = title
        self.content = content

    def get_filename(self):
        return f"{self.author.name}_{self.title}.txt".replace(" ", "_")
    
    def save(self):
        path = os.path.join(Post.FOLDER, self.get_filename())
        f = open(path, "w", encoding="utf-8")
        f.write(f"Author :: {self.author.name}\nTitle :: {self.title}\n\nContent :: {self.content}")

    def delete(filename):
        path = os.path.join(Post.FOLDER, filename)
        if os.path.exists(path):
            os.remove(path)
            return True
        return False
    
    def load(filename):
        path = os.path.join(Post.FOLDER, filename)
        if os.path.exists(path):
            f = open(path, "r", encoding="utf-8")
            content = f.read()
            return content  
        return ""
    
    def list_posts():
        return [fn for fn in os.listdir(Post.FOLDER) if fn.endswith(".txt")]

# ------------------------------------------------------------------------------------------- #

def save_post():                      
    name = name_entry.get().strip()
    title = title_entry.get().strip()
    content = content_text.get("1.0", tk.END).strip()

    if not name or not title or not content:
        messagebox.showwarning("Error!!", "All fields are required!")
        return

    user = User(name)
    post = Post(user, title, content)
    post.save()

    refresh_posts()
    clear_form()

    messagebox.showinfo("Saved Post Successfully!!", f"Post saved as {post.get_filename()}")

# ------------------------------------------------------------------------------------------- #

def refresh_posts():
    posts_list.delete(0, tk.END)

    for fn in Post.list_posts():
        posts_list.insert(tk.END, fn)

# ------------------------------------------------------------------------------------------- #

def view_post():
    try:
        index = posts_list.curselection()[0] 
    except IndexError:
        print("No post selected to view...!!")  
        return

    filename = posts_list.get(index)
    content = Post.load(filename)

    view.delete("1.0", tk.END)
    view.insert("1.0", content)


# ------------------------------------------------------------------------------------------- #

def delete_post():
    try:
        index = posts_list.curselection()[0]   
    except IndexError:
        print("No post selected to delete...!!")  
        return

    filename = posts_list.get(index)
   
    if not os.path.exists(os.path.join(Post.FOLDER, filename)):
        messagebox.showerror("Error!!", f"File '{filename}' not found...!!")
        return

    if messagebox.askyesno("Confirm Delete!!", f"Are you sure you want to delete '{filename}'?"):
        Post.delete(filename)
        refresh_posts()
        view.delete("1.0", tk.END)
        messagebox.showinfo("Deleted!!", f"File '{filename}' has been deleted successfully..")


# ------------------------------------------------------------------------------------------- #

def clear_form():
    name_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

# ------------------------------------------------------------------------------------------- #

# GUI Application

my_app = tk.Tk()
my_app.title("Mini_Blog")
my_app.geometry("820x580")
my_app.config(bg="#f0f4f8")

# Heading

tk.Label(my_app, text="Create & Save Post", font=("Arial", 16, "bold"),bg="#d4edda", 
         fg="#333", padx=10, pady=5).grid(row=0, column=0, columnspan=2 , sticky="nsew", pady=(10,5))

# Labels

tk.Label(my_app, text="Name :::", font=("Arial", 11, "bold"), 
         bg="#f0f4f8").grid(row=1, column=0, sticky="nsew", padx=8, pady=5)

name_entry = tk.Entry(my_app, font=("Arial", 11)); 
name_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=5)

tk.Label(my_app, text="Title :::", font=("Arial", 11, "bold"), 
         bg="#f0f4f8").grid(row=2, column=0, sticky="nsew", padx=8, pady=5)

title_entry = tk.Entry(my_app, font=("Arial", 11)); 
title_entry.grid(row=2, column=1, sticky="ew", padx=8, pady=5)

tk.Label(my_app, text="Content :::", font=("Arial", 11, "bold"), 
         bg="#f0f4f8").grid(row=3, column=0, sticky="nsew", padx=8, pady=5)

content_text = tk.Text(my_app, height=6, wrap="word", font=("Arial", 11))
content_text.grid(row=3, column=1, sticky="ew", padx=8, pady=5)

# Buttons

btn_frame = tk.Frame(my_app, bg="#f0f4f8")
btn_frame.grid(row=4, column=1, pady=10, sticky="n")

tk.Button(btn_frame, text="Save", width=12, bg="#4CAF50", fg="white",
          font=("Arial", 11, "bold"), command=save_post).pack(side="left", padx=12)

tk.Button(btn_frame, text="Clear", width=12, bg="#c07ca1", fg="white",
          font=("Arial", 11, "bold"), command=clear_form).pack(side="left", padx=12)
          

# Posts List and View Post

tk.Label(my_app, text="...Saved Posts List...", font=("Arial", 11, "bold"),
         bg="#d4edda", fg="#333", anchor="center").grid(row=5, column=0, sticky="nsew", padx=8, pady=(0,2))

posts_list = tk.Listbox(my_app, font=("Arial", 11), width=25)
posts_list.grid(row=6, column=0, sticky="nsew", padx=8, pady=6)

btn2_frame = tk.Frame(my_app, bg="#f0f4f8")
btn2_frame.grid(row=7, column=0, pady=6)

tk.Button(btn2_frame, text="View", width=10, bg="#2196F3", fg="white",
          font=("Arial", 11, "bold"), command=view_post).pack(side="left", padx=6)

tk.Button(btn2_frame, text="Delete", width=10, bg="#FF0000", fg="white",
          font=("Arial", 11, "bold"), command=delete_post).pack(side="left", padx=6)

tk.Label(my_app, text="...View Post Here...", font=("Arial", 11, "bold"),
         bg="#d4edda", fg="#333", anchor="center").grid(row=5, column=1, sticky="nsew", padx=8, pady=(0,2))

view = tk.Text(my_app, height=12, wrap="word", font=("Arial", 11))
view.grid(row=6, column=1, rowspan=2, sticky="nsew", padx=8, pady=6)

my_app.grid_columnconfigure(1, weight=1)
my_app.grid_rowconfigure(6, weight=1)

refresh_posts()

my_app.mainloop()

# ---------------------------------------------------------------------------------- #