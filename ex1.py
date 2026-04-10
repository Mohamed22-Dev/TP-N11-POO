import tkinter as tk

def convertir():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except:
        label_result.config(text="Entrée invalide")

window = tk.Tk()
window.title("Conversion Température")
window.geometry("300x200")


label_celsius = tk.Label(window, text="Température en Celsius :")
label_celsius.pack(pady=5)


entry_celsius = tk.Entry(window)
entry_celsius.pack(pady=5)


btn_convertir = tk.Button(window, text="Convertir", command=convertir)
btn_convertir.pack(pady=10)

label_result = tk.Label(window, text="")
label_result.pack(pady=5)

window.mainloop()