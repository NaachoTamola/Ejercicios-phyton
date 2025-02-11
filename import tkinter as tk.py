import tkinter as tk
from tkinter import ttk

def main():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Aplicación con Tkinter y UX/UI")
    root.geometry("400x300")
    
    # Aplicar un tema moderno usando ttk (puedes probar 'clam', 'alt', 'default', etc.)
    style = ttk.Style(root)
    style.theme_use('clam')
    
    # Crear un frame principal con padding para darle espacio a los widgets
    mainframe = ttk.Frame(root, padding="20")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    
    # Configurar el redimensionamiento
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    
    # Título de la aplicación (Label principal)
    title_label = ttk.Label(mainframe, text="Bienvenido a mi App", font=("Helvetica", 16))
    title_label.grid(column=0, row=0, columnspan=2, pady=(0, 10))
    
    # Etiqueta y campo de entrada para el nombre
    name_label = ttk.Label(mainframe, text="Ingresa tu nombre:")
    name_label.grid(column=0, row=1, sticky=tk.W, pady=(5, 5))
    
    name_entry = ttk.Entry(mainframe, width=30)
    name_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=(5, 5))
    
    # Función para mostrar un saludo
    def saludar():
        nombre = name_entry.get()
        saludo = f"¡Hola, {nombre}!"
        saludo_label.config(text=saludo)
    
    # Botón para ejecutar la acción de saludar
    greet_button = ttk.Button(mainframe, text="Saludar", command=saludar)
    greet_button.grid(column=0, row=2, columnspan=2, pady=(10, 5))
    
    # Etiqueta para mostrar el saludo (resultado)
    saludo_label = ttk.Label(mainframe, text="", font=("Helvetica", 14), foreground="blue")
    saludo_label.grid(column=0, row=3, columnspan=2, pady=(5, 5))
    
    # Ejecutar el loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
