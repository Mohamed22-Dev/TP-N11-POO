import tkinter as tk


def ajouter_tache():
    tache = entry.get()
    if tache != "":
        listbox.insert(tk.END, tache)
        entry.delete(0, tk.END)


def supprimer_tache():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except:
        pass


def terminer_tache(event):
    try:
        index = listbox.curselection()[0]
        texte = listbox.get(index)


        if not texte.startswith("✔ "):
            listbox.delete(index)
            listbox.insert(index, "✔ " + texte)
        else:

            texte = texte.replace("✔ ", "")
            listbox.delete(index)
            listbox.insert(index, texte)

    except:
        pass

window = tk.Tk()
window.title("Liste des tâches")
window.geometry("350x300")


entry = tk.Entry(window, width=30)
entry.pack(pady=10)


btn_add = tk.Button(window, text="Ajouter", command=ajouter_tache)
btn_add.pack(pady=5)


listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)


listbox.bind("<<ListboxSelect>>", terminer_tache)


btn_delete = tk.Button(window, text="Supprimer", command=supprimer_tache)
btn_delete.pack(pady=5)


window.mainloop()