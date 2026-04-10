import tkinter as tk


compteur = 0


def incrementer():
    global compteur
    compteur += 1
    label.config(text=str(compteur))


def decrementer():
    global compteur
    if compteur > 0:
        compteur -= 1
        label.config(text=str(compteur))


window = tk.Tk()
window.title("Compteur")
window.geometry("300x200")


label = tk.Label(window, text="0", font=("Arial", 20))
label.pack(pady=20)


btn_plus = tk.Button(window, text="+", command=incrementer, width=10)
btn_plus.pack(pady=5)


btn_minus = tk.Button(window, text="-", command=decrementer, width=10)
btn_minus.pack(pady=5)


window.mainloop()