from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def getNomeEmails():
    nomes = []
    emails = []
    dados = []

    with open('emails.csv', 'r', encoding='utf8') as arquivo:
        for info in arquivo:
           dados.append(info.replace('\n', '').split())

    for item in dados:
        nomes.append(item[0]).replace(',', '.')
        emails.append(item[1])

    return nomes, emails

def getTemplate():

    with open ('template.txt', 'r', encoding='utf8') as arquivo:
        template = arquivo.read()

        return Template(template) 
    
def connect(nomes, emails):

    s = smtplib.SMTP(host='DIGITAR MEU IP DE CASA AQUI', port= 'DIGITAR MINHA PORTA')
    s.starttlsr() #se não acender, significa que está bloqueado pelo firewall
    s.login('seu email', 'senha')

    for nome, email in zip(nomes, emails):
        msg = MIMEMultipart()

        mensagem = template.substitute(nome_pessoa = nome)

    #configurando o setup

        msg['From'] = 'INSERIR O EMAIL QUE VAI DISPARAR'
        msg['To'] = email
        msg['Subject'] = 'INSERIR AQUI O TÍTULO'

        msg.attach(MIMEText(mensagem, 'plain'))

        s.send_message(msg)

# connect(getNomeEmails()[0], getNomeEmails()[1], getTemplate())

