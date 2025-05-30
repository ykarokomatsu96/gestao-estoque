import customtkinter as ctk
from tkinter import messagebox
import re
from email_verification import enviar_email_verificacao
from gestao import Gestao

def formatar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) > 14:
        cnpj = cnpj[:14]
    cnpj_formatado = ''
    if len(cnpj) >= 1:
        cnpj_formatado += cnpj[:2]
    if len(cnpj) >= 3:
        cnpj_formatado += '.' + cnpj[2:5]
    if len(cnpj) >= 6:
        cnpj_formatado += '.' + cnpj[5:8]
    if len(cnpj) >= 9:
        cnpj_formatado += '/' + cnpj[8:12]
    if len(cnpj) >= 13:
        cnpj_formatado += '-' + cnpj[12:14]
    return cnpj_formatado

def formatar_cep(cep):
    cep = re.sub(r'\D', '', cep)
    if len(cep) > 8:
        cep = cep[:8]
    if len(cep) > 5:
        return cep[:5] + '-' + cep[5:]
    else:
        return cep

def formatar_celular(cel):
    cel = re.sub(r'\D', '', cel)
    if len(cel) > 11:
        cel = cel[:11]
    if len(cel) > 7:
        return f'({cel[:2]}) {cel[2:7]}-{cel[7:]}'
    elif len(cel) > 2:
        return f'({cel[:2]}) {cel[2:]}'
    elif len(cel) > 0:
        return f'({cel}'
    else:
        return cel

def abrir_cadastro(janela_login):
    janela_cadastro = ctk.CTkToplevel(janela_login)
    janela_cadastro.title("Cadastro - Sistema de Gestão")
    janela_cadastro.geometry("400x600")
    janela_cadastro.resizable(True, True)
    janela_cadastro.grab_set()

    janela_cadastro.grid_columnconfigure(0, weight=1)

    # Título centralizado
    ctk.CTkLabel(janela_cadastro, text="Cadastro de Estabelecimento", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, pady=20)

    # Função para criar label e input verticalmente alinhados e centralizados
    def criar_campo(row, texto):
        label = ctk.CTkLabel(janela_cadastro, text=texto)
        label.grid(row=row*2-1, column=0, sticky="n", pady=(10, 2))
        entry = ctk.CTkEntry(janela_cadastro, width=300)
        entry.grid(row=row*2, column=0, sticky="n", pady=(0,10))
        return entry

    # Campos
    tipo_label = ctk.CTkLabel(janela_cadastro, text="Tipo de Estabelecimento")
    tipo_label.grid(row=1, column=0, sticky="n", pady=(10, 2))
    tipo_var = ctk.StringVar(value="Supermercado")
    tipo_box = ctk.CTkComboBox(janela_cadastro, values=["Supermercado", "Padaria"], variable=tipo_var, width=300)
    tipo_box.grid(row=2, column=0, sticky="n", pady=(0, 10))

    nome_entry = criar_campo(3, "Nome")
    email_entry = criar_campo(4, "Email")
    senha_entry = criar_campo(5, "Senha")
    senha_entry.configure(show="*")
    cnpj_entry = criar_campo(6, "CNPJ")
    cep_entry = criar_campo(7, "CEP")
    endereco_entry = criar_campo(8, "Endereço")
    celular_entry = criar_campo(9, "Celular")

    def on_cnpj_change(event):
        texto = cnpj_entry.get()
        novo = formatar_cnpj(texto)
        cnpj_entry.delete(0, ctk.END)
        cnpj_entry.insert(0, novo)

    def on_cep_change(event):
        texto = cep_entry.get()
        novo = formatar_cep(texto)
        cep_entry.delete(0, ctk.END)
        cep_entry.insert(0, novo)

    def on_celular_change(event):
        texto = celular_entry.get()
        novo = formatar_celular(texto)
        celular_entry.delete(0, ctk.END)
        celular_entry.insert(0, novo)

    cnpj_entry.bind("<KeyRelease>", on_cnpj_change)
    cep_entry.bind("<KeyRelease>", on_cep_change)
    celular_entry.bind("<KeyRelease>", on_celular_change)

    def cadastrar():
        tipo = tipo_var.get()
        nome = nome_entry.get().strip()
        email = email_entry.get().strip()
        senha = senha_entry.get().strip()
        cnpj = cnpj_entry.get().strip()
        cep = cep_entry.get().strip()
        endereco = endereco_entry.get().strip()
        celular = celular_entry.get().strip()

        if not (nome and email and senha and cnpj and cep and endereco and celular):
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return
        if '@' not in email or '.' not in email:
            messagebox.showerror("Erro", "Email inválido.")
            return
        if len(senha) < 6:
            messagebox.showerror("Erro", "Senha deve ter pelo menos 6 caracteres.")
            return

        gestao = Gestao("sistema.db")
        sucesso = gestao.cadastrar_estabelecimento(tipo, nome, email, senha, cnpj, cep, endereco, celular)
        if sucesso:
            enviar_email_verificacao(email, nome)
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso. Verifique seu email.")
            janela_cadastro.destroy()
        else:
            messagebox.showerror("Erro", "Erro ao cadastrar estabelecimento. Verifique se o email ou CNPJ já está cadastrado.")

    botao_cadastrar = ctk.CTkButton(janela_cadastro, text="Cadastrar", command=cadastrar, width=300)
    botao_cadastrar.grid(row=20, column=0, pady=20)

