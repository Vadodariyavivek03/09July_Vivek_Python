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

def delete_post():
    sel = posts_list.curselection()
    if not sel: return
    filename = posts_list.get(sel[0])
    path = os.path.join(FOLDER, filename)
    if messagebox.askyesno("Delete", f"Delete post '{filename}'?"):
        os.remove(path)
        refresh_posts()
        preview.delete("1.0", tk.END)

def clear_form():
    name_entry.delete(0, tk.END)
    title_entry.delete(0, tk.END)
    content_text.delete("1.0", tk.END)

# GUI
app = tk.Tk()
app.title("MiniBlog")
app.geometry("720x480")
app.config(bg="#f0f4f8")

# Heading
tk.Label(app, text="📝 Create & Save Post", font=("Arial", 16, "bold"),
         bg="#f0f4f8", fg="#333").grid(row=0, column=0, columnspan=2, pady=12)

# Labels + Inputs aligned on the left (sticky="w")
tk.Label(app, text="Name:", font=("Arial", 11, "bold"), bg="#f0f4f8").grid(row=1, column=0, sticky="w", padx=8, pady=5)
name_entry = tk.Entry(app, font=("Arial", 11)); name_entry.grid(row=1, column=1, sticky="ew", padx=8, pady=5)

tk.Label(app, text="Title:", font=("Arial", 11, "bold"), bg="#f0f4f8").grid(row=2, column=0, sticky="w", padx=8, pady=5)
title_entry = tk.Entry(app, font=("Arial", 11)); title_entry.grid(row=2, column=1, sticky="ew", padx=8, pady=5)

tk.Label(app, text="Content:", font=("Arial", 11, "bold"), bg="#f0f4f8").grid(row=3, column=0, sticky="nw", padx=8, pady=5)
content_text = tk.Text(app, height=6, wrap="word", font=("Arial", 11))
content_text.grid(row=3, column=1, sticky="ew", padx=8, pady=5)

# Buttons Save + Clear
btn_frame = tk.Frame(app, bg="#f0f4f8")
btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(btn_frame, text="💾 Save", width=12, bg="#4CAF50", fg="white",
          font=("Arial", 11, "bold"), command=save_post).pack(side="left", padx=12)
tk.Button(btn_frame, text="🧹 Clear", width=12, bg="#f44336", fg="white",
          font=("Arial", 11, "bold"), command=clear_form).pack(side="left", padx=12)

# Posts list and preview
posts_list = tk.Listbox(app, font=("Arial", 11), width=25)
posts_list.grid(row=5, column=0, sticky="nsew", padx=8, pady=6)

btn2_frame = tk.Frame(app, bg="#f0f4f8")
btn2_frame.grid(row=6, column=0, pady=6)
tk.Button(btn2_frame, text="👁 View", width=10, bg="#2196F3", fg="white",
          font=("Arial", 11, "bold"), command=view_post).pack(side="left", padx=6)
tk.Button(btn2_frame, text="🗑 Delete", width=10, bg="#e91e63", fg="white",
          font=("Arial", 11, "bold"), command=delete_post).pack(side="left", padx=6)

preview = tk.Text(app, height=12, wrap="word", font=("Arial", 11))
preview.grid(row=5, column=1, rowspan=2, sticky="nsew", padx=8, pady=6)

# Resize behavior
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(5, weight=1)

refresh_posts()
app.mainloop()
