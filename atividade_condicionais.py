import os
idade = int(input('DIgite sua idade:'))
par_ou_impar = idade%2

if par_ou_impar == 0:
    print('Sua idade é um número par')
else:
    print('Sua idade é um número ímpar')

idade2 = int(input('Digite sua idade:'))

if idade2 > 0 and idade2 <= 12:
    print('Criança')
elif idade2 > 12 and idade2 < 18:
    print('Adolescente')
else:
    print('Adulto')