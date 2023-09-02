import imaplib
import email
from_email=""
from_pwd=''
smtp_port=993
smtp_server='imap.gmail.com'
mail=imaplib.IMAP4_SSL(smtp_server)
mail.login(from_email,from_pwd)
mail.select('inbox',readonly=False)
type_mail,data=mail.search(None,"ALL")
mail_ids=data[0]
id_list=mail_ids.split()
first_email_id =int(id_list[0])
latest_email_id=int(id_list[-1])
for i in range(latest_email_id, first_email_id, -1):
 typ, data = mail.fetch(str.encode(str(i)), '(RFC822)')
 msg = email.message_from_string([1].decode('utf-8'))
 email_subject = msg['subject']
 email_from = msg['from']
 mail_str = str(msg)
print(mail_str)
