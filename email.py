import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>se você recebeu esse email significa que deu certo...</p>
    <p>brabo</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "teste de envio de email"
    msg['From'] = 'guigames543@gmail.com'
    msg['To'] = 'guilhermecustodionieto@gmail.com'
    password = '22827496' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()