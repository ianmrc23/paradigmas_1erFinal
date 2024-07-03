import os
import pickle
import tkinter as tk


def get_main_dir(subdir=""):
    """
    Obtiene el directorio principal del proyecto.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    main_dir = os.path.join(current_dir, "..")
    if subdir:
        return os.path.join(main_dir, subdir)
    return main_dir


def save_pickle_file(data, filename):
    """
    Guarda datos en un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "wb") as file:
        pickle.dump(data, file)


def load_pickle_file(filename):
    """
    Carga datos desde un archivo pickle.
    """
    filepath = get_main_dir(f"db/{filename}")
    with open(filepath, "rb") as file:
        return pickle.load(file)


def file_exists(file_path):
    """
    Verifica si un archivo existe en la ruta especificada.
    """
    return os.path.exists(get_main_dir(f"db/{file_path}"))


class CustomMessageBox(tk.Toplevel):
    def __init__(self, parent, title, message, bg_color="white", text_color="black"):
        super().__init__(parent)
        self.title(title)
        self.configure(bg=bg_color)

        label_message = tk.Label(
            self, text=message, bg=bg_color, fg=text_color)
        label_message.pack(padx=20, pady=10)

        btn_ok = tk.Button(self, text="OK", command=self.destroy)
        btn_ok.pack(pady=10)

        self.geometry("+%d+%d" %
                      (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))

    def show(self):
        self.transient(self.master)
        self.grab_set()
        self.wait_window()
