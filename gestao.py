import sqlite3
import customtkinter as ctk
from tkinter import messagebox

class Gestao:
    def __init__(self, banco):
        self.banco = banco
        self.criar_tabelas()

    def criar_tabelas(self):
        con = sqlite3.connect(self.banco)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS estabelecimentos
                       (cnpj TEXT, nome TEXT, email TEXT, senha TEXT, tipo TEXT)''')
        con.commit()
        con.close()

    def cadastrar_estabelecimento(self, cnpj, nome, email, senha, tipo):
        con = sqlite3.connect(self.banco)
        cur = con.cursor()
        cur.execute("INSERT INTO estabelecimentos VALUES (?, ?, ?, ?, ?)", (cnpj, nome, email, senha, tipo))
        con.commit()
        con.close()

def abrir_main():
    app = ctk.CTk()
    app.geometry("900x600")
    app.title("Painel Principal")

    ctk.CTkLabel(app, text="Bem-vindo ao Sistema de Gestão!", font=("Arial", 24)).pack(pady=30)

    app.mainloop()
