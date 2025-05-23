import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        pesos = float(entrada_pesos.get())
        moneda = opcion_moneda.get()

        if moneda == "Dólar":
            resultado = pesos / 900
        elif moneda == "Euro":
            resultado = pesos / 970
        elif moneda == "Real":
            resultado = pesos / 180
        else:
            resultado = 0

        caja_resultado.config(state=tk.NORMAL)
        caja_resultado.delete(0, tk.END)
        caja_resultado.insert(0, f"{resultado:.2f}")
        caja_resultado.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresá un número válido")

# Ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Monedas")
ventana.config(width=400, height=300)
ventana.resizable(False, False)

# Etiqueta y campo para pesos
tk.Label(text="Pesos argentinos:").place(x=30, y=30)
entrada_pesos = tk.Entry()
entrada_pesos.place(x=170, y=30, width=150)

# Menú de opciones
tk.Label(text="Convertir a:").place(x=30, y=80)
opcion_moneda = tk.StringVar(value="Dólar")
menu = tk.OptionMenu(ventana, opcion_moneda, "Dólar", "Euro", "Real")
menu.place(x=170, y=75)

# Botón convertir
tk.Button(text="Convertir", command=convertir).place(x=150, y=130, width=100, height=40)

# Resultado
tk.Label(text="Resultado:").place(x=30, y=200)
caja_resultado = tk.Entry(state=tk.DISABLED)
caja_resultado.place(x=170, y=200, width=150)

ventana.mainloop()
