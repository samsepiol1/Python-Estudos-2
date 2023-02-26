import smtplib

fromaddr = '<email_de>'
toaddrs = '<email_para>'
msg = '<mensagem>'
subject = '<subject>'
message = 'Subject: %s\n\n%s' % (subject, msg)

# Dados da conta utilizada para enviar o email
username = '<login>'
password = '<senha>'

# Lógica de envio dos dados
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(fromaddr, toaddrs, message)
server.quit()



