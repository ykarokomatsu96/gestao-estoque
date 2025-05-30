import customtkinter as ctk
from tkinter import messagebox

def mostrar_confirmacao(mensagem):
    ctk.CTkMessageBox(title="Confirmação", message=mensagem).show()
    # ou use messagebox.showinfo("Confirmação", mensagem)
