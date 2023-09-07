import tkinter as tk
import os
import threading

def search_directories():
    keyword = entry.get()
    path = path_entry.get() 
    print("PATH", path)
    
    if not os.path.isdir(path) or path.strip()=="" :
        path = None
    
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, "Buscando directorios que coincidan...")
    
    def search_thread():
        
        matching_directories = [d for d in os.listdir(path) if os.path.isdir(d) and keyword in d]
        result_text.delete('1.0', tk.END)
        if matching_directories:
            for n, directory in enumerate(matching_directories):
                result_text.insert(tk.END, f"{n}. {directory}" + '\n', "directory")
        else:
            result_text.insert(tk.END, "No se encontraron directorios que coincidan.")
        search_button.config(state=tk.NORMAL)  # Habilitar el botón después de terminar la búsqueda
    
    search_button.config(state=tk.DISABLED)  # Deshabilitar el botón durante la búsqueda
    loading_label.grid(row=1, column=1)  # Mostrar el ícono de carga
    threading.Thread(target=search_thread).start()
    loading_label.config(text="Completado", fg="green")

# Crear la ventana principal
root = tk.Tk()
root.title("Búsqueda de Directorios")

# Crear los elementos de la interfaz
label = tk.Label(root, text="Ingrese una palabra:")
label.grid(row=0, column=0, padx=10, pady=10)

path_label = tk.Label(root, text="Ingrese una ruta:")
path_label.grid(row=1, column=0, padx=10, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

path_entry = tk.Entry(root)
path_entry.grid(row=1, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Buscar", command=search_directories)
search_button.grid(row=0, column=2, padx=10, pady=10)


loading_label = tk.Label(root, text="Buscando...", font=("Helvetica", 12))
current_path = os.path.dirname(__file__)
current_path_label = tk.Label(root, text=f"{current_path}", font=("Helvetica", 12))
current_path_label.grid(row=3, column=1, padx=10, pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.grid(row=2, columnspan=3, padx=10, pady=10)
result_text.tag_configure("directory", foreground="blue")

# Iniciar el bucle principal de la aplicación
root.mainloop()
