import tkinter as tk

# definition
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#222222")

# display box
display = tk.Entry(root, font=("Arial", 24), justify="right", bg="#333333", fg="white")
display.pack(padx=10, pady=10, fill="x", ipady=15)

# function to insert numbers and operators
def insert_value(value):
    display.insert(tk.END, value)

#Equal to sign
def calculate():
    expression=display.get()

    try:
        result=eval(expression,{"__builtins__":None},{})
        display.delete(0,tk.END)
        display.insert(tk.END,result)

    except:
        display.delete(0,tk.END)
        display.insert(tk.END,"Error")

#Backspace
def backspace():
    text=display.get()
    display.delete(0,tk.END)
    display.insert(tk.END,text[:-1])
    
#delete button C
def clear():
    display.delete(0,tk.END)

    
# Buttons
Button_frame = tk.Frame(root, bg="#222222")
Button_frame.pack()

# top row
b00 = tk.Button(Button_frame, text="7", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("7"))
b01 = tk.Button(Button_frame, text="8", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("8"))
b02 = tk.Button(Button_frame, text="9", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("9"))
b03 = tk.Button(Button_frame, text="/", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("/"))

b00.grid(row=0, column=0, padx=3, pady=3)
b01.grid(row=0, column=1, padx=3, pady=3)
b02.grid(row=0, column=2, padx=3, pady=3)
b03.grid(row=0, column=3, padx=3, pady=3)

# second row
b10 = tk.Button(Button_frame, text="4", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("4"))
b11 = tk.Button(Button_frame, text="5", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("5"))
b12 = tk.Button(Button_frame, text="6", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("6"))
b13 = tk.Button(Button_frame, text="*", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("*"))

b10.grid(row=1, column=0, padx=3, pady=3)
b11.grid(row=1, column=1, padx=3, pady=3)
b12.grid(row=1, column=2, padx=3, pady=3)
b13.grid(row=1, column=3, padx=3, pady=3)

# third row
b20 = tk.Button(Button_frame, text="1", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("1"))
b21 = tk.Button(Button_frame, text="2", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("2"))
b22 = tk.Button(Button_frame, text="3", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("3"))
b23 = tk.Button(Button_frame, text="-", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("-"))

b20.grid(row=2, column=0, padx=3, pady=3)
b21.grid(row=2, column=1, padx=3, pady=3)
b22.grid(row=2, column=2, padx=3, pady=3)
b23.grid(row=2, column=3, padx=3, pady=3)

# fourth row
b30 = tk.Button(Button_frame, text="0", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("0"))
b31 = tk.Button(Button_frame, text=".", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("."))
b32 = tk.Button(Button_frame, text="=", font=("Arial", 18), width=5, height=2,command=calculate)
b33 = tk.Button(Button_frame, text="+", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("+"))

b30.grid(row=3, column=0, padx=3, pady=3)
b31.grid(row=3, column=1, padx=3, pady=3)
b32.grid(row=3, column=2, padx=3, pady=3)
b33.grid(row=3, column=3, padx=3, pady=3)

# fifth row - brackets
b40 = tk.Button(Button_frame, text="(", font=("Arial", 18), width=5, height=2, command=lambda: insert_value("("))
b41 = tk.Button(Button_frame, text=")", font=("Arial", 18), width=5, height=2, command=lambda: insert_value(")"))
b42 = tk.Button(Button_frame, text="⌫", font=("Arial", 18), width=5, height=2, command=backspace)
b43 = tk.Button(Button_frame, text="C", font=("Arial", 18), width=5, height=2, command=clear)

b40.grid(row=4, column=0, padx=3, pady=3)
b41.grid(row=4, column=1, padx=3, pady=3)
b42.grid(row=4, column=2, padx=3, pady=3)
b43.grid(row=4, column=3, padx=3, pady=3)

root.mainloop()
