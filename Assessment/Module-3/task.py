import os
import tkinter as tk
from tkinter import messagebox

FOLDER = "posts"
os.makedirs(FOLDER, exist_ok=True)

def save_post():
    name = name_entry.get().strip()
    title = title_entry.get().strip()
    content = content_text.get("1.0", tk.END).strip()

    if not name or not title or not content:
        messagebox.showwarning("Missing Info", "Fill all fields!")
        return

    filename = f"{name}_{title}.txt".replace(" ", "_")
    path = os.path.join(FOLDER, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"Author: {name}\nTitle: {title}\n\n{content}")

    refresh_posts()
    clear_form()
    messagebox.showinfo("Saved", f"Post saved as {filename}")

def refresh_posts():
    posts_list.delete(0, tk.END)
    for fn in os.listdir(FOLDER):
        if fn.endswith(".txt"):
            posts_list.insert(tk.END, fn)

def view_post():
    sel = posts_list.curselection()
    if not sel: return
    filename = posts_list.get(sel[0])
    path = os.path.join(FOLDER, filename)
    with open(path, "r", encoding="utf-8") as f:
        preview.delete("1.0", tk.END)
        preview.insert("1.0", f.read())

def clear_form():
    name_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

# GUI
app = tk.Tk()
app.title("MiniBlog")
app.geometry("600x420")
app.config(bg="#f0f4f8")

# Heading
tk.Label(app, text="📝 Create & Save Post", font=("Arial", 16, "bold"), 
         bg="#f0f4f8", fg="#333").grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(app, text="Name:", bg="#f0f4f8").grid(row=1, column=0, sticky="w", padx=8, pady=4)
name_entry = tk.Entry(app); name_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=4)

tk.Label(app, text="Title:", bg="#f0f4f8").grid(row=2, column=0, sticky="w", padx=8, pady=4)
title_entry = tk.Entry(app); title_entry.grid(row=2, column=1, sticky="ew", padx=8, pady=4)

tk.Label(app, text="Content:", bg="#f0f4f8").grid(row=3, column=0, sticky="nw", padx=8, pady=4)
content_text = tk.Text(app, height=6, wrap="word"); content_text.grid(row=3, column=1, sticky="ew", padx=8, pady=4)

# Button frame for Save and Clear
btn_frame = tk.Frame(app, bg="#f0f4f8")
btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(btn_frame, text="💾 Save", width=12, bg="#4CAF50", fg="white", command=save_post).pack(side="left", padx=10)
tk.Button(btn_frame, text="🧹 Clear", width=12, bg="#f44336", fg="white", command=clear_form).pack(side="left", padx=10)

# Posts list and preview
posts_list = tk.Listbox(app); posts_list.grid(row=5, column=0, sticky="nsew", padx=8, pady=6)
tk.Button(app, text="👁 View", bg="#2196F3", fg="white", command=view_post).grid(row=6, column=0, pady=6)

preview = tk.Text(app, height=10, wrap="word"); preview.grid(row=5, column=1, rowspan=2, sticky="nsew", padx=8, pady=6)

app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(5, weight=1)

refresh_posts()
app.mainloop()
