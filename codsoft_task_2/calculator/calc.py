import tkinter as tk

def button_click(number):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(0, str(current) + str(number))

def button_clear():
    entry_field.delete(0, tk.END)

def button_operation(op):
    current = entry_field.get()
    if current != "":
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(current) + str(op))

def button_equal():
    expression = entry_field.get()
    try:
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(0, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, "Error")

window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="#2E4F84")  

entry_field = tk.Entry(window, width=30, borderwidth=5, bg="#ffffff", font=("Arial", 14))
entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

button_style = {
    "font": ("Arial", 14),
    "bg": "#ADD8E6",  
    "fg": "#2E4F84",
    "padx": 20,
    "pady": 10,
    "bd": 0,
    "relief": "flat",
    "activebackground": "#87CEEB",  
    "activeforeground": "#333333"
}

buttons = [
    ('7', lambda: button_click(7)),
    ('8', lambda: button_click(8)),
    ('9', lambda: button_click(9)),
    ('/', lambda: button_operation('/')),
    ('4', lambda: button_click(4)),
    ('5', lambda: button_click(5)),
    ('6', lambda: button_click(6)),
    ('*', lambda: button_operation('*')),
    ('1', lambda: button_click(1)),
    ('2', lambda: button_click(2)),
    ('3', lambda: button_click(3)),
    ('-', lambda: button_operation('-')),
    ('C', button_clear),
    ('0', lambda: button_click(0)),
    ('=', button_equal),
    ('+', lambda: button_operation('+'))
]

row = 1
col = 0
for text, command in buttons:
    tk.Button(window, text=text, command=command, **button_style).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

window.mainloop()
