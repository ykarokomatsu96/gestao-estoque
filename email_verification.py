import smtplib
from email.mime.text import MIMEText

def enviar_email_verificacao(destinatario, nome):
    remetente = "seu.email@gmail.com"
    senha = "SUA_SENHA_DE_APP"

    corpo_email = f"""
    Olá {nome},

    Obrigado pelo cadastro no nosso sistema.

    Por favor, clique no link abaixo para verificar seu email:

    http://seusite.com/verificar?email={destinatario}

    Atenciosamente,
    Equipe do Sistema
    """

    msg = MIMEText(corpo_email)
    msg['Subject'] = "Verificação de Email"
    msg['From'] = remetente
    msg['To'] = destinatario

    try:
        servidor = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        servidor.login(remetente, senha)
        servidor.sendmail(remetente, destinatario, msg.as_string())
        servidor.quit()
        return True
    except Exception as e:
        print("Erro ao enviar email:", e)
        return False
