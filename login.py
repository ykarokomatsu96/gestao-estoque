import customtkinter as ctk
from cadastro import abrir_cadastro
from tkinter import messagebox

def abrir_login():
    app = ctk.CTk()
    app.title("Login - Sistema de Gestão")
    app.geometry("350x400")
    app.resizable(False, False)

    ctk.CTkLabel(app, text="Login", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

    entry_email = ctk.CTkEntry(app, placeholder_text="Email")
    entry_email.pack(pady=10, padx=20, fill="x")

    entry_senha = ctk.CTkEntry(app, placeholder_text="Senha", show="*")
    entry_senha.pack(pady=10, padx=20, fill="x")

    def login():
        email = entry_email.get().strip()
        senha = entry_senha.get().strip()
        # Simule validação
        if email == "admin@admin.com" and senha == "admin123":
            messagebox.showinfo("Sucesso", "Login efetuado!")
            app.destroy()
            # Aqui você pode chamar main window depois do login
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos!")

    btn_login = ctk.CTkButton(app, text="Entrar", command=login, corner_radius=12, fg_color="#4a90e2")
    btn_login.pack(pady=20, padx=20, fill="x")

    btn_cadastrar = ctk.CTkButton(app, text="Cadastrar", command=lambda: abrir_cadastro(app), corner_radius=12)
    btn_cadastrar.pack(pady=5, padx=20, fill="x")

    app.mainloop()
