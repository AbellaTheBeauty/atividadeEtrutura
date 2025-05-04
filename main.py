from categoria import Categoria
from desktop import Desktop
from notebook import Notebook
import tkinter as tk
from tkinter import messagebox


import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")

        # Criar frames para Desktop e Notebook
        self.frame_desktop = tk.Frame(root)
        self.frame_notebook = tk.Frame(root)

        # Botões para selecionar tipo de produto
        tk.Button(root, text="Cadastrar Desktop", command=self.show_desktop_form).pack(pady=10)
        tk.Button(root, text="Cadastrar Notebook", command=self.show_notebook_form).pack(pady=10)

    def show_desktop_form(self):
        self.frame_notebook.pack_forget()
        self.frame_desktop.pack()
        self.create_desktop_form()

    def show_notebook_form(self):
        self.frame_desktop.pack_forget()
        self.frame_notebook.pack()
        self.create_notebook_form()

    def create_desktop_form(self):
        for widget in self.frame_desktop.winfo_children():
            widget.destroy()

        tk.Label(self.frame_desktop, text="Modelo:").grid(row=0, column=0)
        self.modelo_entry = tk.Entry(self.frame_desktop)
        self.modelo_entry.grid(row=0, column=1)

        tk.Label(self.frame_desktop, text="Cor:").grid(row=1, column=0)
        self.cor_entry = tk.Entry(self.frame_desktop)
        self.cor_entry.grid(row=1, column=1)

        tk.Label(self.frame_desktop, text="Preço:").grid(row=2, column=0)
        self.preco_entry = tk.Entry(self.frame_desktop)
        self.preco_entry.grid(row=2, column=1)

        tk.Label(self.frame_desktop, text="Categoria ID:").grid(row=3, column=0)
        self.categoria_id_entry = tk.Entry(self.frame_desktop)
        self.categoria_id_entry.grid(row=3, column=1)

        tk.Label(self.frame_desktop, text="Categoria Nome:").grid(row=4, column=0)
        self.categoria_nome_entry = tk.Entry(self.frame_desktop)
        self.categoria_nome_entry.grid(row=4, column=1)

        tk.Label(self.frame_desktop, text="Potência da Fonte:").grid(row=5, column=0)
        self.potencia_entry = tk.Entry(self.frame_desktop)
        self.potencia_entry.grid(row=5, column=1)

        tk.Button(self.frame_desktop, text="Cadastrar", command=self.cadastrar_desktop).grid(row=6, columnspan=2)

    def create_notebook_form(self):
        for widget in self.frame_notebook.winfo_children():
            widget.destroy()

        tk.Label(self.frame_notebook, text="Modelo:").grid(row=0, column=0)
        self.modelo_entry = tk.Entry(self.frame_notebook)
        self.modelo_entry.grid(row=0, column=1)

        tk.Label(self.frame_notebook, text="Cor:").grid(row=1, column=0)
        self.cor_entry = tk.Entry(self.frame_notebook)
        self.cor_entry.grid(row=1, column=1)

        tk.Label(self.frame_notebook, text="Preço:").grid(row=2, column=0)
        self.preco_entry = tk.Entry(self.frame_notebook)
        self.preco_entry.grid(row=2, column=1)

        tk.Label(self.frame_notebook, text="Categoria ID:").grid(row=3, column=0)
        self.categoria_id_entry = tk.Entry(self.frame_notebook)
        self.categoria_id_entry.grid(row=3, column=1)

        tk.Label(self.frame_notebook, text="Categoria Nome:").grid(row=4, column=0)
        self.categoria_nome_entry = tk.Entry(self.frame_notebook)
        self.categoria_nome_entry.grid(row=4, column=1)

        tk.Label(self.frame_notebook, text="Tempo de Bateria:").grid(row=5, column=0)
        self.tempo_bateria_entry = tk.Entry(self.frame_notebook)
        self.tempo_bateria_entry.grid(row=5, column=1)

        tk.Button(self.frame_notebook, text="Cadastrar", command=self.cadastrar_notebook).grid(row=6, columnspan=2)

    def cadastrar_desktop(self):
        modelo = self.modelo_entry.get()
        cor = self.cor_entry.get()
        preco = float(self.preco_entry.get())
        categoria_id = int(self.categoria_id_entry.get())
        categoria_nome = self.categoria_nome_entry.get()
        potencia = self.potencia_entry.get()

        categoria = Categoria(categoria_id, categoria_nome)
        desktop = Desktop(modelo, cor, preco, categoria, potencia)
        desktop.cadastrar()
        messagebox.showinfo("Sucesso", "Desktop cadastrado com sucesso!")

    def cadastrar_notebook(self):
        modelo = self.modelo_entry.get()
        cor = self.cor_entry.get()
        preco = float(self.preco_entry.get())
        categoria_id = int(self.categoria_id_entry.get())
        categoria_nome = self.categoria_nome_entry.get()
        tempo_bateria = self.tempo_bateria_entry.get()

        categoria = Categoria(categoria_id, categoria_nome)
        notebook = Notebook(modelo, cor, preco, categoria, tempo_bateria)
        notebook.cadastrar()
        messagebox.showinfo("Sucesso", "Notebook cadastrado com sucesso!")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()