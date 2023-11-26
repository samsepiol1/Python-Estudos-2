import email


import imaplib
// Modificação no email
user='email.teste@gmail.com'


server='imap.gmail.com'

#Abrindo conexão SSL e navegando até o inbox
mail=imaplib.IMAP4_SSL(server)

mail.login(user,password)

#Selecionar a caixa de entrada
mail.select('inbox')

#Retornar todos os email da lista
status,data=mail.search(None,'ALL')

#Separar os ID's obtidos em data
mail_ids=[]

#Concatenar a lista obtidas em datas com a nova lista que criamos
for block in data:
    mail_ids+=block.split()
#Para cada ID obtido podemos baixar o email e extrair o seu conteúdo
# Utilizando o protocolo IMAP para o funcionamento do envio e recepção do email
for i in mail_ids:
    status,data=mail.fetch(i,'(RFC822)')
    for response_part in data:
        if isinstance(response_part,tuple):
            message = email.message_from_bytes(response_part[1])
            str(message)
            #Com as informações extraidas aqui podemos pegar o assunto e o nome de quem enviou o email
            mail_from=message['from']
            mail_subject=['subject']

            #Para a leitura encontramos um problema. Se o email conter algum anexo, ele não vai vim no Payload
            if message.is_multipart():
                mail_content=''
                for part in message.get_payload():
                    if part.get_content_type()=='text/plain':
                        mail_content+=part.get_payload()
            else:
                mail_content=message.get_payload()
            # Mostrar informações
            print(f'From {mail_from}')
            print(f'Subject{mail_subject}')
            print(f'Content{mail_content}')



