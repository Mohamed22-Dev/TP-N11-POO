import tkinter as tk


def calculer_carre():
    try:
        nombre = float(entry_nombre.get())
        carre = nombre ** 2
        label_result.config(text=f"Résultat : {carre}")
    except:
        label_result.config(text="Entrée invalide")

window = tk.Tk()
window.title("Calcul du Carré")
window.geometry("300x200")


label = tk.Label(window, text="Entrer un nombre :")
label.pack(pady=5)


entry_nombre = tk.Entry(window)
entry_nombre.pack(pady=5)


entry_autre = tk.Entry(window)
entry_autre.pack(pady=5)

btn = tk.Button(window, text="Calculer le carré", command=calculer_carre)
btn.pack(pady=10)


label_result = tk.Label(window, text="")
label_result.pack(pady=5)


window.mainloop()