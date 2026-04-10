import tkinter as tk

def click(btn):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(btn))


def calculer():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erreur")


def clear():
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("Calculatrice")
window.geometry("300x350")


entry = tk.Entry(window, width=20, font=("Arial", 18), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)


buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('/',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        tk.Button(window, text=text, width=5, height=2,
                  command=calculer).grid(row=row, column=col)
    elif text == "C":
        tk.Button(window, text="Clear", width=5, height=2,
                  command=clear).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=5, height=2,
                  command=lambda t=text: click(t)).grid(row=row, column=col)


window.mainloop()