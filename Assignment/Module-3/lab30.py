import tkinter

app = tkinter.Tk()
app.title("Calculator")
app.geometry("500x120")  
app.config(bg="light blue")

tkinter.Label(app, text="Number 1 :", bg="light blue", fg="blue", 
              font='Arial 15 bold').grid(row=0, column=0, sticky='w')
tkinter.Label(app, text="Number 2 :", bg="light blue", fg="blue", 
              font='Arial 15 bold').grid(row=1, column=0, sticky='w')

n1 = tkinter.Entry(app)
n1.grid(row=0, column=1, sticky='w')
n2 = tkinter.Entry(app)
n2.grid(row=1, column=1, sticky='w')

def add():
    result = int(n1.get()) + int(n2.get())
    print("Addition ::", result)

def sub():
    result = int(n1.get()) - int(n2.get())
    print("Subtraction ::", result)

def mul():
    result = int(n1.get()) * int(n2.get())
    print("Multiplication ::", result)

def div():
    try:
        result = float(n1.get()) / float(n2.get())
        print("Division ::", result)
    except ZeroDivisionError:
        print("Error :: Division by zero")

tkinter.Button(app, text="Addition", fg="blue", font='Arial 12 bold', 
               command=add).grid(row=2, column=0, sticky='ew')
tkinter.Button(app, text="Subtraction", fg="red", font='Arial 12 bold', 
               command=sub).grid(row=2, column=1, sticky='ew')
tkinter.Button(app, text="Multiplication", fg="green", font='Arial 12 bold', 
               command=mul).grid(row=2, column=2, sticky='ew')
tkinter.Button(app, text="Division", fg="orange", font='Arial 12 bold', 
               command=div).grid(row=2, column=3, sticky='ew')


for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
