import pandas as pd
from time import sleep
print('=' * 10,'PROGRAMA PARA ENTREGAS FACILITADAS DO RIO DE JANEIRO','=' *10)
print('''\033[1;31mNOTA:\033[m
\033[1;32;40mO PROGRAMA TEM COMO INTUITO, RECONHECER A REGIÃO ONDE O ENTREGADOR RESIDE,PARA QUE ASSIM POSSA FAZER\033[m
\033[1;32;40mUMA LEITURA DA MESMA, EXIBINDO SOMENTE OS BAIRROS E ADJACÊNCIAS DA AQUELA REGIÃO,TORNANDO ASSIM\033[m
\033[1;32;40mA ENTREGA MAIS ÁGIL E SEGURA!\033[m''')

#sleep(3)
nome = str(input(('Digite seu nome:'))).upper()
print('-' * 20)
while not nome.split():
    nome = str(input(('\033[1;31mDADOS INVÁLIDOS!\033[m Digite seu Nome:'))).upper().strip()

idade =(input('Qual sua Idade?:'))
print('-' * 20)
while not idade.isnumeric():
    idade = (input('\033[1;31mDADOS INVÁLIDOS!\033[m Digite sua idade:'))
    print('-' * 20)
zona = str(input('Qual Zona do Rj você reside?\033[37;40mEx:\033[m[Zona Norte]•[Zona Sul]•[Zona Oeste]•[Zona Central]'
'Digite:')).strip().upper()
while zona not in 'ZONA SUL ZONA NORTE ZONA OESTE ZONA CENTRAL':
    zona = str(input('\033[1;31mDADOS INVÁLIDOS!\033[m Digite novamente:')).strip().upper()

print('-¬' * 14)
print('\033[1;32mINFORMAÇÕES DO ENTREGADOR:\nNOME:{}\nIDADE:{}\nREGIÃO:{}\033[m'.format(nome,idade,zona))
print('-¬' * 14)
sleep(2)

zs = ['Botafogo','Catete','Copacabana','Cosme Velho','Flamengo','Gávea','Glória','Humaitá','Ipanema','Jardim Botânico',
'Entre outros... ▬']
zn = ['Alto da Boa Vista','Andaraí','Grajaú','Maracanã','Praça da Bandeira','Tijuca','Vila Isabel','Abolição',
'Água Santa','Cachambi','Entre outros... ▬']
zo = ['Anil','Barra da Tijuca','Camorim','Cidade de Deus','Curicica','Freguesia de Jacarepaguá','Gardênia Azul',
'Grumari','Itanhangá','Jacarepaguá','Entre outros... ▬']
zc = ['Bairro Imperial de São Cristóvão','Benfica','Caju','Catumbi','Centro','Cidade Nova','Estácio','Gamboa','Lapa',
'Mangueira','Entre outros... ▬']
df = pd.DataFrame(zs)
df2 = pd.DataFrame(zn)
df3 = pd.DataFrame(zo)
df4 = pd.DataFrame(zc)

if zona == 'ZONA SUL':
    print('\033[1;34;40m{}\033[m, com base na sua região,suas entregas irá abranger os bairros:{}'.format(nome,df))
elif zona == 'ZONA NORTE':
    print('\033[1;34;40m{}\033[m, com base na sua região,suas entregas irá abranger os bairros:{}'.format(nome,df2))
elif zona == 'ZONA OESTE':
    print('\033[1;34;40m{}\033[m, com base na sua região,suas entregas irá abranger os bairros:{}'.format(nome,df3))
elif zona == 'ZONA CENTRAL':
    print('\033[1;34;40m{}\033[m, com base na sua região,suas entregas irá abranger os bairros:{}'.format(nome,df4))


print('=' * 35)
print('\033[1;36m{}, lhe desejamos um bom trabalho!\033[m'.format(nome))
print('=' * 35)

