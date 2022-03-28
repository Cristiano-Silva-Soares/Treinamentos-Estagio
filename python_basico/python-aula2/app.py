import requests
import smtplib
import yagmail

results = requests.get('https://jsonplaceholder.typicode.com/users')


ok = results.json()

contents = []
for n in ok:
    variable = n.get('name')
    contents.append(variable)

names = ','.join(contents)

yagmail.register('cristianodasilvasoares777@gmail.com', 'CDZelegal123#')
yag = yagmail.SMTP('cristianodasilvasoares777@gmail.com')
yag.send('osenias.oliveira@fpf.br', 'Atividade da aula 02 - Python básico.', names)




# #Configuration for the email sending
# host = 'mario-ThinkCentre-Edge72'
# port = 587
# user = 'cristianodasilvasoares777@gmail.com'
# password = 'CDZelegal123#'
#
# #Criando objeto
# print('Creating object server....')
# server = smtplib.SMTP(host, port)
#
# #Login com servidor
# print('Login....')
# server.ehlo()
# server.starttls()
# server.login(user, password)
#
# #Criando Mensagem
# message = variable
# print('Criando mensagem....')
# email_msg = MIMEMultipart()
# email_msg['From'] = user
# email_msg['To'] = 'osenias.oliveira@fpf.br'
# email_msg['Subject'] = 'Atividade da aula 02 - Python básico.'
# print('Adicionando texto....')
# email_msg.attach((MIMEText(message, 'plain')))
#
# #Enviando mensagem
# print('Enviando mensagem....')
# server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
# print('Mensagem enviada!')
# server.quit()





